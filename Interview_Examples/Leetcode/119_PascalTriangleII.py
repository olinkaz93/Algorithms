def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]

    else:
        previous_row = [1, 1]

        for row in range(2, rowIndex+1):
            print("row", row)
            # previous_row = [1,1]
            current_row = []
            length_of_row = row
            # [1, 2, 1]
            # [1, 3, 3, 1]

            current_row.append(1)
            for i in range(1, row):
                current_row.append(previous_row[i - 1] + previous_row[i])
            current_row.append(1)
            print("current row", current_row)
            previous_row = current_row

    return current_row

if __name__ == "__main__":
    print(getRow(4))
