class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Address: {self.city} {self.street} {self.zip_code}\n"
                f"Phone: {self.phone}\n"
                f"Open hours: {self.open_hours}\n")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}\n"
                f"Hired: {self.hire_date}\n"
                f"Birth date: {self.birth_date}\n"
                f"Address: {self.street}, {self.city}\n")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by: {self.author_name} {self.author_surname}\n"
                f"Published: {self.publication_date}\n"
                f"Pages: {self.number_of_pages}\n  {self.library}\n")


class Order:
    def __init__(self, employee, books, order_date):
        self.employee = employee
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = "\n".join(str(book) for book in self.books)
        return (f"Order Date: {self.order_date}\n"
                f"Processed by:\n {self.employee}\n"
                f"Books:\n  {books_info}\n")


