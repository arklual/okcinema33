from django.shortcuts import render

def manual(request):
    return render(request, 'partial/manual.html')