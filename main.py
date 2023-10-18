
def blank(name, fname, yearb, kurs, ss):
    try:
        age = 2023 - int(yearb)
    except ValueError:
        print("Вы неправильно ввели год рождения!!!")
        return
    print(f"""
Вы заполнили такие данные:
Вас зовут : {name} {fname}
Вам {age} лет
Ваш ответ к первому вопросу: {kurs}
Ваш ответ к второму вопросу: {ss}""")


if __name__ == '__main__':
    name = input("Введите ваше имя: ")
    fname = input("Введите вашу фамилию: ")
    year = input("Введите ваш год рождения: ")
    kurs = input("Нравится ли вам курс?: ")
    ss = input("Что вы ожидаете от курса: ")
    blank(name, fname, year, kurs, ss)

