# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:50:02 2017

@author: Zhenning-Henlix
"""

# find the minimum ascii distance between two strings

def helper_cal_dist(str1, str2, common):
    asc1 = [ord(i) for i in str1]
    asc2 = [ord(i) for i in str2]
    asc_common = [ord(i) for i in common]
    score = sum(asc1) + sum(asc2) - 2* sum(asc_common)
    return score 
    
def ascii_distance(str1, str2):
    # find longest common string between two strings
    # create a score matrix to note the similarities between two strings
    n = len(str1)
    m = len(str2)
    d = []
    for i in range(n):
        row = []
        for j in range(m):
            if str1[i] == str2[j]:
                row.append(1)       #1 represents same element
            else: row.append(0)     #0 represents different elements
        d.append(row)
    
    # diagonal "1"'s represent common string
    # the goal is to find the longest string of diagnonal "1"'s
    
    start = 0
    longest = 0 
    distance = helper_cal_dist(str1, str2, "") 
    for i in range(n):
        for j in range(m):
           if d[i][j] ==1:
               length = 0
               temp_start = i
               ind_i = i
               ind_j = j
               while ind_i <n and ind_j <m and d[ind_i][ind_j] ==1:
                   ind_i +=1
                   ind_j +=1
                   length +=1
               common = str1[temp_start:temp_start + length]
               cal_dist = helper_cal_dist(str1, str2, common)
               if cal_dist < distance:
                   longest = length
                   start = temp_start
                   distance = cal_dist
    print distance
            
               
               

str1 = "ab"
str2 = "cabc"

ascii_distance(str1, str2)