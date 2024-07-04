#!/usr/bin/python3
"""
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""

def can_open_all_boxes(boxes):
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
    total_boxes = len(boxes)
    opened_boxes = set([0])
    keys_to_check = set(boxes[0]).difference(set([0]))
    
    while keys_to_check:
        current_key = keys_to_check.pop()
        if current_key >= total_boxes or current_key < 0:
            continue
        if current_key not in opened_boxes:
            keys_to_check = keys_to_check.union(boxes[current_key])
            opened_boxes.add(current_key)
    
    return total_boxes == len(opened_boxes)

