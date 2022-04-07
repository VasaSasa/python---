
#TASK01
#numbers = []
#while True:
#    number = int(input('Enter number:'))
#    numbers.append(number)
#    if len(numbers) == 3:
#        break

#print(sum(numbers))

#TASK02
#numbers = []
#while True:
#    number = input('Enter number: ')
#    numbers.append(number)
#    if len(numbers) == 3:
#        break


#string01 = ""
#for i in numbers:
#    string01 = string01 + i

#print(string01)

#TASK03

#string_number = input("Enter number: ")
#integer_number = [int(i) for i in str(string_number)]

#numbers = integer_number
#product_num = 1
#for i in numbers:
    #product_num = product_num * i

#print(product_num)

string_cislo = input("Zadej číslo: ")

integer_cislo_seznam = []
for i in string_cislo:
  integer_cislo_seznam.append(i)

print(integer_cislo_seznam)

seznam_cisel = list(map(int,integer_cislo_seznam))

print(seznam_cisel)


soucin_cisel = 1
for i in seznam_cisel:
  soucin_cisel *= i

print(soucin_cisel)

