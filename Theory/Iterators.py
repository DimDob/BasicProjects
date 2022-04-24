from copy import copy, deepcopy

vals = iter([100, 'A', [1,2]]) #Аргументи на обектът - итератор се явява итерируем обект(лист). Итератор е, защото листът е подаден като аргумент на функция iter().
print(vals) #Ако принтираме референцията към обекта тип итератор, ние получаваме мястото на итератора в паметта

try:
    print(f"Първо: {next(vals)}")
    print(f"Второ: {next(vals)}")
    print(f"Трето: {next(vals)}")
    print(f"Четвърто: {next(vals)}")

except StopIteration:
    print("Няма повече стойности")

#Итераторът се обхожда само веднъж. Той е еднократен, с други думи. Ако трябва да го обхождаме пак, ще трябва да създадем копие.
try:
    print(f"Първо: {next(vals)}")
    print(f"Второ: {next(vals)}")
    print(f"Трето: {next(vals)}")
    print(f"Четвърто: {next(vals)}")

except StopIteration:
    print("Няма повече стойности")