from django.db import models
from users.models import Semester,Subject,Profile
# Create your models here.
class AssessmentComponent(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Theory Mark", "Practical Mark"
    max_mark = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Assessment(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=20)  # e.g., "MSE 1", "Other Component"

    def __str__(self):
        return f"{self.assessment_type} - {self.subject.name} - {self.student.user.username}"


class Mark(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='marks')
    component = models.ForeignKey(AssessmentComponent, on_delete=models.CASCADE)
    mark_obtained = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.component.name} - {self.mark_obtained}/{self.component.max_mark}"