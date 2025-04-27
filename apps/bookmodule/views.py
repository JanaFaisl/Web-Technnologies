from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Student, Address, Product
from django.db.models import Q, Count, Avg, Sum, Max, Min
from .models import Department, Course, Student, Student_module, Card, Address, Student2, Address2
from .forms import BookForm,  StudentForm, AddressForm, Student2Form, Address2Form, ProductForm
from django.shortcuts import get_object_or_404

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


def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_book.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('books.list_books')
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('books.list_books')
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.list_books')
    return render(request, 'bookmodule/delete_book.html', {'book': book})

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.list_books_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book.html', {'form': form})




def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.list_books_form')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/edit_book.html', {'form': form})


def t(request):
    return render(request, 'bookmodule/t.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.save()
            return redirect('student_list')
    else:
        student_form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'student_form': student_form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    address = student.address
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        address_form = AddressForm(request.POST, instance=address)
        if address_form.is_valid() and student_form.is_valid():
            address_form.save()
            student_form.save()
            return redirect('student_list')
    else:
        student_form = StudentForm(instance=student)
        address_form = AddressForm(instance=address)
    return render(request, 'bookmodule/add_student.html', {'student_form': student_form, 'address_form': address_form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        student_form = Student2Form(request.POST)
        address_form = Address2Form(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.save()

            # Get selected addresses from checkboxes
            selected_addresses = request.POST.getlist('addresses')
            if selected_addresses:
                student.addresses.add(*Address2.objects.filter(id__in=selected_addresses))

            # Check if a new city was entered
            if address_form.is_valid() and address_form.cleaned_data.get('city'):
                address = address_form.save()
                student.addresses.add(address)

            return redirect('student2_list')

    else:
        student_form = Student2Form()
        address_form = Address2Form()

    addresses = Address2.objects.all()
    return render(request, 'bookmodule/add_student2.html', {
        'student_form': student_form,
        'address_form': address_form,
        'addresses': addresses,
    })



def update_student2(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student_form = Student2Form(request.POST, instance=student)
        address_form = Address2Form(request.POST)
        if student_form.is_valid() and address_form.is_valid():
            # Save the new address
            address = address_form.save()
            # Save the updated student
            student = student_form.save()
            # Remove all existing addresses
            student.addresses.clear()
            # Get selected addresses from the form
            selected_addresses = request.POST.getlist('addresses')
            # Add selected addresses to the student
            student.addresses.add(*Address2.objects.filter(id__in=selected_addresses))
            # Add the new address to the student if it was created
            student.addresses.add(address)  # Many-to-many: add new address
            return redirect('student2_list')
    else:
        student_form = Student2Form(instance=student)
        address_form = Address2Form()

    # Fetch all addresses and pass them to the form
    addresses = Address2.objects.all()
    return render(request, 'bookmodule/add_student2.html', {
        'student_form': student_form,
        'address_form': address_form,
        'addresses': addresses,
    })

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'bookmodule/add_product.html', {'form': form})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'bookmodule/product_list.html', {'products': products})