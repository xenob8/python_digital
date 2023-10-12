numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

avg = sum(x for x in numbers if x is not None) / len(numbers)
#Suppoce in common case we dont know pos of None element
index = numbers.index(None)
numbers[index] = avg

print("Измененный список:", numbers)
