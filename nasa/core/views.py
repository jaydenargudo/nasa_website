from django.shortcuts import render

def lock(request):
    return render(request, 'lock/lockscreen.html')