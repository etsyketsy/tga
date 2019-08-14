from django.db import models

class Artist(models.Model):
    name = models.CharField(
        verbose_name='Artist Name',
        max_length=150,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name
    
    @property
    def known_balance(self):
        # calculate known balance based on logged expenses/incomes
        return 'hello'


class Album(models.Model):
    name = models.CharField(
        verbose_name='Album Name', 
        max_length=150,
        blank=False,
        null=False
    )
    artist = models.ManyToManyField('Artist')
    release_number = models.IntegerField(
        verbose_name='Release Number',
        unique=True
    )
    release_date = models.DateField(
        verbose_name='Release Date',
        blank=True,
        null=True
    )

    class Meta:
        order_with_respect_to = 'release_number'

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(
        verbose_name='Vendor',
        max_length=150,
        blank=True,
        null=True,
    )   

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(
        verbose_name='Source',
        max_length=150,
        blank=True,
        null=True,
    )  

    def __str__(self):
        return self.name

class Income(models.Model):
    name = models.CharField(
        verbose_name='Income',
        max_length=150,
        blank=True,
        null=True,
    )  
    
    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(
        verbose_name='Expense',
        max_length=150,
        blank=True,
        null=True,
    )  
    
    def __str__(self):
        return self.name


class IncomeType(models.Model):
    DIGITAL = 'Digital'
    PHYSICAL = 'Physical'
    OTHER = 'Other'
    INCOME_TYPE_CHOICES = (
            (DIGITAL, DIGITAL),
            (PHYSICAL, PHYSICAL),
            (OTHER, OTHER),
        )
    name = models.Charfield(
        verbose_name='Income Type',
        max_length=150,
        choices=INCOME_TYPE_CHOICES,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.name