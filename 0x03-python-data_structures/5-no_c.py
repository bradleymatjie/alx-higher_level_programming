#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    for a in my_string:
        if a == 'c' or a == 'C':
            a = ''
    return my_string
no_c("i can see u")
