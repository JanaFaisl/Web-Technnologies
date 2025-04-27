from django import forms
from .models import Book, Student, Address, Address2, Student2, Product


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.all()
        self.fields['address'].label_from_instance = lambda obj: obj.city

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(Student2Form, self).__init__(*args, **kwargs)
        self.fields['addresses'].required = False  # allow addresses to be empty

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']