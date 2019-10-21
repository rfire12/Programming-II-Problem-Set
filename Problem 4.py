'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATOR

You are a biologist who examines DNA sequences from different life forms. You will be given two DNA sequences, and the goal is to find the ordered set of adjacent larger bases that is common in both DNAs.

The DNA sequences will be given as ordered sets of nucleotide bases: adenine (abbreviated A), cytosine (C), guanine (G) and thymine (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

For the previous example, the result is CTTCCT because that is the ordered set of adjacent larger bases found in both life forms.

'''


def divideWord(adn_1, adn_2, i, j):
    str = ""
    while(adn_1[i] == adn_2[j]):
        str += adn_2[j]
        if(i < len(adn_1)-1):
            i += 1
        if(j < len(adn_2)-1):
            j += 1
    return str


def findCommonSequence(adn_1, adn_2):
    i = 0
    adn_1 += " "  # Esto es por si el ultimo caracter de los Strings son iguales, el programa pueda terminar
    lineCheck = []
    while(i < len(adn_1)):
        j = 0
        k = i
        emptyString = ""
        while(j < len(adn_2)):
            l = j
            if(adn_1[k] == adn_2[j]):
                emptyString = divideWord(adn_1, adn_2, k, l)
            j += 1
            if(emptyString != ""):
                lineCheck.append(emptyString)
        i += 1
    lineCheck.sort(key=len)
    str = lineCheck[len(lineCheck) - 1]
    return str


def main():
    str_adn_1 = str(input("Primera secuencia de ADN: "))
    str_adn_2 = str(input("Segunda secuencia de ADN: "))
    str_adn_1 = str_adn_1.upper()
    str_adn_2 = str_adn_2.upper()
    str_common = findCommonSequence(str_adn_1, str_adn_2)
    print(str_common)


main()
