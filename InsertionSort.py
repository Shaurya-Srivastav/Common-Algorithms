#Insertion Sort
"""
Pseudocode:
Given an array of size n:
Iterate through the array starting from the second element:
    Set the current element as the key.
    Compare the key with the elements before it.
    If an element before the key is greater than the key, shift that element to the right.
    Repeat the previous step until we find the correct position for the key.
    Insert the key into its correct position.
Repeat step 1 until the entire array is sorted.

Assumptions:
The algorithm assumes that the input array is not null and has at least one element.
The algorithm only works for sorting arrays.

Explanation:
The insertion sort algorithm builds the final sorted array one element at a time. It iterates 
through the input array and at each iteration, it takes the current element and inserts it into 
its correct position in the sorted part of the array on the left. This process is repeated 
until the entire array is sorted.

Time Complexity:
The insertion sort algorithm has a time complexity of O(n^2) in the worst and average case. 
This is because, in the worst case, for each element, it needs to compare and shift all the 
elements in the sorted part of the array. The number of comparisons and shifts increases with 
the size of the array. Asymptotically, this results in a time complexity of O(n^2).

"""

def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        while i > 0 and key < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


def main(): 
    # Test Cases:
    array = [5,2,6,1,3,4, 10, -1, 0]
    print(InsertionSort(array))

if __name__ == "__main__":
    main()