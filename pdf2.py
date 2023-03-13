login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == "user" and password == "qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")


amount = float(input("Введите сумму в тенге: "))
currency = input("Выберите валюту для перевода (USD/EUR/RUB): ")

if currency == "USD":
    converted_amount = amount / 420
    print(f"Сумма в USD: {converted_amount:.2f}")
elif currency == "EUR":
    converted_amount = amount / 510
    print(f"Сумма в EUR: {converted_amount:.2f}")
elif currency == "RUB":
    converted_amount = amount / 5.8
    print(f"Сумма в RUB: {converted_amount:.2f}")
else:
    print("Неверно выбрана валюта для перевода.")