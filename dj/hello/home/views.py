from django.shortcuts import render,HttpResponse
from home.models import Data,Expdata,doners
# Create your views here.
def index(request):
    # return HttpResponse('This is home page')
    data={'python':'python is easy'}
    context=data
    return render(request,'index.html',context)
def login(request):
    return render (request,'login.html')
def freshregister(request):
    if request.method=='POST':
        name=request.POST.get('nme')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        if pw==cpw:
            data=Data(name=name,pno=pno,email=email,gender=gender,dob=dob,password=pw)
            data.save()
            return render(request,'login.html')
        
    else:
        return render (request,'freshregister.html')
def expregister(request):
    if request.method=='POST':
        name=request.POST.get('nme')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        yop=request.POST.get('yop')
        if pw==cpw:
            data=Expdata(name=name,pno=pno,email=email,gender=gender,dob=dob,password=pw,yop=yop)
            data.save()
            
            return render(request,'login.html',{'name':name})
    else:
        return render (request,'expregister.html')
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
    o1=doners()
    o1.name='jathin'
    o1.pno=9874563210
    o1.email='jathin.email.com'
    o1.bgroop='o+'
    o1.address='Kalyan'
    o2=doners()
    o2.name='suaheel'
    o2.pno=9517538524
    o2.email='susheel.email.com'
    o2.bgroop='o-'
    o2.address='Thane'
    o3=doners()
    o3.name='abhishek'
    o3.pno=9874563210
    o3.email='abhishek.email.com'
    o3.bgroop='ab+'
    o3.address='Kaluva'
    o4=doners()
    o4.name='Diptesh'
    o4.pno=753951852
    o4.email='Diptesh.email.com'
    o4.bgroop='ab-'
    o4.address='Mumbra'
    objects=[o1,o2,o3,o4]
    return render (request,'verbal.html',{'data':objects})