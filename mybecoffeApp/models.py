

from django.contrib.auth.models import AbstractUser


from django.db import models

# Create your models here.
class users(AbstractUser):
   
    chef=models.BooleanField(default=False)
    




class presence(models.Model):
    
    date=models.DateField(null=False)
    arrival_time=models.TimeField(null=False)
    depart_time=models.TimeField(blank=True,null=True)
    user_id=models.ForeignKey(users,on_delete=models.CASCADE)

    class Meta:
        unique_together=('date','user_id')
    


    
    def __str__(self):
        return f"{self.id} {self.user_id} {self.date} {self.arrival_time} {self.depart_time} "





    
    
    


class recettes(models.Model):
    date=models.DateField(null=False,unique=True)
    recette=models.CharField(null=False,max_length=100)
    user_id=models.ForeignKey(users,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user_id} {self.recette} {self.date}"