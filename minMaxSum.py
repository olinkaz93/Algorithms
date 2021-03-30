
list = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    minimum_element = min(arr)
    maximum_element = max(arr)
    sum = 0

    for el in arr:
        sum = sum + el

    maximum_sum = sum - minimum_element
    minimum_sum = sum - maximum_element
    result = [maximum_sum, minimum_sum]

    return maximum_sum, minimum_sum

max = miniMaxSum(list)
print(max)