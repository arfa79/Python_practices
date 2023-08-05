# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    new_list=[] #create a new list for slice the numbers
    for n in nums:
        if  len(new_list) == 0 or n != new_list[-1]: # check list not empty and also not equal to each other
            new_list.append(n)                       # append non repeated numbers to a new list
    return print(new_list)
remove_adjacent([1, 2, 2, 3])