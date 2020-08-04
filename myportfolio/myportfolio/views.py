from django.http import HttpResponse

def HomePage(request):
    return HttpResponse('Home')

def about(request):
    return HttpResponse('about')
