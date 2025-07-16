#create 
from bookshelf.models import Book(book = Book.objects.create(title="1984", author="George Orwell publication_year=1949))

output = [Book: 1984]



#retrieve
book = Book.objects.get(title="1984")

book.title
output = [1984]

book.author
output = [George Orwell]

book.publication_year
output = [1949]



#delete
book.title = "Nineteen Eighty-Four"
book.save()

book.title
output = [Nineteen Eighty-Four]



#delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
output = [ QuerySet[] ]