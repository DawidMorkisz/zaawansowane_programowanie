from datetime import date
import zad_1 as z1
import zad_2 as z2
import zad_3 as z3


student_1 = z1.Student("Jan", [50, 80, 40])
student_2 = z1.Student("Jan", [20, 40, 60])

print(student_1.is_passed())
print(student_2.is_passed())

# Zad 2

library1 = z2.Library("Warsaw", "Rumiankowa 6", "00-001", "9:00-17:00", "123-456-789")
library2 = z2.Library("Krakow", "Warszawska 5", "30-002", "10:00-18:00", "987-654-321")

book1 = z2.Book(library1, date(2021, 5, 10), "Adam", "Mickiewicz", 300)
book2 = z2.Book(library1, date(2019, 7, 20), "Henryk", "Sienkiewicz", 500)
book3 = z2.Book(library2, date(2020, 3, 15), "Juliusz", "Słowacki", 250)
book4 = z2.Book(library2, date(2018, 11, 5), "Bolesław", "Prus", 400)
book5 = z2.Book(library1, date(2022, 1, 25), "Wisława", "Szymborska", 150)

employee1 = z2.Employee("Jan", "Kowalski", date(2020, 1, 10), date(1990, 5, 20), "Warsaw", "Rumiankowa 6")
employee2 = z2.Employee("Anna", "Nowak", date(2019, 2, 15), date(1985, 8, 12), "Krakow", "Warszawska 5")
employee3 = z2.Employee("Piotr", "Wiśniewski", date(2021, 6, 1), date(1992, 11, 30), "Gdańsk", "Morska 12")

order1 = z2.Order(employee1, [book1, book3, book5], date.today())
order2 = z2.Order(employee2, [book2, book4], date.today())

print(f"{order1}\n\n{order2}")

# Zad 3

house = z3.House(area=120, rooms=5, price=500000, address="Warsaw, Kopernika 8", plot=300)

flat = z3.Flat(area=60, rooms=3, price=300000, address="Krakow, Warszawska 12", floor=2)

print(f'{house}\n\n{flat}')