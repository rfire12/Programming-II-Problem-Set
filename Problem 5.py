'''
TRANSLATED FROM SPANISH TO ENGLISH WITH GOOGLE TRANSLATOR

You are an entrepreneur in Madrid, and you have the brilliant idea of ​​opening a milk store in the Plaza Mayor. As he is a very prudent person, he wants the milk he will sell to be perfectly natural and fresh, and for that reason, he will bring some very healthy cows from the Zaragoza region to Madrid. You have at your disposal a truck with a certain weight limit, and a group of cows available for sale. Each cow can have a different weight, and produce a different amount of milk a day.

Your goal as an entrepreneur is to choose which cows to buy and carry in his truck, so that he can maximize milk production, observing the weight limit of the truck.

Input: Total number of cows in the Zaragoza area that are for sale.

Input: Total weight that the truck can carry.

Input: List of weights of cows.

Input: List of milk production per cow, in liters per day.

Output: Maximum amount of milk production can be obtained.

'''

def get_data():
    print("Ingrese la cantidad de vacas: ")
    num = int(input())
    print("Peso total que soporta el camion: ")
    max_weight = int(input())
    print("Ingrese los pesos de las vacas separados por un espacio")
    cows_weight = input()
    print("Litros de leche por vaca (separados por un espacio)")
    cows_milk = input()
    return cows_weight, cows_milk, max_weight, num


def format_data(weight, milk, num):
    weight = weight.split(" ")
    milk = milk.split(" ")
    cows, count = [], 0
    while count < num:
        cows.append([int(weight[count]), int(milk[count])])
        count += 1
    return cows

def sort_cows(cows):
    num = len(cows)
    cont1, cont2 = 0, 0
    while cont1 < num:
        while cont2 < (num - 1):
            if (cows[cont1][1] / cows[cont1][0]) > (cows[cont2][1] / cows[cont2][0]):
                temp = cows[cont1]
                cows[cont1] = cows[cont2]
                cows[cont2] = temp
            cont2 += 1
        cont1 += 1
        cont2 = 0
    return cows


def replace_cows(truck_cows, cows, max_weight, cows_in_truck_weight):
    for cow in cows:
        cows_truck_num = 0
        cows_truck_len = len(truck_cows)
        if cow not in truck_cows:
            while cows_truck_num < cows_truck_len:
                temp_truck_weight = cows_in_truck_weight - truck_cows[cows_truck_num][0] # Peso del camion sin la vaca que se intenta sacar del mismo
                if (cow[1] >= truck_cows[cows_truck_num][1]) and ((temp_truck_weight + cow[0]) < max_weight): # Si la vaca que se intenta entrar produce mas leche que la que se intenta sacar y el peso no excede el limite
                    truck_cows[cows_truck_num] = cow
                    cows_in_truck_weight = temp_truck_weight + cow[0]
                    return replace_cows(truck_cows, cows, max_weight, cows_in_truck_weight)
                cows_truck_num += 1
    return truck_cows


def max_milk(cows):
    milk = 0
    for cow in cows:
        milk += cow[1]
    return milk


def fill_truck(cows, max_weight):
    cows = sort_cows(cows)
    truck_cows = []
    cows_in_truck_weight = 0
    for cow in cows:
        if (cow[0] + cows_in_truck_weight) <= max_weight:
            truck_cows.append(cow)
            cows_in_truck_weight += cow[0]
    truck_cows = replace_cows(truck_cows, cows, max_weight, cows_in_truck_weight)
    return max_milk(truck_cows)


cows_weight, cows_milk, max_weight, num = get_data()
cows = format_data(cows_weight, cows_milk, num)
print("\nLa cantidad maxima de lecha es: %d" % fill_truck(cows, max_weight))

