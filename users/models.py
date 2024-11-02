from django.db import models
from django.contrib.auth.models import User

from django.core.validators import validate_image_file_extension
from django.core.exceptions import ValidationError


class Division(models.Model):
    name= models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Subject(models.Model):
    name= models.CharField(max_length=100)
    code= models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name

TOTAL_SEMESTERS= (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10)
)
class Semester(models.Model):
    semester_number= models.IntegerField(choices=TOTAL_SEMESTERS)
    start_date= models.DateField()
    subjects= models.ManyToManyField(Subject)
    

    def __str__(self):
        return str(self.semester_number)
    

class Courses(models.Model):
    name= models.CharField(max_length=100)
    fee= models.DecimalField(max_digits=10, decimal_places=2)
    duration= models.IntegerField()
    session_start_year= models.IntegerField(blank=True)
    divisions= models.ManyToManyField(Division)
    semesters= models.ManyToManyField(Semester)

    @property
    def session_till_year(self):
        return self.session_start_year+ self.duration

    def __str__(self):
        return self.name
    
    class Meta:
        pass
        # Ensures that the combination of 'division' and 'name' is unique across the table
        #unique_together = ["divisions", "name"]

    

#profiles = Profile.objects.filter(course_id=course_id, current_semester=semester, division=division)

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='Profile-Image', validators=[validate_image_file_extension], blank=True, null=True)
    
    course=  models.ForeignKey(Courses, on_delete=models.CASCADE, null=True,blank=True)
    current_semester= models.IntegerField(blank=True, null=True)
    usn=  models.CharField(max_length=15, null=True,blank=True)
    roll_number= models.CharField(max_length=15, null=True,blank=True)
    #division= models.ForeignKey(Division, on_delete=models.CASCADE)
    #division = models.CharField(max_length=1, choices=[('A', 'Section A'), ('B', 'Section B')], blank=True, null=True)
    

    def get_current_semester_choices(self):
        if self.course:
            return [(i, f"Semester {i}") for i in range(1, self.course.total_semesters + 1)]
        return []

    def __str__(self):
        return str(self.user)
    
    def clean(self):
        # Ensure user phone number is not the same as father's phone number
        if hasattr(self, 'contactinformationprofile') and hasattr(self, 'parentprofile'):
            if self.contactinformationprofile.student_mobile_number == self.parentprofile.fathers_mobile_number:
                raise ValidationError("User phone number cannot be the same as father's phone number.")


STATE_CHOICES = ((1,"Andhra Pradesh"),(2,"Arunachal Pradesh "),(3,"Assam"),
                 (4,"Bihar"),(5,"Chhattisgarh"),(6,"Goa"),(7,"Gujarat"),
                 (8,"Haryana"),(9,"Himachal Pradesh"),(10,"Jammu and Kashmir "),
                 (11,"Jharkhand"),(12,"Karnataka"),(13,"Kerala"),(14,"Madhya Pradesh"),
                 (15,"Maharashtra"),(16,"Manipur"),(17,"Meghalaya"),(18,"Mizoram"),
                 (19,"Nagaland"),(20,"Odisha"),(21,"Punjab"),(22,"Rajasthan"),
                 (23,"Sikkim"),(24,"Tamil Nadu"),(25,"Telangana"),(26,"Tripura"),
                 (27,"Uttar Pradesh"),(28,"Uttarakhand"),(29,"West Bengal"),
                 (30,"Andaman and Nicobar Islands"),(31,"Chandigarh"),
                 (31,"Dadra and Nagar Haveli"),(32,"Daman and Diu"),(33,"Lakshadweep"),
                 (34,"National Capital Territory of Delhi"),(35,"Puducherry"))

class PersonalProfile(models.Model):
    profile= models.OneToOneField(Profile, on_delete=models.CASCADE)
    title= models.IntegerField(choices= ( (1,'Mr'), (2,'Ms'),(3,'Mrs'), (4,'Miss'), (5,'Dr')  ))
    mobile_number= models.CharField(max_length=10, unique=True)
    gender= models.IntegerField(choices= ( (1,'Male'), (2,'Female')   ))
    """
    category= models.IntegerField(choices= ( (1,'1G'), (2,'2A'), (3,'2B'), (4,'3A'), 
                                              (5,'3B'), (6,'GM'), (7,'OPEN'), (8, 'SC'),
                                                (9, 'ST') )
    """
    #region= models.IntegerField(choices=( (1,'Rural'), (2,'Urban') ))
    aadhar_card_number= models.CharField(max_length=12,unique=True, blank=True, null=True)
    pan_number= models.CharField(max_length=10, unique=True, blank=True, null=True)
    differently_abled= models.BooleanField(default=False)

    dob= models.DateField()
    caste= models.IntegerField(choices= ( (1,'Hindu'), (2,'Muslim'), (3,'Christian')), blank=True, null=True)
    state= models.IntegerField(choices=STATE_CHOICES, blank=True, null=True)

    aadhar_card_file= models.FileField(upload_to='Aadhar-Card',blank=True, null=True)
    pan_card_file= models.FileField(upload_to='Pan-Card',blank=True, null=True)
    


    def __str__(self):
        return str(self.profile)
    



