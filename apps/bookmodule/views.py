from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index2(request, val1 = 0): 
    try:
        return HttpResponse("value1 = "+str(val1))
    except ValueError:
        return HttpResponse("Error, expected val1 to be integer")
 
def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    books = Book.objects.filter(price = 100)
    return render(request, 'bookmodule/booklist.html', {'books': books})



def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/one_book.html', context)

def links_page(request):
    return render(request, 'bookmodule/links.html')


def text_formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')
    apps/templates/bookmodule/ listing.html

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        filtered_books = []

        mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
        mybook.save()

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                filtered_books.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    print(mybooks) 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
