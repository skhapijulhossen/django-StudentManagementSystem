from django.urls import path
from . import views
urlpatterns =[
    path('',views.index),
    path('add-student/',views.addStudent,name='addStudent'),
    path('add-student/add/',views.add,name='add'),
    path('search-student/',views.searchStudent,name='searchStudent'),
    path('search-student/search/',views.search,name='search'),
    path('all-students/',views.allStudents,name='allStudents'),
]