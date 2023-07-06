#selection sort
"""
Pseudocode:
Given an array of size n:
Set the variable minIndex to 0.
Iterate through the array from the beginning:
Set the minIndex to the current index.
Iterate through the remaining unsorted part of the array:
    If the element at the current index is smaller than the element at minIndex, update minIndex to the current index.
    Swap the element at the current index with the element at minIndex.
Repeat steps 2 and 3 until the entire array is sorted.

Assumptions:
The algorithm assumes that the input array is not null and has at least one element.
The algorithm only works for sorting arrays.

Explanation:
The selection sort algorithm divides the input array into two parts: the sorted part and the unsorted part. It repeatedly 
selects the smallest element from the unsorted part and places it at the beginning of the sorted part. This process is 
repeated until the entire array is sorted.

Time Complexity:
The selection sort algorithm has a time complexity of O(n^2) because it involves nested iterations through the array. 
For each element, it searches for the minimum element in the remaining unsorted part, 
resulting in n + (n - 1) + (n - 2) + ... + 1 comparisons, which simplifies to (n * (n - 1)) / 2. 
Asymptotically, this is equivalent to O(n^2).
"""
def selectionSort(array):
    for step in range(len(array)):
        minIndex = step
        for j in range(step+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        
        array[step], array[minIndex] = array[minIndex], array[step]

    return array
 

def main():
    array = [1,3,5,8,2,4,7]
    print(selectionSort(array))


if __name__ == "__main__":
  main()
    