from django.shortcuts import render

# Create your views here.
def career(request):
    return render(request,'Career/career.html')