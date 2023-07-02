#Binary Search Algorithm
'''
Psuedo Code 
Given an Array of size n
1) Set the min = 0, and the max = len(array) - 1 (sets max variable to the last index of the array). 
2) Find the average of the array and index into it. Check if array[middle] = target
4) if val > target, set max to guess - 1. 
5) if val < target, set min to guess + 1.
6) repeat from step 2.

Assumption: 
The algorithm can run as long as max >= min. Once max = min, we have reached the answer so the loop should break.
* ALGORITHM ONLY WORKS FOR A SORTED LIST *
'''


def binarySearch(array, target):
  min = 0
  max = len(array) - 1
  guess = 0

  while (max >= min):
    guess = (max + min) // 2
    if array[guess] == target:
      return guess
    elif array[guess] > target:
      max = guess - 1
    else:
      min = guess + 1

  return -1


def main():
  arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
  targetVal = int(input("Target Value: "))
  val = binarySearch(arr, targetVal)

  if val != -1:
    print(f"Element exists within array at index: {val} ")
  else:
    print("Element does not exist within the array")


if __name__ == "__main__":
  main()

