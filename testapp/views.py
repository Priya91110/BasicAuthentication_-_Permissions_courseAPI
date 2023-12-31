from rest_framework import generics
from django.shortcuts import render
from .serializers import InstructorSerializer, CourseSerializer
from .models import Instructor , Course
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class InstructorListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] 
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
    

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()    
    
    
class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
 

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()    