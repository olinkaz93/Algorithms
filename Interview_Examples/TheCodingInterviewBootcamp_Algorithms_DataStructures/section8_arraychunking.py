#given an array and chunk size, divide the array into many subarrays
#where each subarray is of length size

"""
examples:
chunk([1,2,3,4], 2) --> [[1,2], [3,4]]
chunk([1,2,3,4,5], 2) --> [[1,2],[3,4], [5]]
chunk([1,2,3,4,5], 10) --> [[1,2,3,4,5]]

"""

#for this solution no.1 we create the list with one empty list inside,
#this will be indexed accordingly and checked every step
#if the length superceeds the length we will add one more empty subarray
#and update it for the index of current adding subarray

def chunk(array, size):

    print("array to chunk", array)
    print("size of chunked array", size)

    subarrays = [[]]
    current_index_of_subarray = 0
    print(type(subarrays))
    print(subarrays)
    print(len(subarrays))
    print(len(subarrays[current_index_of_subarray]))
    print("subarrays [] ", subarrays[current_index_of_subarray])
   #subarray = [[el, el, el], [el, el, el], [el, el, el], [el]]

    #test = [[3,4],[4,6],[5,7]]
    #print("test", test)
    #print(test[1])

    for el in array:
        if (len(subarrays[current_index_of_subarray]) == size):
            subarrays.append([])
            current_index_of_subarray += 1
        if (len(subarrays[current_index_of_subarray]) < size):
            subarrays[current_index_of_subarray].append(el)

       # print(subarrays)
    print("subarray", subarrays)
    #print("subarray 0 1", subarrays[0][1])
    #print(subarrays[0][0])
    #return result

#2nd approach, we can loop from the indexes of the elements in array
#end filling the temp subarray.
#once the array if the length of the size, we append it to the result array, and clean the subarray for next iteration
#we must also keep the last case when the last element is added and might be not filling fully the subarray

def chunk_version2(array, size):

    result = []
    subarray = []

    #for el in array:
    #    subarray.append(el)
    #    if (len(subarray) == size or ):
    #        result.append(subarray)
    #        subarray == []


    for i in range(0, len(array), 1):
        subarray.append(array[i])
        if (len(subarray) == size or i == len(array) - 1):
            result.append(subarray)
            subarray = []

    return  result

if __name__ == "__main__":

    array = [1, 2, 3, 4, 8, 9, 0]
    size = 2
    chunk(array, size)

    print(chunk_version2(array, size))
