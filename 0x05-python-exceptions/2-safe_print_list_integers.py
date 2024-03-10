#!/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first elments of a list and only integers.

    Args:
        my_list (list): A list contain any type.
        x (int): The numbers of elementsto access in my_list.

    Returns:
        The real number of integers printed.
    """
    num_of_int = 0

    for i in range(0, x):
        try:
            print"({:d}".format(my_list[i]), end='')
            num_of_int += 1
        except (ValueError, TypeError):
            continue
    print('')
    return (num_of_int)

