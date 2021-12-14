print('Простые числа')

# Программа считает количество простых чисел
# в заданной последовательности
# и выводит ответ на экран.

how_long = int(input('Сколько чисел в последовательности? '))

numbers = []
numbers_prime = 0

for i in range(how_long):
  numbers.append(int(input('Введите число: ')))
  counter = 0
  for j in range(2, numbers[i]):
    if (numbers[i]) % j == 0:
      counter += 1
  if counter == 0:
    numbers_prime += 1

print('Количество простых чисел:', numbers_prime)
