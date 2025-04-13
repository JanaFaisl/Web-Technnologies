from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Student, Address
from django.db.models import Q, Count, Avg, Sum, Max, Min
from .models import Department, Course, Student, Student_module, Card

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

def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte = 80))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task2(request):
    mybooks = Book.objects.filter(Q(edition__gte = 3) & ( Q(author__icontains = 'co') | Q(title__icontains = 'co') )  )
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task3(request):
    mybooks = Book.objects.filter(Q(edition__lte = 3) & ( ~Q(author__contains = 'co') | ~Q(title__contains = 'co') )  )
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/status.html', {'stats': stats})



def lab8_task7(request):
    city_stats = Student.objects.values('address__city').annotate(total=Count('id')) 
    return render(request, 'bookmodule/studentNum.html', {'city_stats': city_stats})



def task1(request):
    departments = Department.objects.annotate(student_count=Count('student_module'))
    return render(request, 'bookmodule/task1.html', {'departments': departments})

def task2(request):
    courses = Course.objects.annotate(student_count=Count('student_module'))
    return render(request, 'bookmodule/task2.html', {'courses': courses})

def task3(request):
    departments = Department.objects.annotate(oldest_id=Min('id'))
    return render(request, 'bookmodule/task3.html', {'oldest_students': departments})

def task4(request):
    departments = Department.objects.annotate(student_count=Count('student_module')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/task4.html', {'departments': departments})
