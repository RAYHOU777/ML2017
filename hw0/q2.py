
import sys
print('ddd')


from PIL import Image
im = Image.open(sys.argv[1])
width,height = im.size

im_n = Image.open(sys.argv[2])


for y in range(height):
    for x in range(width):
         rgba = im.getpixel((x,y))

         rgba_n = im_n.getpixel((x,y))
   #      print rgba
         if (rgba_n[0] == rgba[0]) and rgba_n[1] == rgba[1] and rgba_n[2] == rgba[2] and rgba_n[3] == rgba[3] :
              r = 0
              g = 0
              b = 0
              a = 0 
         else :
              r = rgba_n[0]
              g = rgba_n[1]
              b = rgba_n[2] 
              a = rgba_n[3]

 


         rgba = (r,
                 g,
                 b,
                 a , );
      #   print rgba
         im.putpixel((x,y),(r,g,b,a)) 



print im
im.save("ans_two.png")



