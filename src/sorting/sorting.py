# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [] # changed this to a blank array from 0 * elements i didnt like that

    # Your code here
    while True:      
        if arrA[0] < arrB[0]:
            print("ArrayA has smaller")
            print(arrA[0])
            merged_arr.append(arrA.pop(0))
        else:
            print("ArrayB has smaller")
            print(arrB[0])
            merged_arr.append(arrB.pop(0))

        # check if one is empty, if one is empty then append rest of whatever one and exit loop
        if len(arrA) == 0:
            for x in arrB:
                merged_arr.append(x)
            break
        if len(arrB) == 0:
            for x in arrA:
                merged_arr.append(x)
            break

            
    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) == 1:
        return arr

    # divide into many smaller arrays
    arrA = arr[:round(len(arr)/2)]
    arrB = arr[round(len(arr)/2):]

    # run recursion on new smaller arrays
    arr1 = merge_sort(arrA)
    arr2 = merge_sort(arrB)

    # combine
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    arr = merge(arr1, arr2)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

