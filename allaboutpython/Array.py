# Function to rotate an array by d elements
# def my_function(arr, d):
#     d = d % len(arr)
#     return arr[d:] + arr[:d]

# arr = [1, 2, 3, 4, 5]
# d = int(input("Enter number of rotations: "))
# print("Array after rotation:", my_function(arr, d))

#################### ##########################
# example 2
# find the matching pair in array

stringList = ["apple", "banana", "orange", "apple", "grape", "banana"]
queries = ["apple", "banana", "kiwi"]

def matchingStrings(stringList, queries):
    #write your code here
    ans = []
    for i in range(len(queries)):
        count = 0
        for j in range(len(stringList)):
            if queries[i] == stringList[j]:
                count += 1
        ans.append(count)

    return ans
        
print(matchingStrings(stringList, queries))