"""Hometask 9."""

"""
We have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set if no such
element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should
produce list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions

Advices:
set of (list1 indexes union list2 indexes) could be
helpful to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was not found d1.get(key, 0)
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def list_sum(list1, list2):
    """
    Create a new list from 2 lists.

    The same indexes from 2 lists are collected for 1 tuple.
    If the len of one of the lists is longer, a '0' value
    is set for the missing element.
    """
    # Create 2 dictionaries from our lists with indexes as a key
    d1 = {i: list1[i] for i in range(len(list1))}
    d2 = {i: list2[i] for i in range(len(list2))}

    # New list generation with max list len using
    new_list = [(d1.get(i, 0), d2.get(i, 0))
                for i in range(max(len(list1), len(list2)))]
    return new_list


# Usage example:
l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]
print(list_sum(l1, l2))  # Result: [(2, 1), (4, 2), (6, 3), (8, 0), (10, 0)]
