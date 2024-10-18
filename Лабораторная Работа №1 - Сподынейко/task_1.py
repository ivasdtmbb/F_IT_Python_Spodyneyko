numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missed_position = numbers.index(None)
# Save an original list's length
original_length = len(numbers)
# remove a None element from the list
numbers.pop(missed_position)
mean_value = (sum(numbers)) / original_length
numbers.insert(missed_position, mean_value)

print("Измененный список:", numbers)

