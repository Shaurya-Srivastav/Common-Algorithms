#swap elements in a list
'''
Simple swap, using comma assignment since the positions of the elements are known, we can simply swap the positions of the elements.

Big O Time Complexity: O(1), for using constant operations.

'''

def swap_function(list, idx1, idx2):
    list[idx1], list[idx2] = list[idx2], list[idx1]
    return list

list = [1,3,5,8,10,2]
pos1,pos2 = 0, 2

print(swap_function(list, pos1, pos2))


'''
Simple swap to swap elements at a given position, using a temp variable now.

Big O Time Complexity: O(1), for using constant operations.

'''

def swap_function_tempVar(list, idx1, idx2):
    temp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = temp
    return list
    
list2 = [1,3,5,8,10,2]
print(swap_function_tempVar(list2, pos1, pos2)) 

'''
Simple swap to swap elements at a given position, using Tuples.
Store the element at idx1 and idx2 as a pair in a tuple. 
Unpack those elements with idx2 and idx1 positions in that list. 
Both the positions in that list are swapped. 

Big O Time Complexity: O(1), for using constant operations.

'''
def swap_function_tuples(list, idx1, idx2):
    tupleswap = list[idx1], list[idx2]
    
    list[idx2], list[idx1] = tupleswap
    
    return list

   
list3 = [1,3,5,8,10,2]
print(swap_function_tuples(list3, pos1, pos2)) 
    