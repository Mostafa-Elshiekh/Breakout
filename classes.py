from global_var import *
class RectLevel:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    # creating list
me=[]
#me=RectLevel(435,444,475,460)
#me1=RectLevel(395,444,420,460)

#new.append(RectLevel(435,444,475,460))
count=0
count_y = 30   # counter to shift the rect to the higher level in y axis
count_x=0      #counter to shift the rect to the second rect in x axis(At the same level(

for k in range(0,4):
 for j in range(0,10):
    me.append(RectLevel(435-count_x, 444+count_y, 475-count_x, 460+count_y))

    count_x+=45

 count_y += 30 #increment y to go higher level
 count_x=0 #make it 0 to return to the start of level

#class to define attributes for Bat and boll
class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top