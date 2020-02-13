from django.shortcuts import render


# Create your views here.
def mainmenu(request):
    return render(request, 'mainmenu/mainmenu.html')