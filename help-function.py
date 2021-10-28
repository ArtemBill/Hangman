edibles = ["отбивные", "яйца", "пельмени", "орехи"]

for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени!")
        continue
    print("Отлично, вкусные " + food)
else:
    print("Хорошо, что не было пельменей!")
print("Ужин окончен.")
