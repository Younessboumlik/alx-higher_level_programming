#!/usr/bin/python3
def  new_in_list(my_list, idx, element):
   
  if len(my_list): 
    if idx < 0 or idx > len(my_list):
       return my_list
    else :
     return my_list[:idx] + [element] + my_list[idx+1:]
