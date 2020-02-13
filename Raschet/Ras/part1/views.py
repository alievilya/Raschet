from django.shortcuts import render


def page1(request):
    return render(request, 'part1/Page1.html')


def page2(request):
    return render(request, 'part1/Page2.html')


def page3(request):
    return render(request, 'part1/Page3.html')


def page4(request):
    return render(request, 'part1/Page4.html')

