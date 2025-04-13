from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, verbose_name='Address', on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    edition = models.IntegerField()



class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return str(self.card_number)

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.title

class Student_module(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
