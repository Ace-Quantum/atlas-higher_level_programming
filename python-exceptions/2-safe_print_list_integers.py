#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tester = 0
    count = 0
    for i in range(0, x):
        try:
            tester = my_list[i] + 0
            print("{:d}".format(my_list[i]), end='')
            count += 1
            tester = 0
        except:
            break
    print()
    return count
