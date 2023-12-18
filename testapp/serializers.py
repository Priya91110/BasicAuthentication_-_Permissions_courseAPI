from rest_framework import serializers
from .models import Course, Instructor


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
      
        
class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    # passing url view_name/api/course/id
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')
    class Meta:
        model = Instructor
        fields = '__all__'
