'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATE


When a king abdicates, his firstborn inherits the throne and must receive, in his coronation, a number that will identify him for posterity. Numbering is important because, otherwise, it would be difficult to differentiate kings with the same name of the same dynasty by also sharing last name. The result is that, before the abdication of a king, it is time to review the history books to find out their number. Are you able to do it?

Input

The program will receive, by standard input, multiple test cases. Each consists of a first line with a number indicating the number of kings of a particular dynasty. Then, on another line, will come the names of all their kings separated by space.

Then two more lines will appear, one with the number of future successors to be numbered (at least one), and another with their names separated by space. Then two more lines will appear, one with the number of future successors to be numbered (at least one), and another with their names separated by space.

All names will be composed of a single word of no more than 20 letters of the English alphabet, and will be case sensitive. In addition, it is guaranteed that in each test case there will be no more than 20 names of different kings.

The entry ends with a test case without potitos.

Output

For each successor of each test case, an independent line will be indicated, the number that will correspond. Although Roman numerals are normally used, for simplicity the number will be indicated in traditional Arabic notation. After each test case, a blank line will be written.

'''


def get_data():
    print("Ingrese la cantidad de reyes: ")
    num_kings = int(input())
    print("Escriba los nombre de los reyes: ")
    kings = input()
    print("Ingrese la cantidad de sucesores: ")
    num_successors = int(input())
    print("Ingrese los nombres de los sucesores: ")
    successors = input()
    print("")
    return kings.split(' ')[:num_kings], successors.split(' ')[:num_successors]


def kings_quantity(kings_list):
    kings = {}
    for element in kings_list:
        if element not in kings:
            kings[element] = 0
        kings[element] += 1
    return kings


def numbering():
    kings_list, successors_list = get_data()
    kings = kings_quantity(kings_list)
    successors_numbered = []
    for element in successors_list:
        if element not in kings:  # If the key doesn't exist, then create the key
            kings[element] = 0
        kings[element] += 1
        successors_numbered.append("%s %d" % (element, kings[element]))
    return successors_numbered


print(*numbering(), sep='\n')
