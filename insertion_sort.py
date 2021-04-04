# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    #we will start comparing sorted / unsorted elements
    #from the index 1, as [0] element is already nothing on the left of it

    for i in range(1, len(arr)):

        #we take the value which
        #would be compared on every iteration
        value_to_sort = arr[i]

        #condition
        #while value to the left is higher than the current value to be sort
        #item to the left is larger, we must to switch those values
        #also i > 0 - because python allows negative indexes

        #here comapring to the already sorted values
        #to the left, once find the value that is not higher that current one, we can move to another step

        while (arr[i-1] > value_to_sort and i > 0):
            #doing that we compare the arr[i] element and find the proper index in the array
            arr[i], arr[i-1] = arr[i-1], arr[i]

            #to continue comparisation further down to the list,
            #we must to increment the i value

            i = i-1
            #incrementningly stepping back

            #we do a swap on the two values,
            #1)we get the value to be sort
            #2) we comapre it to the value on the left
            #3) if the compared item is larger
            #4)we swap them
            #5) and then we check it with next - left element
            #6) after that all elements on the left of index "i"
            #____|______
    return arr
