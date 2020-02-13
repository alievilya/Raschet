from django.shortcuts import render


def page1(request):
    return render(request, 'part2/Page1.html')


