# name = input('введите ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# if name == "Denis":
#     print('Здраствуйте, преподователь')
# else:
#     print('привет', name)
number = int(input("Введите число: ")) #fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
if number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print("Число не подходит")
