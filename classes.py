class RectLevel:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


# creating list
me = []
count = 0
count_y = 30  # counter to shift the rect to the higher level in y axis
count_x = 0  # counter to shift the rect to the second rect in x axis(At the same level(

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 440 + count_y, 475 - count_x, 460 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 540 + count_y, 475 - count_x, 560 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 640 + count_y, 475 - count_x, 660 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 740 + count_y, 475 - count_x, 760 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 840 + count_y, 475 - count_x, 860 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level
for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 940 + count_y, 475 - count_x, 960 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 1040 + count_y, 475 - count_x, 1060 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

for k in range(0, 3):
    for j in range(0, 10):
        me.append(RectLevel(435 - count_x, 1140 + count_y, 475 - count_x, 1160 + count_y))
        count_x += 45
    count_y += 30  # increment y to go higher level
    count_x = 0  # make it 0 to return to the start of level

# class to define attributes for Bat and boll
class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
