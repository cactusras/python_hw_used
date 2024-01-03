# import math
# def polar_angle(p0, anchor,p1=None):
#     if p1==None: p1=anchor
#     #...
#     y_span=p0[1]-p1[1]
#     x_span=p0[0]-p1[0]
#     print(y_span)
#     print(x_span)
#     print(math.degrees(math.atan2(y_span, x_span)))

#     return math.atan2(y_span, x_span)

# def insertionSort(arr, anchor):
#     n = len(arr)  # Get the length of the array
 
#     for i in range(1, n):  # Iterate over the array starting from the second element
#         key = polar_angle(arr[i],anchor)  # Store the current element as the key to be inserted in the right position
#         j = i-1
#         while j >= 0 and key < polar_angle(arr[j],anchor):  # Move elements greater than key one position ahead
#             arr[j+1] = arr[j]  # Shift elements to the right
#             j -= 1
#         arr[j+1] = key  # Insert the key in the correct position
#     return arr
# def quicksort(a, anchor):
#   if(len(a)<=1):
#     return a
#   smaller = []
#   equal = []
#   larger = []
#   piv_ang = polar_angle(a[0], anchor)
#   for pt in a:
#     pt_ang= polar_angle(pt, anchor)
#     if pt_ang<piv_ang:
#       smaller.append(pt)
#     elif pt_ang==piv_ang:
#       equal.append(pt)
#     else:
#       larger.append(pt)
#   return quicksort(smaller, anchor)+equal+quicksort(larger, anchor)
# def graham_scan(points, anchor):
#     min_idx=None
#     for i,(x,y) in enumerate(points):
#       if min_idx==None or y<points[min_idx][1]:
#         min_idx=i

#     anchor=points[min_idx]

#     # sort the points by polar angle then delete
#     # the anchor from the sorted list
#     sorted_pts=quicksort(points,anchor)
#     print(sorted_pts)
#     del sorted_pts[sorted_pts.index(anchor)]

#     # anchor and point with smallest polar angle will always be on hull
#     hull=[anchor,sorted_pts[0]]
#     for s in sorted_pts[1:]:
#       while orientation(hull[-2],hull[-1],s) == -1:
#         del hull[-1] # backtrack
#         if len(hull)<2: break
#       hull.append(s)
#     return hull

import itertools
def outerTrees(points):
	
        def ccw(A, B, C):
            return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])

        if len(points) <= 1:
            return points

        hull = []
        points.sort()
        for i in itertools.chain(range(len(points)), reversed(range(len(points)-1))):
            while len(hull) >= 2 and ccw(hull[-2], hull[-1], points[i]) < 0:
                hull.pop()
            hull.append(points[i])
        hull.pop()

        for i in range(1, (len(hull)+1)//2):
            if hull[i] != hull[-1]:
                break
            hull.pop()
        return hull

def orientation(p1,p2,p3):
  d = (p3[1]-p2[1])*(p2[0]-p1[0])-(p2[1]-p1[1])*(p3[0]-p2[0])
  if d > 0:
    return 1
  elif d < 0:
    return -1
  else:
    return 0

def is_inside(edges, xp, yp):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge[0],edge[1]
        if(y1 == y2 and y1 == yp):
           if (xp<=x2 and xp >= x1) or (xp>=x2 and xp<=x1):
              return True
        if (xp == x1 and yp == y1) or (xp == x2 and yp == y2):
           return True
        if (yp<=y1 and yp>y2) or (yp>y1 and yp<=y2):
          if xp<x1+(yp-y1)/(y2-y1)*(x2-x1):
            cnt += 1
          elif xp==x1+(yp-y1)/(y2-y1)*(x2-x1):
             return True
    if cnt%2 == 0:
      return False
    else:
      return True

# inputList = [[2,0], [3,0], [4,1]]
# inputList = [[2,0], [1,1], [2,2], [3,3], [2,4], [4,2]]
# inputList = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
# global anchor
# anchor = {}
# for i in inputList:
#     polar_angle(i, anchor)
# k_m = input()
k_m = input().split(',')
trees = int(k_m[0])
sheeps = int(k_m[1])
# print(trees+sheeps)
# trees = int(input())
inputList = []
sheepList = []
for i in range(trees):
  string_list = input().split(',')
  integer_list = [int(item) for item in string_list]
  inputList.append(integer_list)
for i in range(sheeps):
  string_list = input().split(',')
  integer_list = [int(item) for item in string_list]
  sheepList.append(integer_list)

# answer = outerTrees(inputList)
# i = len(answer)-2
# while i != -2:
#   if(orientation(answer[i-1],answer[i],answer[i+1]) == 0):
#       answer.pop(i)
#   i-=1
edge = []
answer = inputList
j=len(answer)-1
while j >=0 :
   edge.append([answer[j],answer[j-1]])
   j-=1
# print(edge)
s=len(sheepList)-1
while s >=0 :
  if(is_inside(edge, sheepList[s][0], sheepList[s][1])):
    sheepList.pop(s)
  s-=1
print(len(sheepList))
if(len(sheepList) != 0):
   for i in sheepList:
      print("%d,%d" %(i[0],i[1]))
# number = len(answer)
# if(number < 3):
#   print(0)
# elif(number == 3):
#   if(orientation(answer[0],answer[1],answer[2]) == 0):
#     print(0)
#   else:
#     print(3)
# else:
#   i = len(answer)-2
#   while i != -2:
#     if(orientation(answer[i-1],answer[i],answer[i+1]) == 0):
#        answer.pop(i)
#     i-=1

#   # print("answer: ")
#   # print(answer)
#   print(len(answer))