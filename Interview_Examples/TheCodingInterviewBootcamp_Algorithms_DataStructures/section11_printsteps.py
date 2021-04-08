#write a function that accepts a positive number N
#the function should console log a step shape using # character
#make sure the steps has spaces on the right side!

"""examples
steps(2):
'# '
'##'

steps(3:
'#  '
'## '
'###'

steps(4)
'#   '
'##  '
'### '
'####'

"""

def steps(n):

    number_of_lines = n
    lenght_of_lines = n
    line = ""
    for index_of_line in range(0, number_of_lines, 1):

        number_of_hashes = index_of_line+1
        hashes = number_of_hashes*"#"

        line = line + hashes
        while (len(line)<lenght_of_lines):
            line = line + " "
        print(line)
        line = ""

def stepsVersion2(n):

    number_of_lines = n
    lenght_of_lines = n
    line = ""
    for index_of_line in range(0, number_of_lines, 1):

        number_of_hashes = index_of_line+1
        hashes = number_of_hashes*"#"

        number_of_white_spaces = lenght_of_lines - number_of_hashes
        white_spaces = number_of_white_spaces*" "
        line = hashes + white_spaces
        print(line)
        line = ""

if __name__ == "__main__":

    n = 4
    #steps(n)
    stepsVersion2(20)


