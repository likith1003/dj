from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('This is home page')
    return render(request,'index.html')
def login(request):
    return render (request,'login.html')
def freshregister(request):
    return render (request,'freshregister.html')
def expregister(request):
    return render(request,'expregister.html')
def pydev(request):
    return render (request,'pydev.html')
def django(request):
    return render (request,'django.html')
def mt(request):
    return render(request,'mt.html')
def at(request):
    return render (request,'at.html')
def web(request):
    return render (request,'web.html')
def sql(request):
    return render(request,'sql.html')
def apti(request):
    return render (request,'apti.html')
def verbal(request):
    return render (request,'verbal.html')