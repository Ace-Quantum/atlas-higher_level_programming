#!/usr/bin/python3
def divisible_by_2(my_list=[]):
   new_list=[]
   for x in range(0, len(my_list) - 1):
       if x % 2 == 0:
           new_list[x] = True
       else:
            new_list[x] = False
