#!/usr/bin/python3
"""
Someday I will get good at documentation
Today is not that day
"""

def pascal_triangle(n):
    """
    I forgot to document here
    And also to put a 3 at the end of my shebang
    """

    ret_list = []

    if n <= 0:
        return ret_list
    
    for i in range(n):
        current_layer = []
        for j in range(i+1):
            if j > 0 and j < i and i > 0:
                current_layer.append(ret_list[i-1][j-1] + ret_list[i-1][j])
            else:
                current_layer.append(1)
            ret_list.append(current_layer)
        return ret_list