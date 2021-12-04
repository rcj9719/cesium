'''
Author : Rhuta Joshi
Language : Python 3
Required Library : math
Pre-requisites : pre.data and post.data file in same directory as script
Input : Pixel coordinates for 2 points (comma separated coordinates for each) within range [0,255] along each axis

'''

from math import sqrt

pre_file_name = "pre.data"
post_file_name = "post.data"

# calculates distance between two points based on pre and post height maps
# returns difference after comparing pre and post eruption images
def slope_based_dist(path):
    pre_dist = 0
    post_dist = 0

    for i in range(len(path) - 1):
        x1 = int(path[i][0])
        y1 = int(path[i][1])
        x2 = int(path[i+1][0])
        y2 = int(path[i+1][1])

        py1 = pre_file_data[x1 * 512 + y1]
        py2 = pre_file_data[x2 * 512 + y2]

        pre_dist += sqrt((30 * 30) + (121 * (py2 - py1) * (py2 - py1)))
        py1 = post_file_data[x1 * 512 + y1]
        py2 = post_file_data[x2 * 512 + y2]

        post_dist += sqrt((30 * 30) + (121 * (py2 - py1) * (py2 - py1)))

    return abs(pre_dist - post_dist)


# calculates each pixel on the shortest path of map using DDA line drawing algorithm
def shortest_planar_path(point1, point2): 
    pixels = []
    steps=0
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    x = point1[0]
    y = point1[1]

    if abs(dx)>abs(dy) :
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    Xinc=dx/steps
    Yinc=dy/steps
    pixels.append((int(x), int(y)))

    for k in range(steps):
        x=x+Xinc
        y=y+Yinc
        pixels.append((int(x), int(y)))
    return pixels
        

if __name__ == "__main__":
    with open(pre_file_name, mode='rb') as file:
        pre_file_data = file.read()
    with open(post_file_name, mode='rb') as file:
        post_file_data = file.read()
    
    pre_length = len(pre_file_data)

    point1 = tuple(int(x.strip()) for x in input("Pixel coordinates of point 1 : ").lstrip('(').rstrip(')').split(','))
    point2 = tuple(int(x.strip()) for x in input("Pixel coordinates of point 2 : ").lstrip('(').rstrip(')').split(','))
    
    path = shortest_planar_path(point1, point2)
    diff = slope_based_dist(path)

    print(diff)
