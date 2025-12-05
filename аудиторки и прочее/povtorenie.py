# Задача 1

password = input('Введите пароль: ')
while len(password) < 8:
    print('Пароль слишком короткий. Попробуйте снова.')
    password = input('Введите пароль: ')
if len(password) >= 8:
    print('Пароль принят!')


# Задача 2

commands = ('start', 'stop', 'pause', 'quit')
while True:
    action = input("Введите команду: ")

    if action not in commands:
        print("Неизвестная команда.")
        continue

    if action == 'quit':
        print("Выход из программы.")
        break

    print(f"Выполняю команду: {action}")


# Задача 3

shopping_list = []
choice = str()

while choice != "Выйти":
    print('Выберите действие: ')
    print("Добавить товар")
    print("Удалить товар")
    print("Показать список")
    print("Выйти")

    choice = input("Ваш выбор: ")

    if choice == "Добавить товар":
        item = input("Введите товар для добавления: ")
        shopping_list.append(item)
        print(f"Товар '{item}' добавлен!")
        
    elif choice == "Удалить товар":
        item = input("Введите товар для удаления: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Товар '{item}' удалён!")
        else:
            print("Такого товара нет в списке.")

    elif choice == "Показать список":
        print("Вот ваш список покупок:")
        print(shopping_list)

    elif choice == "Выйти":
        print("Выход из программы.")

    else:
        print("Неизвестная команда. Выберите другую команду.")

# Задача 4 

email_set = set()
email = input("Введите email: ")
while email != "":
    email_set.add(email)
    email = input("Введите email: ")
addr_list = sorted(email_set)
print(f'Уникальные email-адреса: {addr_list}')

# презентация while, слайд 23

responses = (
    ("hello", "Hi there!"),
    ("how are you", "I'm a program, but thanks for asking!")
)

message = ""

while message != "exit":
    message = input("You: ")

    if message == "exit":
        print("Bot: Goodbye!")
        break

    if message == responses[0][0]:
        print("Bot:", responses[0][1])

    elif message == responses[1][0]:
        print("Bot:", responses[1][1])

    else:
        print("Bot: I don't understand that.")



