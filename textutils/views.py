# Created by Priyanshu
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index2.html')


def removepunc(request):
    # Get the text
    message = request.POST.get('text', 'default')
    # print(message)
    check1 = request.POST.get('check1', 'default')
    check2 = request.POST.get('check2', 'default')
    check3 = request.POST.get('check3', 'default')
    check4 = request.POST.get('check4', 'default')
    # print(check)
    if check1 == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in message:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif check2 == 'on':
        analyzed = ''
        for char in message:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Lower Case to UpperCase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif check3 == 'on':
        analyzed = ''
        for char in message:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif check4 == 'on':
        analyzed = ''
        for index, char in enumerate(message):
            if not (message[index] == " " and message[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return render(request, 'error.html')


def search(request):
    search1 = request.POST.get('search2', 'default')
    if search1 == 'analyze':
        return render(request, 'analyze.html')
    else:
        return render(request, 'error.html')
