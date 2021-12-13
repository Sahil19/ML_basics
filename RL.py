# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Changes Made

import random

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

# rows, cols = (2, 10)
# arr = [[0 for i in range(cols)] for j in range(rows)]
# for j in range(cols):
#     arr[0][j] = j
# print(arr)

N = 10
arr = [0]*N
print(arr)

rec = []
choi = []


for iterations in  range(3):
    

    c = random.randint(2,5)
    ch =  random.sample(range(1, 10), c)
    print("Recommendation based on similarity")
    print(ch)
    
    print("After sorting as per reward")
    yx = dict(zip(ch,arr))
    print(yx)
    ch.sort(key=yx.get)
    print(ch)
    # ch = []
    # c = 5
    # for i in range(c):
    #     ch.append(random.randint(0, 9))
    
    recommendation = ' '.join([str(elem) for elem in ch])
    rec.append(recommendation)
      
    print(recommendation) 
    
    x = 0
    z = []
    while x == 0:
        b = int(input('click'))
        z.append(b)
        x = int(input("0 or 1"))
        
    print(z)
    
    v = intersection(ch,z)
    print(v)
    
    choices = ' '.join([str(ele) for ele in v])
    choi.append(choices)
    print(choices)
    
    d = Diff(ch,z)
    print(d)
    
    for m in range(len(v)):
        reward = 1 - ((m+1)/c)
        print(reward)
        fr = v[m]
        arr[fr] = arr[fr] + reward
        
    print(arr)

print(rec)
print(choi)


yx = dict(zip(ch,arr))
ch.sort(key=yx.get)
print(ch)
print(yx)



    