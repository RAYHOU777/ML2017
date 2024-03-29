   
import keras.backend as K 
import pickle
from keras.models import load_model 
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import sys

test_path = sys.argv[1]
output_path = sys.argv[2]

def f1_score(y_true,y_pred):
    thresh = 0.5
    y_pred = K.cast(K.greater(y_pred,thresh),dtype='float32')
    tp = K.sum(y_true * y_pred)
    
    precision=tp/(K.sum(y_pred))
    recall=tp/(K.sum(y_true))
    return 2*((precision*recall)/(precision+recall))

def read_data(path,training):
    print ('Reading data from ',path)
    with open(path,'r') as f:
    
        tags = []
        articles = []
        tags_list = []
        
        f.readline()
        for line in f:
            if training :
                start = line.find('\"')
                end = line.find('\"',start+1)
                tag = line[start+1:end].split(' ')
                article = line[end+2:]
                
                for t in tag :
                    if t not in tags_list:
                        tags_list.append(t)
               
                tags.append(tag)
            else:
                start = line.find(',')
                article = line[start+1:]
            
            articles.append(article)
            
        if training :
            assert len(tags_list) == 38,(len(tags_list))
            assert len(tags) == len(articles)
    return (tags,articles,tags_list)

#(Y_data,X_data,tag_list) = read_data('train_data.csv',True)
(_, X_test,_) = read_data(test_path,False)
#all_corpus = X_data + X_test
model2 =  load_model('best.hdf5', custom_objects={'f1_score': f1_score})
#tokenizer = Tokenizer()
#tokenizer.fit_on_texts(all_corpus)
tag_list = ['SCIENCE-FICTION', 'SPECULATIVE-FICTION', 'FICTION', 'NOVEL', 'FANTASY', "CHILDREN'S-LITERATURE", 'HUMOUR', 'SATIRE', 'HISTORICAL-FICTION', 'HISTORY', 'MYSTERY', 'SUSPENSE', 'ADVENTURE-NOVEL', 'SPY-FICTION', 'AUTOBIOGRAPHY', 'HORROR', 'THRILLER', 'ROMANCE-NOVEL', 'COMEDY', 'NOVELLA', 'WAR-NOVEL', 'DYSTOPIA', 'COMIC-NOVEL', 'DETECTIVE-FICTION', 'HISTORICAL-NOVEL', 'BIOGRAPHY', 'MEMOIR', 'NON-FICTION', 'CRIME-FICTION', 'AUTOBIOGRAPHICAL-NOVEL', 'ALTERNATE-HISTORY', 'TECHNO-THRILLER', 'UTOPIAN-AND-DYSTOPIAN-FICTION', 'YOUNG-ADULT-LITERATURE', 'SHORT-STORY', 'GOTHIC-FICTION', 'APOCALYPTIC-AND-POST-APOCALYPTIC-FICTION', 'HIGH-FANTASY']


#with open("tokenizer.txt", "wb") as f:
#    pickle.dump(tokenizer, f, pickle.HIGHEST_PROTOCOL)
tokenizer = pickle.load(open("tokenizer.txt", "r"))
word_index = tokenizer.word_index
max_article_length =None 
test_sequences = tokenizer.texts_to_sequences(X_test)
test_sequences = pad_sequences(test_sequences,maxlen=max_article_length) 



Y_pred = model2.predict(test_sequences)
thresh = 0.65
with open(output_path,'w') as output:
#   print ('\"id\",\"tags\"',file=output)
     Y_pred_thresh = (Y_pred > thresh).astype('int')
     output.write('"id","tags"\n')
     for index,labels in enumerate(Y_pred_thresh):
         labels = [tag_list[i] for i,value in enumerate(labels) if value==1 ]
         labels_original = ' '.join(labels)
     #       print ('\"%d\",\"%s\"'%(index,labels_original),file=output)
         output.write('"' + str(index) + '"' + ',' + '"' + labels_original + '"' + '\n')
