#define function that merges two sorted list and returns the merged sorted list
#we know that our lists are sorted
#we should check weather they are list itself
#we should check if some of the list is not empty -> in that case we can return the other list

#e.g. having list1 [0, 1, 5], list2 [0, 3, 9, 10]

#we want to get one, merged, sorted list e.g. sorted_list = [], which is gonna be empty for the initial state
#we should check if the lists are not empty, and if one of those is empty, we return as the result the other list

#we should track indexes of each element in two given lists, and having those, we can compare the values at those indexes,
#and checking weather element_list1 <= element_list2 , we can append those lower value to the sorted_list - which we want to return
#after every check depending which value is lower/higher we will update the index of the concurrent list,

#we should implement while loop, which will proceed as long as we do not exceed of the lenghth of the list,
#when the while loop stops, we need to add to the end of the result the rest of other list, which elements are still about to be appended


def merge_sorted_lists(list1, list2):

    if (type(list1)!=list or type(list2)!=list):
        return "Wrong input!"

    #having one of the lists which is empty
    if (list1 == []):
        return list2
    if (list2 == []):
        return list1

    #having both lists which are not empty
    merged_list = []

    current_el_list1_index = 0
    current_el_list2_index = 0

    while current_el_list1_index < len(list1) and current_el_list2_index < len(list2):
        if list1[current_el_list1_index] <= list2[current_el_list2_index]:
            merged_list.append(list1[current_el_list1_index])
            current_el_list1_index+=1
        elif list1[current_el_list1_index] > list2[current_el_list2_index]:
            merged_list.append(list2[current_el_list2_index])
            current_el_list2_index+=1

    result = merged_list + list1[current_el_list1_index:] + list2[current_el_list2_index:]

    return result


sample_list1 = []
sample_list2 = [1, 2]
result = merge_sorted_lists(sample_list1, sample_list2)
print(result)

#time complexity of the merging function
#big O = (n + m)