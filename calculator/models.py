from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    # options=(
    #     ('wireframes','wireframes'),
    #     ('frontend','frontend'),
    #     ('backend','backend'),
    #     ('frameworks','frameworks'),
    #     ('database','database'),
    #     ('cloud','cloud'),
    #     ('hosting','hosting'),
    #     ('Extra','Extra')
    # )
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname 

class Technology(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    def __str__(self):
        return str(self.name)

class AddTech(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return str(self.price)
