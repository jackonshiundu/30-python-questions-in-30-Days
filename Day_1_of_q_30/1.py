#Write a Python program to get the largest number from a list.

def get_largest(list):

    max=0

    for x in list:
        if x > max:
            max =x

    return print(max)

get_largest([3,6,4,6,8])
