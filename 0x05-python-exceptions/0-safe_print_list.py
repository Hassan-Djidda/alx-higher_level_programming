#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list.
    
    Args:
        my_list (list): the list of the elements to print.
        x (int): The number of element to print from the list.

    Returns:
        The number of printed elements.
    """
    num_of_ele = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i], end=''))
            num_of_ele+= 1
        except IndexError:
            break
    print('\n')
    return (num_of_ele)
