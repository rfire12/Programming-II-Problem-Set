'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATOR

The English alphabet contains 26 characters and mobile phones only have ten digits on the keyboard. Several letters are mapped on each number key, as shown in the image below, so that a message can be written with repetitive keystrokes. For example, to insert character B, you must press 22. To enter a sequence of two characters from the same key, the user must pause before pressing the button a second time. For example, 2 2 indicates AA while 22 indicates B (a "space character" is displayed to indicate a pause).

You must create a program that calculates the sequence of keys that you have to press to write a certain message.
'''


def add(word, char, cant):
    count = 0
    while count < cant:
        word += char
        count += 1
    return word


def find(char, list):
    count = 0
    num = 0
    position = 0
    while count < 8:
        if char in list[count]:
            num = count + 2
            position = list[count].index(char) + 1
            count = 10
        count += 1
    if char == ' ':
        num = 0
        position = 1
    return num, position


def find_number(word):
    number = ''
    last_num = 0
    num = 0
    list = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    for char in word:
        num, cant = find(char, list)
        if num == last_num:
            number += ' '
        number = add(number, str(num), cant)
        last_num = num
    return number


print("Ingresa la palabra: ")
word = input()

print("El numero es: %s" % find_number(word))
