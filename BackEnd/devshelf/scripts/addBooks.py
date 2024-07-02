from library.models import Book
import csv

def run():
    with open('/home/sihari/Desktop/BTech/DevShelf_TeamMeow/datasetnew2.csv') as file:
        reader = csv.reader(file)
        next(reader)
        #Book.objects().all().delete()
        for row in reader:
            print(row)
            book = Book()
            book.title = row[0]
            book.description = row[1]
            book.author = row[2]
            book.genre = row[3]
            book.department = row[4]
            book.count = row[5]
            book.vendor = row[6]
            book.vendor_id = row[7]
            book.publisher = row[8]
            book.publisher_id = row[9]

            book.save()






