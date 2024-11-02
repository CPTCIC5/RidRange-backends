from rest_framework import serializers
from .models import Profile,PersonalProfile, AdmissionProfile, ContactInformationProfile, EducationQualificationProfile, ParentProfile, Division, Subject, Semester,Courses
from django.contrib.auth.models import User


class DivisonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Division
        fields= ('name')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields= ('name','code')




class SemesterCreateSerializer(serializers.ModelSerializer):
    #subjects=  SubjectSerializer(many= True)
    class Meta:
        model= Semester
        fields= ('semester_number', 'start_date', 'subjects')

class SemesterSerializer(serializers.ModelSerializer):
    subjects=  SubjectSerializer(many= True)
    class Meta:
        model= Semester
        fields= ('id','semester_number', 'start_date', 'subjects')


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'name',
            'fee',
            'duration',
            'session_start_year'
        )

class CourseSerializer(serializers.ModelSerializer):
    divisions = DivisonSerializer(many=True)
    semesters = SemesterCreateSerializer(many=True)

    class Meta:
        model = Courses
        fields = (
            'name',
            'fee',
            'duration',
            'session_start_year',
            'divisions',
            'semesters',
        )



class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True)
    confirm_new_password= serializers.CharField(required=True,write_only=True)



class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields= ('avatar','course','current_semester','usn','roll_number')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "avatar",
            "course",
            "current_semester",
            "usn",
            "roll_number"
        )

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "email",
            "is_active",
            "profile"
        )

    def get_full_name(self, obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create profile related to the user
        if profile_data:
            profile_instance, _ = Profile.objects.update_or_create(user=instance, defaults=profile_data)
            # Update profile instance with nested serializer data
            ProfileSerializer(profile_instance, data=profile_data, partial=True).is_valid(raise_exception=True)
            profile_instance.save()
        return instance
    



class PersonalProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalProfile
        fields = ('title','mobile_number','gender','aadhar_card_number','pan_number','differently_abled','dob','caste','state','aadhar_card_file','pan_card_file')

    def create(self, validated_data):
        return PersonalProfile.objects.create(profile= self.context['request'].user.profile ,**validated_data)


class PersonalProfileSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer()
    class Meta:
        model= ProfileSerializer
        fields = ('id','profile','title','mobile_number','gender','aadhar_card_number','pan_number','differently_abled','dob','caste','state','aadhar_card_file','pan_card_file')




class AdmissionProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionProfile
        fields = (
            'course',
            'admission_type',
            'admission_academic_year'
        )

    def create(self, validated_data):
        return AdmissionProfile.objects.create(profile= self.context['request'].user.profile ,**validated_data)
    

class AdmissionProfileSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer()
    course= CourseSerializer()
    class Meta:
        model = AdmissionProfile
        fields = (
            'id',
            'profile',
            'course',
            'admission_type',
            'admission_academic_year'
        )





class ContactInformationProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformationProfile
        fields = (
            'student_mobile_number',
            'emergency_contact_name',
            'emergency_mobile_number',
            'address_line1',
            'address_line2',
            'state',
            'district',
            'pincode'
        )

    def create(self, validated_data):
        return ContactInformationProfile.objects.create(profile= self.context['request'].user.profile ,**validated_data)
    

class ContactInformationProfileSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer()
    class Meta:
        model = ContactInformationProfile
        fields = (
            'id',
            'profile',
            'student_mobile_number',
            'emergency_contact_name',
            'emergency_mobile_number',
            'address_line1',
            'address_line2',
            'state',
            'district',
            'pincode'
        )




class EducationQualificationProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationQualificationProfile
        fields = (
            'board_10th',
            'passing_year_10th',
            'passed_from_state_10th',
            'obtained_marks_10th',
            'percentage_10th',
            'school_name_10th',
            'result_file_10th',
            'board_12th',
            'passing_year_12th',
            'passed_from_state_12th',
            'obtained_marks_12th',
            'percentage_12th',
            'school_name_12th',
            'result_file_12th'
        )

    def create(self, validated_data):
        return EducationQualificationProfile.objects.create(profile= self.context['request'].user.profile ,**validated_data)

class EducationQualificationProfileSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer()
    class Meta:
        model = EducationQualificationProfile
        fields = (
            'id',
            'profile',
            'board_10th',
            'passing_year_10th',
            'passed_from_state_10th',
            'obtained_marks_10th',
            'percentage_10th',
            'school_name_10th',
            'result_file_10th',
            'board_12th',
            'passing_year_12th',
            'passed_from_state_12th',
            'obtained_marks_12th',
            'percentage_12th',
            'school_name_12th',
            'result_file_12th'
        )




class ParentProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = (
            'fathers_name',
            'fathers_mobile_number',
            'designation',
            'occupation',
            'annual_income',
            'mother_name',
            'mother_mobile_number',
            'mother_occupation',
            'guardian_name',
            'relation_type',
            'guardian_mobile_number'
        )

    def create(self, validated_data):
        return ParentProfile.objects.create(profile= self.context['request'].user.profile ,**validated_data)
    

class ParentProfileSerializer(serializers.ModelSerializer):
    profile= ProfileSerializer()
    class Meta:
        model = ParentProfile
        fields = (
            'id',
            'profile',
            'fathers_name',
            'fathers_mobile_number',
            'designation',
            'occupation',
            'annual_income',
            'mother_name',
            'mother_mobile_number',
            'mother_occupation',
            'guardian_name',
            'relation_type',
            'guardian_mobile_number'
        )