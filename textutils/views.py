# Created by Priyanshu
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def removepunc(request):
    message = request.POST.get('text', 'default')
    check1 = request.POST.get('check1', 'default')
    check2 = request.POST.get('check2', 'default')
    check3 = request.POST.get('check3', 'default')
    check4 = request.POST.get('check4', 'default')
    if check1 == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in message:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        message = analyzed

    if check2 == 'on':
        analyzed = ''
        for char in message:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Lower Case to UpperCase', 'analyzed_text': analyzed}
        message = analyzed

    if check3 == 'on':
        analyzed = ''
        for char in message:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        message = analyzed

    if check4 == 'on':
        analyzed = ''
        for index, char in enumerate(message):
            if not (message[index] == " " and message[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        message = analyzed

    if check1 != "on" and check2 != "on" and check3 != "on" and check4 != "on":
        return render(request, 'error.html')
    else:
        return render(request, 'analyze.html', params)


def search(request):
    search1 = request.POST.get('search2', 'default')
    if search1 == 'analyze':
        return render(request, 'analyze.html')
    else:
        return render(request, 'error.html')


def about(request):
    return render(request, 'error.html')


def contactus(request):
    return render(request, 'error.html')
