from django.db import models
from django.contrib.auth.models import User
from home.models import course
# Create your models here.

from home.models import course 


class student_couser(models.Model):
    # core_subject = models.OneToOneField(course,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.core_subject.product_name
    

class usercourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sub = models.ForeignKey(course,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name+""+ self.sub.product_name
    
class helpquary(models.Model):
    student_name=models.CharField(max_length=500)
    student_email =models.CharField(max_length=300)
    student_message = models.TextField()

    def __str__(self) -> str:
        return self.student_name