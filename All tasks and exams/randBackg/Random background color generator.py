
import random
from PIL import Image

#use a function wjich returns a tuple having the rgb values
def generate_color()->tuple:

    #rgb range from 0 to 255
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return (r,g,b)

color=generate_color()
#visualizing the color
img=Image.new("RGB",(200,200),color)      #takes(mode,size) where mode here is RGB , size in form of a tuple, then the tuple with our rgb values

#displaying
img.show()



#Was unable to run the code even though pillow was installed






