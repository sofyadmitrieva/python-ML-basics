# слайд 8
num_list = [2, 4, 6, 8, 10]

total = 0
for num in num_list:
    total += num

print("Сумма: ", total)

# слайд 9, задача 1

words = ["apple", "banana", "cherry"]

for word in words:
    print(word, "-", len(word))

# слайд 9, задача 2
text = "Python"

for i in range(len(text)):
    print(f"Символ {i+1}: {text[i]}")

# слайд 10, задача 1

numbers = [3, 7, 2, 9, 5]
result = [x * 2 for x in numbers]
print(result)

# слайд 10, задача 2
words = ["cat", "elephant", "dog", "butterfly"]

for w in words:
    if len(w) > 3:
        print(w)


# слайд 10, задача 3
fio = ("Иванов", "Иван", "Иванович")
result = tuple(word.lower() for word in fio)
print(result)
