from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('instructors/', views.InstructorListView.as_view()),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name='instructor-detail'),
    
    path('courses/', views.CourseListView.as_view()),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    
]
