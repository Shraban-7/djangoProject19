from django.db import models

# Create your models here.
class Post(models.Model):
    TEN = '10'
    NINE = '9'
    EIGHT = '8'
    SEVEN = '7'
    SIX = '6'
    FIVE = '5'
    FOUR = '4'
    THREE = '3'
    TWO = '2'
    ONE = '1'
    year_in_scholl_choice = [(TEN , '10'),
                             (NINE ,'9'),
                             (EIGHT , '8'),
                             (SEVEN , '7'),
                             (SIX , '6'),
                             (FIVE , '5'),
                             (FOUR,'4'),
                             (THREE, '3'),
                             (TWO,'2'),
                             (ONE, '1'),
                             ]
    medium_choice = (('English','English'),
                     ('Bangla','Bangla'))
    title = models.CharField(max_length=255)
    content = models.TextField()
    class_school = models.CharField(max_length=2,choices=year_in_scholl_choice,default=ONE)
    medium = models.CharField(max_length=50,choices=medium_choice,default='Bangla')
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    location = models.CharField(max_length=250,default='Dhaka')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title