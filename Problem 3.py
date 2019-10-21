'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATOR

An integer is said to be a palindrome if it is equal to the number obtained by reversing the order of its figures. For example, 79197 and 324423 are palindromes. In this task you will be given an integer N, 1 <= N <= 1,000,000. You must find the smallest integer M such that M <= N that is prime and M is a palindrome N. For example, if N is 31, then the answer is 101.

Input format: A single integer N, (1 <= N <= 1,000,000), on a single line.

Output format: Your output must consist of a single integer, the smallest palindrome cousin greater than or equal to N.

'''


import math


def palindrome(num):
    number = num[::-1]  # Voltear el numero
    return num.find(number)  # Si lo encuentra retornara 1 sino -1


def is_prime(num):
    end = math.sqrt(num)
    count, prime = 2, True
    while count < end:
        if (num % count) == 0:
            prime = False
            count = end       # Terminar ciclo
        count += 1
    return prime


def find_number(number):
    num = int(number)
    number_found = 0
    while number_found == 0:
        if palindrome(str(num)) == 0 and is_prime(num):
            number_found = num
        num += 1
    return number_found


print("Ingrese el numero: ")
number = input()
print("El resultado es: %d" % find_number(number))
