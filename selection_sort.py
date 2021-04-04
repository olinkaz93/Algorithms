def selection_sort(input):

    lenght_of_list = len(input)
    for i in range(0, lenght_of_list, 1):
        minimum_element = input[i]
        current_min_index = i
        for j in range(i+1, lenght_of_list, 1):
            if input[j]<minimum_element:
                minimum_element = input[j]
                current_min_index = j

        if current_min_index != i:
            input[i], input[current_min_index] = input[current_min_index], input[i]

    return input

if __name__ == "__main__":

    print(selection_sort([0, -5, 22, 70, -55]))