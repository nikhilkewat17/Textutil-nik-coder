# I have created this file-Nikhil Govind Kewat
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse('''<h1>Harry</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Codes with Harry </a>''')


#def about(request):
#    return HttpResponse("About ,Kewat Nikhil")
# code for video 7

def index(request):

    return render(request,'index.html')
    #return HttpResponse("Home")
#def about(request):
    #return render(request,'about.html')
#def contact(request):
    #return render(request,'contact.html')
def nik1(request):
    return HttpResponse('''
    <h1>Code With Harry : <a href="https://codewithharry.com/">Click Here </a></h1>
    <h2>Django course with Harry : <a href="https://codewithharry.com/videos/python-django-tutorials-hindi-0/">Django Full Course List</a></h2>
    ''')

    
def analyze(request):
    # get text
    djtext= request.POST.get('text','default')
    # check checkbox values
    removepunc= request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount =request.POST.get('charcount','off')
    #print(removepunc)
    #print(djtext)
# check is on
    if removepunc == "on":
        #analyzed=djtext
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = { 'purpose':'Changed to Uppercase','analyzed_text':analyzed }
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if (charcount == "on"):
        analyzed = len(djtext)
        params = { 'purpose':'Character count of string','analyzed_text':analyzed }
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if (extraspaceremover =="on"):
        analyzed = ""
        for index ,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Space','analyzed_text':analyzed }
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed +char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext=analyzed

    if (removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and charcount !="on" and fullcaps !="on"):
        return  render(request,'error.html')

    return render(request, 'analyze.html', params)









#def capfirst(request):
#    return HttpResponse("capitilize first <a href='/'>back</a>")

#def newlineremove(request):
#    return HttpResponse("new line remover <a href='/'>back</a>")

#def spaceremove(request):
#    return HttpResponse("space remover <a href='/'>back</a>")

#def charcount(request):
#    return HttpResponse("character counter <a href='/'>back</a>")