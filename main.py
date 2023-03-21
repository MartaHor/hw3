import datetime

class Book():

    def __init__(self, name, author, year, year_now=datetime.datetime.now()):
        self.name = name
        self.author = author
        self.year = datetime.datetime(year=year, month=1, day=1)
        self.year_now = datetime.datetime.now()

    def calculation_year(self):
        self.calculation_year = self.year_now - self.year
        print(f'Days book - {self.calculation_year}')

    def get_into(self):
        return f'Names book - {self.name}\n' \
               f'Authors book - {self.author}\n' \
               f'The book was writen - {self.year}\n'


book = Book('It', 'Stephen King', 1986)

print(book.get_into())
print(book.calculation_year())

