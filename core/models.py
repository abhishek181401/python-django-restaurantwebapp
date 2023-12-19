from django.db import models

# Create your models here.
class Owner(models.Model):
    location= models.CharField(max_length=200)
    restaurantname = models.CharField(max_length=255)

    def __str__(self):
        return self.restaurantname

    class Meta:
        verbose_name_plural = "Owner"



class ContactNumber(models.Model):
    number = models.CharField(max_length=15)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class TeamMember(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='team_member_pics/',null=True,blank=True)
    position = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    momo_choices =(
        ('Buff','Buff'),
        ('Chicken','Chicken'),
        ('Veg','Veg')
    )
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200,null=True,blank=True)
    price = models.IntegerField()
    type = models.CharField(max_length=50,choices=momo_choices)
    is_deleted = models.BooleanField(default=False)
    momo_picture = models.ImageField(upload_to='recipe_pics/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __self__(self):
        return self.name


class UserQuery(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'UserQueries'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

