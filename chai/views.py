from django.shortcuts import render

def all_chai(request):
    return render(request, 'ChupChai/all_chai.html')