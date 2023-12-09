from django.db import models

class Managers(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    service = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'managers'
        app_label = 'bd'


class Orders(models.Model):
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='productid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    statusid = models.ForeignKey('Statuses', models.DO_NOTHING, db_column='statusid')
    managerid = models.ForeignKey(Managers, models.DO_NOTHING, db_column='managerid', blank=True, null=True)
    datecreated = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
        app_label = 'bd'


class Products(models.Model):
    productname = models.CharField(max_length=100)
    companyid = models.ForeignKey('Companies', models.DO_NOTHING, db_column='companyid')
    abouproduct = models.CharField(max_length=1000)
    price = models.TextField()  # This field type is a guess.
    instock = models.BooleanField()
    quantityid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='quantityid')

    class Meta:
        managed = False
        db_table = 'products'
        app_label = 'bd'
        ordering = ['id']


class Statuses(models.Model):
    status = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuses'
        app_label = 'bd'

class Companies(models.Model):
    company = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'companies'
        app_label = 'bd'

    def __str__(self):
        return self.company

class Stock(models.Model):
    model = models.CharField(max_length=20)
    quantity = models.IntegerField()
    nextdeliverydate = models.DateField()

    def __str__(self):
        return self.quantity

    class Meta:
        managed = False
        db_table = 'stock'
        app_label = 'bd'

class Users(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'bd'