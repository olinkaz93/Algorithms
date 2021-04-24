"""
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.
You need to help them find out their
common interest with the least list index sum.
If there is a choice tie between answers,
output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 3:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:
Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]

"""


def findRestaurant(list1, list2):

    if len(list1) == 0 or len(list2) == 0:
        return []
    if len(list1) == 1 and len(list2) == 1 and list1[0] == list2[0]:
        return list1[0]

    """if len(list1) < len(list2):
        shorter_list = list1
        longer_list = list2
    else:
        shorter_list = list2
        longer_list = list1

    # for index, el in enumerate(list1):
    #    print(el, "at index", index)"""

    dictionary_list1 = {}
    #dictionary_list2 = {}
    shortest_index_sum = float('inf')
    result = []

    for index, el in enumerate(list1):
        if el not in dictionary_list1:
            dictionary_list1[el] = index

    """
    for index, el in enumerate(list2):
        if el not in dictionary_list2:
            dictionary_list2[el] = index
    

    for key in dictionary_list1.keys():
        if key in dictionary_list2:
            common_restaurant = key
            distance = dictionary_list1[key] + dictionary_list2[key]
            if distance < shortest_index_sum:
                shortest_index_sum = distance
                result = []
                result.append(key)
                #shortest_index_sum = distance
            elif distance == shortest_index_sum:
                result.append(key)
    """

    for index in range(0, len(list2), 1):
        key = list2[index]
        if key in dictionary_list1:
            distance = dictionary_list1[key] + index
            if distance < shortest_index_sum:
                shortest_index_sum = distance
                result = []
                result.append(key)
            elif distance == shortest_index_sum:
                result.append(key)
    return result


if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    list3 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list4 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]


    print(findRestaurant(list1, list2))
    print(findRestaurant(list3, list4))