#module_soccer_sprites
import turtle,time
wn=turtle.Screen()
image=[]
def sprite(turtle,m):
    for i in range(27):
        image.append(str(i)+'.gif')
    wn.addshape(image[m])
    turtle.shape(image[m])



