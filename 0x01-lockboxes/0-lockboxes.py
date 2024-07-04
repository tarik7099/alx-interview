#!/usr/bin/python3
"""
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""

def canUnlockAll(boxes):
    """
    This function takes a list of lists and returns a boolean indicating
    whether all boxes in the list can be opened. A key with the same
    number as a box opens that box. You can assume all keys will be
    positive integers. There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes
    and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    all_n = len(boxes)
    opened = [False] * all_n
    opened[0] = True
    stack = [0]
    
    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < all_n and not opened[key]:
                opened[key] = True
                stack.append(key)
    
    return all(opened)
