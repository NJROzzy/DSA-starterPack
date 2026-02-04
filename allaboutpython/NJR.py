print("John is learning Python programming for his assesment task.")

# Arrays and String for DSA 
# 2 pointer for DSA 
print("@ line 5 for Arrays and strings examples")

#example 1
# check if a string is palindrome or not

# def check_if_palindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# s =  input("Enter a string to check if it's a palindrome: ")
# print(f"Is the string '{s}' a palindrome? {check_if_palindrome(s)}")

#################### ##########################
# example 2 
# nums = [1,2,3,4,5,6,7,8,9,14,15]
# target = 13, return true becaise 4 + 9 = 13. 

# def numspaircheck(nums, target):
#     left, right = 0, len(nums)-1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return True
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return False
# nums = [1,2,3,4,5,6,7,8,9,14,15]
# target = int(input("Enter a target sum to check for pairs: "))
# print(f"Is there a pair that sums to {target}? {numspaircheck(nums, target)}")

# #################### ##########################
# example 3
# check if the  pointers are subsequent of each other! 

# class Solution:
#     def isSubsequent(self, s: str, t: str) -> bool:
#       i = j = 0
#       while i < len(s) and j < len(t):
#          if s[i] == t[j]:
#             i += 1
#             j += 1
         
#       return i == len(s)
# s = input("Enter the first string (s): ")
# t = input("Enter the second string (t): ")
# solution = Solution()
# print(f"Is '{s}' a subsequence of '{t}'? {solution.isSubsequent(s, t)}")

#################### ##########################
# example 4
# merge two sorted arrays

# def combine(arr1, arr2):
#     ans= []
#     i = j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#             i += 1
#         else: 
#             ans.append(arr2[j])
#             j += 1
    
#     while i < len(arr1):
#         ans.append(arr1[i])
#         i += 1    

#     while j < len(arr2):
#         ans.append(arr2[j])
#         j += 1

#     return ans
# arr1 = [1,3,5,7]
# arr2 = [2,4,6,8]
# print(f"Merged array: {combine(arr1, arr2)}")

#################### ##########################

##################################################
# hashing for DSA
print("@ line 92 for Hashing examples")
#Lets find bob from hash table 

# my_list = ["alice", "bob", "charlie", "david"]

# def find_name( my_list):
   
#     sum_of_chars = 0
#     for x in my_list:
#         sum_of_chars += ord(x)

#     return sum_of_chars % len(my_list)
# print("'bob' has hash code:", find_name('bob'))

# #################### ##########################
# example 2
# check for x in an array using hashing 

# arr = ["r", "y", "z", "a", "b", "c"]

# def check_for_x(arr):
#     hash_set = set(arr)
#     return "x" in hash_set
# print("Is 'x' in the array?", check_for_x(arr))

# time, space complexity = O1(), O(n) 
#################### ##########################
# example 3
# find duplicates in an array using hashing
# nums = [1,2,3,4,5,3,2,1]
# def find_duplicates(nums):
#     hash_set = set()
#     for num in nums:
#         if num in hash_set:
#             return True
#         hash_set.add(num)
#     return False  

##################### ##########################
##########################################
# linear Search DSA
print("@ line 133 for Linear Search examples")
#example 1

# def linaerSearch(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# mylist = [10,20,30,40,50,60]
# x = 4

# result = linaerSearch(mylist, x)
# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found in the list")

##################### ##########################
##########################################

print("@ line 153 for Binary Search examples")
# Binary Search DSA
# example 1
# def binarySearch(arr, targetVal):
#   left = 0
#   right = len(arr) - 1

#   while left <= right:
#     mid = (left + right) // 2

#     if arr[mid] == targetVal:
#       return mid

#     if arr[mid] < targetVal:
#       left = mid + 1
#     else:
#       right = mid - 1

#   return -1

# mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# x = 11

# result = binarySearch(mylist, x)

# if result != -1:
#   print("Found at index", result)
# else:
#   print("Not found")

##################### ##########################
##########################################

# Bubble Sort DSA
# example 1
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if mylist[j] > mylist[j+1]:
#       mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist)
##################### ##########################
##########################################

print("@ line 200 for Selection Sort examples")

# Selection Sort DSA
# example 1

# mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(mylist)
# for i in range(n-1):
#   min_index = i
#   for j in range(i+1, n):
#      if mylist[j] < mylist[min_index]:
#        min_index = j
#   min_value = mylist.pop(min_index)
#   mylist.insert(i, min_value)

# print(mylist)

##################### ##########################
##########################################

print("@ line 221 for Insertion Sort examples")
# Insertion Sort DSA  
# example 1

# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(1,n):
#   insert_index = i
#   current_value = mylist.pop(i)
#   for j in range(i-1, -1, -1):
#     if mylist[j] > current_value:
#       insert_index = j
#   mylist.insert(insert_index, current_value)

# print(mylist)

##################### ##########################
##########################################

print("@ line 241 for Merge Sort examples")
# Merge Sort DSA
# example 1
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1  
#     return arr
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]
# sorted_list = merge_sort(mylist)
# print("Sorted list:", sorted_list)
  

##################### ##########################  
##########################################
print("@ line 281 for Quick Sort examples")
# Quick Sort DSA
# example 1
# def partition(array, low, high):
#   pivot = array[high]
#   i = low - 1

#   for j in range(low, high):
#      if array[j] <= pivot:
#        i += 1
#        array[i], array[j] = array[j], array[i]

#   array[i+1], array[high] = array[high], array[i+1]
#   return i+1

# def quicksort(array, low=0, high=None):
#   if high is None:
#     high = len(array) - 1

#   if low < high:
#     pivot_index = partition(array, low, high)
#     quicksort(array, low, pivot_index-1)
#     quicksort(array, pivot_index+1, high)

# mylist = [64, 34, 25, 5, 22, 11, 90, 12]
# quicksort(mylist)
# print(mylist)

##################### ##########################
##########################################
print("@ line 311 for Counting Sort examples")
# counting Sort DSA
# example 1
# def countingSort(arr):
#   max_val = max(arr)
#   count = [0] * (max_val + 1)

#   while len(arr) > 0:
#     num = arr.pop(0)
#     count[num] += 1

#   for i in range(len(count)):
#     while count[i] > 0:
#       arr.append(i)
#       count[i] -= 1

#   return arr

# mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# mysortedlist = countingSort(mylist)
# print(mysortedlist)

# mylist = [170, 45, 75, 90, 802, 24, 2, 66]
# print("Original array:", mylist)
# radixArray = [[], [], [], [], [], [], [], [], [], []]
# maxVal = max(mylist)
# exp = 1

# while maxVal // exp > 0:

#   while len(mylist) > 0:
#     val = mylist.pop()
#     radixIndex = (val // exp) % 10
#     radixArray[radixIndex].append(val)

#   for bucket in radixArray:
#     while len(bucket) > 0:
#       val = bucket.pop()
#       mylist.append(val)

#   exp *= 10

# print(mylist)