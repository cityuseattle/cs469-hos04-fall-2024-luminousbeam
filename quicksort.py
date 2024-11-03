def quicksort(arr, left=0, right=None):
  # Initialize the right pointer
  # If right is none, assign it to the last index of the array
  if right is None:
      right = len(arr) - 1
  # left -> first index
  # right -> last index
  if left < right:
      pivot = partition(arr, left, right)
      quicksort(arr, left, pivot - 1)
      quicksort(arr, pivot + 1, right)
  return arr

def partition(arr, left, right):
  '''
  Place the pivot element at its correct position in the array
  Place smaller elements to the left of the pivot
  Place bigger elements to the right of the pivot
  '''
  pivot = left
  index = pivot + 1
  i = index
  while i <= right:
    if arr[i] < arr[pivot]:
      swap(arr, i, index)
      index += 1
    i += 1
  swap(arr, pivot, index - 1)
  return index - 1

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# Test the quicksort function
# First case
arr1 = [5,6,1,5,6,2,3,9,10,55,14,62,859]
print("First test: ", quicksort(arr1))

# Second case
import random

def create_random_int_list(start, stop, length):
  #Validate input
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0

  rd_list = []
  for i in range(length):
    rd_list.append(random.randint(start, stop))
  return rd_list

arr2 = create_random_int_list(0, 1000, 100)
print("Second test: ", quicksort(arr2))