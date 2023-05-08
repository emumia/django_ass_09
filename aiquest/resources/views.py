from django.shortcuts import render

# Create your views here.
def resource(request):
    return render(request,'Resources/resources.html')