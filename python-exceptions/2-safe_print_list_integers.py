#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tester = 0
    count = 0
    for x in my_list:
        try:
            tester = my_list[x] + 0
            print("{:d}".format(my_list[x]), end='')
            count += 1
            tester = 0
        except:
            break
    print()
    return count
