from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request,'Courses/course.html')

def django(request):
    return render(request,'Courses/django_web_development.html')

def machine_learning(request):
    return render(request,'Courses/machine_learning.html')

def deep_learning(request):
    return render(request,'Courses/deep_learning.html')

def data_analysis(request):
    return render(request,'Courses/data_analysis.html')

def cloud_computing(request):
    return render(request,'Courses/cloud_computing.html')

def big_data(request):
    return render(request,'Courses/big_data.html')

def python(request):
    return render(request,'Courses/python.html')

def statistics(request):
    return render(request,'Courses/statistics.html')

def sql(request):
    return render(request,'Courses/sql.html')

