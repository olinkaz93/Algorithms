#bubble sort algorithm
#we loop from the beginning to the end of the array,
#multiple times once the output is sorted

def bubble_sort(items):

    input = items
    if (len(input) == 1):
        return "only one element in the list"
    # we need to loop i - times, so the outer loop is just to say how many times we need to loop
    for i in range(0, len(input), 1):
        #we need to loop j, times to compare the pairs of elelemnts, since we need to access the last element and keep it save so len(list)-1
        for j in range(0, len(input)-1, 1):

            if(items[j]>items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]

    return items

if __name__ == "__main__":
    print(bubble_sort([3,6,0,80,100,-1]))


