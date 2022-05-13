from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class Language(models.Model):
    key = models.CharField(max_length=4)
    name = models.CharField(max_length=128)

    def __STR__(self):
        return self.name

class CustomUser(AbstractUser):
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
        ) 
    preferred_language = models.ForeignKey(
            Language,
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            default=None
        )

class Title(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a Title (e.g. Science Fiction)')

    def __str__(self):
        return self.name


from django.urls import reverse 

class Body(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        
        return f'{self.last_name}, {self.first_name}'