class AdmissionProfile(models.Model):
    profile= models.OneToOneField(Profile, on_delete=models.CASCADE)
    course= models.ForeignKey(Courses, on_delete=models.CASCADE)
    admission_type= models.IntegerField(choices= ( (1,'Distance'), (2,'Regular')))
    admission_academic_year = models.CharField(max_length=9)

    def __str__(self):
        return str(self.profile)


class ContactInformationProfile(models.Model):
    profile= models.OneToOneField(Profile,on_delete=models.CASCADE)
    student_mobile_number=  models.CharField(max_length=10, unique=True)
    emergency_contact_name= models.CharField(max_length=50)
    emergency_mobile_number= models.CharField(max_length=10, unique=True)

    address_line1= models.TextField()
    address_line2= models.TextField()
    state= models.IntegerField(choices=STATE_CHOICES)
    district= models.CharField(max_length=100)
    pincode= models.CharField(max_length=6)

    def __str__(self):
        return str(self.profile)
    
    def clean(self):
        # Ensure emergency contact name is not the same as the user's contact
        if self.emergency_contact_name == self.profile.user.username:
            raise ValidationError("Emergency contact name cannot be the same as the user's contact name.")

        # Ensure emergency contact number is not the same as the user's contact number
        if self.emergency_mobile_number == self.student_mobile_number:
            raise ValidationError("Emergency contact number cannot be the same as the user's contact number.")

        # Ensure emergency contact number could be father's or mother's number
        if hasattr(self.profile, 'parentprofile'):
            if self.emergency_mobile_number not in [
                self.profile.parentprofile.fathers_mobile_number,
                self.profile.parentprofile.mother_mobile_number
            ]:
                raise ValidationError("Emergency contact number must be either father's or mother's number.")

BOARD_CHOICES = [
    (1, "Central Board of Secondary Education (CBSE)"),
    (2, "Indian School Certificate (ISC)"),
    (3, "Indian School Certificate Examinations (ICSE)"),
    (4, "National Institute of Open Schooling (NIOS)"),
    (5, "Board of High School and Intermediate Education Uttar Pradesh (UP Board)"),
    (6, "Jammu and Kashmir State Board of School Education (JKBOSE)"),
    (7, "Board of Secondary Education Rajasthan (RBSE)"),
    (8, "Himachal Pradesh Board of School Education (HPBOSE)"),
    (9, "Madhya Pradesh Board of Secondary Education (MPBSE)"),
    (10, "Chhattisgarh Board of Secondary Education (CGBSE)"),
    (11, "Punjab School Education Board (PSEB)"),
    (12, "Haryana Board of School Education (BSEH / HBSE)"),
    (13, "Bihar School Examination Board (BSEB)"),
    (14, "Gujarat Secondary and Higher Secondary Education Board (GSEB)"),
    (15, "Maharashtra State Board Of Secondary and Higher Secondary Education (MSBSHSE)"),
    (16, "Andhra Pradesh Board of Intermediate Education (BIEAP)"),
    (17, "Andhra Pradesh Board of Secondary Education (BSEAP)"),
    (18, "West Bengal Board of Secondary Education (WBBSE)"),
    (19, "West Bengal Council of Higher Secondary Education (WBCHSE)"),
]

class EducationQualificationProfile(models.Model):
    #10th Education
    profile= models.OneToOneField(Profile,on_delete=models.CASCADE)
    board_10th= models.IntegerField(choices=BOARD_CHOICES)
    passing_year_10th= models.IntegerField()
    passed_from_state_10th= models.IntegerField(choices= STATE_CHOICES)
    obtained_marks_10th= models.IntegerField()
    percentage_10th= models.DecimalField(max_digits=5,decimal_places=2)
    school_name_10th= models.CharField(max_length=100)
    result_file_10th= models.FileField(upload_to='10th-Marksheets')
#------------------------------------------------------------------------
    
    board_12th= models.IntegerField(choices=BOARD_CHOICES)
    passing_year_12th=models.IntegerField()
    passed_from_state_12th=models.IntegerField(choices= STATE_CHOICES)
    obtained_marks_12th=models.IntegerField()
    percentage_12th=models.DecimalField(max_digits=5,decimal_places=2)
    school_name_12th=models.CharField(max_length=100)
    result_file_12th=models.FileField(upload_to='12th-Marksheets')
    
    

class ParentProfile(models.Model):
    profile= models.OneToOneField(Profile,on_delete=models.CASCADE)
    fathers_name= models.CharField(max_length=50)
    fathers_mobile_number= models.CharField(max_length=10, unique=True)
    
    designation= models.CharField(max_length=50)
    occupation= models.CharField(max_length=100)
    annual_income= models.IntegerField()

#------------------------------------------------------------------------
    mother_name= models.CharField(max_length=100)
    mother_mobile_number= models.CharField(max_length=10, unique=True)
    mother_occupation= models.CharField(max_length=100)


    guardian_name= models.CharField(max_length=100, blank=True, null=True)
    relation_type= models.CharField(max_length=50, blank=True, null=True)
    guardian_mobile_number= models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.profile)



# authenticate: aadhar, pan, phone(if possible), dob must be valid.
# add: personal payment gateway on fee section, courses wise fee structure, add sem wise subjects of all courses while adding a course 
class UserSemesterData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    credits_earned = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.semester.name}"