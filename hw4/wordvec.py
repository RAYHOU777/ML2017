from argparse import ArgumentParser
#-- coding: utf-8 --


import word2vec
import numpy as np
import nltk


word2vec.word2phrase('all.txt', 'all-phrases', verbose=True)
word2vec.word2vec('all-phrases', 'model.bin', size=100, verbose=True)

parser = ArgumentParser()
parser.add_argument('--train', action='store_true',
                    help='Set this flag to train word2vec model')
parser.add_argument('--corpus-path', type=str, default='hp/all',
                    help='Text file for training')
parser.add_argument('--model-path', type=str, default='model.bin',
                    help='Path to save word2vec model')
parser.add_argument('--plot-num', type=int, default=500,
                    help='Number of words to perform dimensionality reduction')
args = parser.parse_args()


if args.train:
    # DEFINE your parameters for training
    MIN_COUNT = 0
    WORDVEC_DIM = 0
    WINDOW = 0
    NEGATIVE_SAMPLES = 0
    ITERATIONS = 0
    MODEL = 1
    LEARNING_RATE = np.nan

    # train model
    word2vec.word2vec(
        train=args.corpus_path,
        output=args.model_path,
        cbow=MODEL,
        size=WORDVEC_DIM,
        min_count=MIN_COUNT,
        window=WINDOW,
        negative=NEGATIVE_SAMPLES,
        iter_=ITERATIONS,
        alpha=LEARNING_RATE,
        verbose=True)
else:
    # load model for plotting


    model = word2vec.load(args.model_path)

    vocabs = []                 
    vecs = []                   
    for vocab in model.vocab:
        vocabs.append(vocab)
        vecs.append(model[vocab])
    vecs = np.array(vecs)[:args.plot_num]
    vocabs = vocabs[:args.plot_num]

    '''
    Dimensionality Reduction
    '''
    # from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    tsne = TSNE(n_components=2)
    reduced = tsne.fit_transform(vecs)




    '''
    Plotting
    '''
    import matplotlib.pyplot as plt
    from adjustText import adjust_text

    # filtering
    use_tags = set(['JJ', 'NNP', 'NN', 'NNS'])
    puncts = ["'", '.', ":", ';', ",", '?', "!", "’", "xe2"]
    
    
    plt.figure()
    texts = []
  #  print vocabs

    for i, label in enumerate(vocabs):
        pos = nltk.pos_tag([label])
        xs, ys = reduced[i, :]
   #     print '-------------'
   #     print label[0]
   #     print label
   #     print '************'

        if (label[0].isupper() and len(label) > 1 and pos[0][1] in use_tags
                and (label.find(",")==-1) and(label.find(".")==-1) and
	            (label.find(":")==-1) and
				(label.find(";")==-1) and
				(label.find("!")==-1) and
				(label.find("?")==-1) ):
         #   print'YYYYYYYYYY'
            x, y = reduced[i, :]
            texts.append(plt.text(x, y, label))
            plt.scatter(x, y, s=15, c='r', edgecolors=(1,1,1,0))
	    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')


    adjust_text(texts)

    plt.savefig('hp2.png', dpi=1000)
    plt.show()





'''
        if (label[1].isupper() and len(label) > 1 and pos[0][1] in use_tags
                and all(c not in label for c in puncts)):
            x, y = reduced[i, :]
            texts.append(plt.text(x, y, label))
            plt.scatter(x, y)


        x, y = reduced[i, :]
        texts.append(plt.text(x, y, label))
        plt.scatter(x, y)
'''








