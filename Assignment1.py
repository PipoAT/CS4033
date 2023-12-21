# Assigment 1 Hybrid Sort
# Group 39- Clair Grywalski, Andrew Pipo, Max Santos

import time

"""
Part 1:

1. Bubblesort
2. quickSort
3. mergeSort
4. hybridSort
5. several runs of each of these algorithms for lists different lengths
6. At the end of the program file, in a comment section, examples ofruns, and the results obtained along with an analysis comparing the behavior of these algorithms (for example, number of pairwise
element comparisons, or execution time).
"""
comparisons = 0


# 1. BubbleSort
def bubbleSort(array):
  """
    Bubble Sort algorithm to sort the given list in order using comparisons 
    to adjacent elements.
    
    Args:
        array (list): List to be sorted.
    
    Returns:
        list: Sorted list.
    """
  global comparisons
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        comparisons += 1
  return array


# 2. quickSort
def quickSort(array):
  global comparisons
  """
    Quick Sort algorithm to sort the given list in order using a pivot.
    
    Args:
        array (list): List to be sorted.
    
    Returns:
        list: Sorted list.
    """
  if len(array) <= 1:
    return array
  pivot = array[len(array) // 2]
  left = [x for x in array if x < pivot]
  middle = [x for x in array if x == pivot]
  right = [x for x in array if x > pivot]

  comparisons += (len(left) + len(right))

  return quickSort(left) + middle + quickSort(right)


# 3. mergeSort
def mergeSort(array):
  '''
  mergeSort algorithm sorts the given array/list by
  spliting the array/list and sorts those smaller array/lists recursively

  Args:
    array (list): List that needs sorted

  Returns:
    array/list: sorted list
  '''

  # checks for if the array is larger than 1, to which sorting can be utilized
  global comparisons
  if (len(array) > 1):
    mid = len(array) // 2  # determines the middle index
    leftArray, rightArray = array[:mid], array[mid:]

    # calls mergeSort for recursion and breakdown of array
    mergeSort(leftArray)
    mergeSort(rightArray)

    # initialize i, j, k to keep track of indexes
    i = j = k = 0

    # loops runs while the index is withn bounds
    while i < len(leftArray) and j < len(rightArray):
      if leftArray[i] < rightArray[j]:
        # if the left half value is less than the right
        # it is in the correct place and adds to the merged array
        array[k] = leftArray[i]
        # increase index by one
        i += 1
      else:
        # if right half value is less than the left
        # it sets the right value into the merged array
        array[k] = rightArray[j]
        j += 1

      # increase index of merged array
      k += 1

    # loops while the index is within left array's bounds
    while i < len(leftArray):
      array[k] = leftArray[i]
      i, k, comparisons = i + 1, k + 1, comparisons + 1

    # loops while the index is withn right array's bounds
    while j < len(rightArray):
      array[k] = rightArray[j]
      j, k, comparisons = j + 1, k + 1, comparisons + 1

  return array


# 4. hybridSort
def hybridSort(array, big, small, t):
  global comparisons
  #Checks array size against threshold
  if len(array) > t:
    #Checks to see what "big" sorting algorithm was selected
    if big == "mergeSort":

      # Splits list in half like mergeSort
      mid = len(array) // 2
      left_half = array[:mid]
      right_half = array[mid:]

      # Calls bubbleSort on split halves
      leftArray = hybridSort(left_half, big, small, t)
      rightArray = hybridSort(right_half, big, small, t)

      #Returns to merge sort behavoir with two sorted lists
      i = j = k = 0
      while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
          # if the left half value is less than the right
          # it is in the correct place and adds to the merged                       array
          array[k] = leftArray[i]
          # increase index by one
          i += 1
        else:
          # if right half value is less than than the left                          half value
          # it sets the right value into the merged array
          array[k] = rightArray[j]
          j += 1

        # increase index of merged array
        k += 1

      # loops while the index is within left array's bounds
      while i < len(leftArray):
        array[k] = leftArray[i]
        i += 1
        k += 1
        comparisons += 1

      # loops while the index is withn right array's bounds
      while j < len(rightArray):
        array[k] = rightArray[j]
        j += 1
        k += 1
        comparisons += 1

    # If quickSort is selected as "big" sorting algorithm
    else:
      # First pivot is selected and array is divided in half
      pivot = array[len(array) // 2]
      # Middle is selected
      middle = [x for x in array if x == pivot]
      comparisons += 1

      # Then bubble sort the left and right side
      left = hybridSort([x for x in array if x < pivot], big, small, t)
      comparisons += 1
      right = hybridSort([x for x in array if x > pivot], big, small, t)
      comparisons += 1

      #Returns to acting like quick sort
      array = left + middle + right

  #Sorts arrays smaller than the threshold
  elif small == "bubbleSort":
    bubbleSort(array)

  return array


# 5. Running these algorithms
# different sized array/list lengths

# 5.1 bubbleSort
print("-- bubbleSort --")
print(bubbleSort([2, 1]))
print(bubbleSort([2, 1, 3]))
print(bubbleSort([45, 3, 1, 2]))
print(bubbleSort([1, 2, 6, 5, 33]))
print(bubbleSort([6, 5, 4, 3, 2, 1]))

# 5.2 quickSort
print("")
print("-- quickSort --")
print(quickSort([2, 1]))
print(quickSort([2, 1, 3]))
print(quickSort([45, 3, 1, 2]))
print(quickSort([1, 2, 6, 5, 33]))
print(quickSort([6, 5, 4, 3, 2, 1]))

# 5.3 mergeSort
print("")
print("-- mergeSort --")
print(mergeSort([2, 1]))
print(mergeSort([2, 1, 3]))
print(mergeSort([45, 3, 1, 2]))
print(mergeSort([1, 2, 6, 5, 33]))
print(mergeSort([6, 5, 4, 3, 2, 1]))

# 5.4 hybridSort
print("")
print("-- hybridSort --")

print(hybridSort([99, 101, 88, 6], "mergeSort", "bubbleSort", 2))

print(hybridSort([65, 565, 87], "mergeSort", "bubbleSort", 2))

print(hybridSort([65, 5, 8, 2, 25, 1], "mergeSort", "bubbleSort", 2))

print(hybridSort([65, 5], "quickSort", "bubbleSort",3))

print(hybridSort([65, 5, 81, 24], "quickSort", "bubbleSort", 3))

print(hybridSort([65, 5, 8, 2, 25, 1, 15, 21, 109], "quickSort", "bubbleSort",3))

# 6.1 Example Run
"""
-- bubbleSort --
[1, 2]
[1, 2, 3]
[1, 2, 3, 45]
[1, 2, 5, 6, 33]
[1, 2, 3, 4, 5, 6]

-- quickSort --
[1, 2]
[1, 2, 3]
[1, 2, 3, 45]
[1, 2, 5, 6, 33]
[1, 2, 3, 4, 5, 6]

-- mergeSort --
[1, 2]
[1, 2, 3]
[1, 2, 3, 45]
[1, 2, 5, 6, 33]
[1, 2, 3, 4, 5, 6]

-- hybridSort --
[6, 88, 99, 101]
[65, 87, 565]
[1, 2, 5, 8, 25, 65]
[1, 2, 5, 8, 15, 21, 25, 65, 109]
"""
# 6.2 Counting comparisons and execution time
print("")
print("--Execution Time and Comparisons--")
comparisons = 0
time_1 = time.time()
print("BubbleSort: ", bubbleSort([99, 101, 88, 6, 37, 3]))
time_2 = time.time()
print("Time: ", time_2 - time_1)
print("Comparisons: ", comparisons)

comparisons = 0
time_1 = time.time()
print("quickSort: ", quickSort([99, 101, 88, 6, 37, 3]))
time_2 = time.time()
print("Time: ", time_2 - time_1)
print("Comparisons: ", comparisons)

comparisons = 0
time_1 = time.time()
print("mergeSort: ", mergeSort([99, 101, 88, 6, 37, 3]))
time_2 = time.time()
print("Time: ", time_2 - time_1)
print("Comparisons: ", comparisons)

comparisons = 0
time_1 = time.time()
print("Hybrid (merge): ",
      hybridSort([99, 101, 88, 6, 37, 3], "mergeSort", "bubbleSort", 5))
time_2 = time.time()
print("Time: ", time_2 - time_1)
print("Comparisons: ", comparisons)

comparisons = 0
time_1 = time.time()
print("Hybrid (quick): ",
      hybridSort([99, 101, 88, 6, 37, 3], "quickSort", "bubbleSort", 5))
time_2 = time.time()
print("Time: ", time_2 - time_1)
print("Comparisons: ", comparisons)

# 6.3 Info about number of comparisons and execution time
# Sample Run:
"""
--Execution Time and Comparisons--
BubbleSort:  [3, 6, 37, 88, 99, 101]
Time:  1.3828277587890625e-05
Comparisons:  13
quickSort:  [3, 6, 37, 88, 99, 101]
Time:  1.6689300537109375e-05
Comparisons:  9
mergeSort:  [3, 6, 37, 88, 99, 101]
Time:  2.0742416381835938e-05
Comparisons:  7
Hybrid (merge):  [3, 6, 37, 88, 99, 101]
Time:  1.7881393432617188e-05
Comparisons:  7
Hybrid (quick):  [3, 6, 37, 88, 99, 101]
Time:  1.2874603271484375e-05
Comparisons:  8
 
Because the sample array was quite small, BubbleSort took the second shortest amount of time, but still had the highest number of comparisons. It has a time complexity of 0(n^2), but works well on shorter lists as there are significantly less elements to compare that need swapped, and every pass through the lists ends with an element being in the correct place. 

MergeSort (time complexity of 0(n log(n)), took the longest in this sample run but had a tie for lowest number of comparisons with the hybrid mergeSort. QuickSort (time complexity of 0(n log(n)) functioned in a similar capacity as mergeSort but had more comparisons. These both work by partitioning a list and filtering them back together, however mergeSort cuts sublists until each only has one item and then merges everything together, whereas quickSort picks a pivot and merges separate lists back together by using it. 

HybridSort, which utilizes the strengths of BubbleSort on short lists and the strengths of mergeSort or quickSort on longer lists, worked pretty efficiently with less comparisons needed. Long lists were divided, sorted separately using an algorithm that works well for short lists, then sorted back together using algorithms that normally split lists into partitions and then sort them back together. When the partitions are already sorted, merging them back together is easier and takes less time. 

"""
"""
Part 2:

View sorting as a task to be performed by an agent. What kind of
agent architecture would be appropriate for each of the sorting algorithms considered here? In each case discuss the PEAS descriptions.
"""

# BubbleSort PEAS
"""
BUBBLE SORT:
- Performance Measure: For the bubble sort agent the performance measure can be the number of swaps 
required to sort the given list.
- Environment: The unsorted list is provided by what is called the environment. Then, after bubble
sort is run, the environment then receives the sorted output.
- Actuators: The actuator will deliver the sorted list using pairwise element comparisons and swamps
to initially sort it.
- Sensors: The agent will recieve input which in this case is an unsorted list and its elements

Bubble Sort Architecture:
The agent architecture is reflex with state. This is because a reflex agent is suitable since the 
list is continuously being sorted and needs to readjust itself based on the adjacent elements.
"""

# quickSort
"""
QUICK SORT:
- Performance Measure: For the quick sort agent we can use the average number of comparisons.
- Environment: Again, the environment provides the initial list and eventually will receive the 
sorted output.
- Actuators: The agent will select a pivot element and then partition the list. Afterwards, the sublists
created by the partitions become sorted into a single sublist.
- Sensors: The unsorted list in inputted and the agent detects the pivot elements.

Quick Sort Architecture:
The agent architecture is goal-based. This is because the choosing of pivots and sorting of partitions/
sublists can all be classified as agent actions and the goal is to achieve a fully sorted list.
"""
# mergeSort PEAS
"""
MERGE SORT:
- Performance Measure: For the merge sort the number of recursive calls made during sorting
can be the performance measure.
- Environment: Again, the environment provides the initial list and eventually will receive the 
sorted output.
- Actuators: The list will be divided and merges the sublits by the agent to sort the list properly.
- Sensors: The unsorted list is sensed by the agent and eventually the list is divided and re-merged
to sort the list.

Merge Sort Architecture:
The agent architecture for merge sort is goal-based. Like merge sort, its goal is to achieve the
fully sorted list however, to do so, recursion is handled by the agent instead of the sorting
of partitions.


"""
# hybridSort PEAS
"""
HYBRID SORT:
- Performance Measure: The number of comparisons made can be an example of performance measure as it is
related to its efficiency.
- Environment: Again, the environment provides the initial list and eventually will receive the 
sorted output.
- Actuators: The decision between usage of bubble sort, quick sort, or merge sort is made by the agent 
(based on list size and threshold).
- Sensors: The unsorted list size is observed by the agent and the threshold is used to find the proper
sorting stategy

Hybrid Sort Architecture:
The agent architecture for hybrid sort is utility-based. Hybrid sorting requires the agent to have 
responsibility of choosing the proper strategy (based on list size and threshold here) to make decisions. 
This makes hybrid sorting an obvious utility-based agent architecture.
"""
