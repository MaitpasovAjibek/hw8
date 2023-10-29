import sqlite3

conn = sqlite3.connect("hw1.db")
cur = conn.cursor()

cur.execute("SELECT id, title FROM cites")
cites = cur.fetchall()
print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
for city in cites:
    print(f"{city[0]}. {city[1]}")

while True:

    city_id = int(input("Введите id города: "))
    if city_id == 0:
        break
    else:

        cur.execute(f"SELECT employees.first_name, employees.last_name, countries.title, cites.title, cites.area FROM employees JOIN cites ON employees.city_id = cites.id JOIN countries ON cites.country_id = countries.id WHERE cites.id = {city_id}")
        employees = cur.fetchall()
        if len(employees) == 0:
            print("В данном городе нет сотрудников")
        else:

            print("Имя      Фамилия      Страна     Город  Площадь-города")
            for employee in employees:
                print(f"{employee[0]}\t{employee[1]}\t{employee[2]}\t{employee[3]}\t{employee[4]}")


cur.close()
conn.close()
