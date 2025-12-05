# слайд 19
# 1
n = 0
while n < 5:
    n += 1
print(n)

# 2
word = input()
while not word == "стоп":
    print(list(word))
    word = input()


# слайд 21

correct_password = "secret123"
logged_in = False
attempts = 0
max_attempts = 3

while logged_in == False and attempts < max_attempts:
    password = input("Введите пароль: ")
    if password == correct_password:
        logged_in = True
        print("Вход выполнен.")
    else:
        attempts += 1
        print(f"Кол-во попыток: {attempts}")
if attempts >= max_attempts and not logged_in:
    print("Не осталось попыток.")
