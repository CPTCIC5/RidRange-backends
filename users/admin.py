from django.contrib import admin
from .models import Profile,PersonalProfile,Courses,AdmissionProfile,ContactInformationProfile,EducationQualificationProfile,ParentProfile,Division,Subject,Semester
# Register your models here.

admin.site.register(Division)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Profile)
admin.site.register(PersonalProfile)
admin.site.register(Courses)
admin.site.register(AdmissionProfile)
admin.site.register(ContactInformationProfile)
admin.site.register(EducationQualificationProfile)
admin.site.register(ParentProfile)
