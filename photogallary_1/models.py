from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    cat_name = models.CharField(null = False,max_length=50, blank=False )

    def __str__(self):
        return self.cat_name


class Photo(models.Model):
    profile = models.ForeignKey(Profile,null = True ,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True,blank=True)
    image = models.ImageField( null = False,blank=False)
    description = models.CharField(null = True,max_length=50)


    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)  # Call the "real" save() method.
            
    def __str__(self):
        return self.description



#blank for form 
#null for database 