from django.db import models
from users.models import Courses,Semester
# Create your models here.

MSE_NUMBERING= (
    (1,"MSE-1"),
    (2,"MSE-2"),
    (3,"MSE-3"),
    (4,"MSE-4"),
)
class mseResult(models.Model):
    mse_number= models.IntegerField(choices=MSE_NUMBERING)
    course= models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester= models.ForeignKey(Semester, on_delete=models.CASCADE)
    result_day= models.DateTimeField()

    #class Meta:
    #    unique_together= ['mse_number','course','semester']

    def __str__(self):
        return f" {self.course}- {self.semester}- {self.mse_number}"
    

