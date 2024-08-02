slovo = str(input("Введите слово  без пробелов - "))
a = slovo[::-1]
if slovo == a:
    print("yes")
else:
    print("no")
