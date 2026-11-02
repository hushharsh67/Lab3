print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # REQ-04: no numbers entered
    if len(arr) == 0:
        return 0

    # REQ-05: any value that is not an integer
    for value in arr:
        if not isinstance(value, int):
            return 2

    # REQ-03: 10 or more numbers
    if len(arr) >= 10:
        return 1

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # Invalid sorting order returns an empty list
    if sorting_order != SORT_ASCENDING and sorting_order != SORT_DESCENDING:
        return []

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)