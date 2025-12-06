# Слайд 16 1. Повторить действие N раз

for i in range(5):
    print("Hello")

# Слайд 17 2. Пройти по индексам списка

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")


# слайд 26
numbers1 = list(range(10))
numbers2 = list(range(2, 21, 2))
countdown = list(range(10, 0, -1))
print(numbers1)
print(numbers2)
print(countdown)

# слайд 27
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
for i in range(len(words)):
    if "a" in words[i]:
        words[i] = "FOUND"

print(words)

# слайды 29-30
products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор"]
prices = [50000, 2500, 4000, 30000]
quantities = [8, 45, 25, 12]
total_price = []
for i in range(len(products)):
    price = prices[i] * quantities[i]
    total_price.append(price)
print("Выручка по товарам: ", total_price)
max_revenue = max(total_price)
max_index = total_price.index(max_revenue)
print("Максимальная выручка:", max_revenue)
print("Товар с максимальной выручкой:", products[max_index])


# слайд 31
products = ["Телефон", "Планшет", "Ноутбук", "Наушники"]
prices = [30000, 45000, 80000, 15000]
stock = [15, 8, 5, 20]
discounts = [10, 15, 20, 5]  # Скидки в процентах

for i in range(len(products)):
    prices[i] = prices[i] - (prices[i] * discounts[i] / 100)
    print(f"{products[i]} — новая цена: {prices[i]}, остаток: {stock[i]} штук")


# слайд 35
fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# слайд 40
# способ 1
numbers = [x for x in range(21) if x % 2 == 0]
print(numbers)

# способ 2
numbers = []
for x in range(21):
    if x % 2 == 0:
        numbers.append(x)

print(numbers)

# слайд 41
# способ 1
words = ["python", "data", "science", "list"]
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)

# способ 2
words = ["python", "data", "science", "list"]
lengths = [len(word) for word in words]
print(lengths)

# слайд 42
words = ["cat", "elephant", "dog", "butterfly", "ox"]
long_words = [word for word in words if len(word) > 4]
print(long_words)
