from rest_framework import serializers
from .models import mseResult,mseMarks
from users.serializers import CourseSerializer,SemesterSerializer,SubjectSerializer


class mseResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= mseResult
        fields= ('mse_number', 'course', 'semester', 'result_day')



class mseResultSerializer(serializers.ModelSerializer):
    course=  CourseSerializer()
    semester= SemesterSerializer()

    class Meta:
        model= mseResult
        fields= ('id', 'mse_number', 'course', 'semester', 'result_day')



class mseMarksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= mseMarks
        fields= ['subject','maximum_marks','obtained_marks']

    def create(self, validated_data):
        return mseMarks.objects.create(profile= self.context['request'].user.profile ,**validated_data)
    
class mseMarksSerializer(serializers.ModelSerializer):
    subject= SubjectSerializer()
    model= mseMarks
    fields= ['id','subject', 'maximum_marks','obtained_marks']