import numpy

def binary_to_int(x):
    
    x_int = 0;
    for i in range(len(x)):
        x_int += x[i]*(2**i);

    return x_int;

#sort an input list using quicksort; returns both sorted list and corresponding indexes
#input list must be formed by binary lists
def efficient_binary_sorting(input_list):

    #convert binary strings to integers
    int_list = [];
    for a in input_list:
        int_list.append(binary_to_int(a));

    #sort list
    indexes = numpy.argsort(int_list);

    sorted_int_list = [];
    sorted_bin_list = [];

    for i in indexes:
        sorted_int_list.append(int_list[i]);
        sorted_bin_list.append(input_list[i]);


    return indexes, sorted_bin_list, sorted_int_list;


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
def dicotomic_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return dicotomic_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return dicotomic_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


def hello_world():

    print("ciao");

    return 0;

