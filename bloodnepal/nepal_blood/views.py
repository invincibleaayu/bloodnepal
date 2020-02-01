from django.shortcuts import render                         #to return html file as response
from django.http import HttpResponse
from .models import getInvolved,Donate,app
from django.views.generic import TemplateView                            #imported the database models
#now we create method for our pipeline/urls here 
def home(request):
    return render(request,'home.html')                      #the request is used to generate response 
                                                            #which is used in render
def donate(request): 
    if request.method=='POST':
        dbList=Donate()                                            #creating instance of the database class getInvolved
        dbList.name=request.POST.get('fullName')
        dbList.address=request.POST.get('address')
        dbList.phoneNo=request.POST.get('phoneNumber')
        dbList.email=request.POST.get('email')
        dbList.gender=request.POST.get('gender')
        dbList.bloodGroup=request.POST.get('blood')
        dbList.RH_type=request.POST.get('bloodRh')
        dbList.save()
        return render(request,'donate.html')                                       #our url donate/ is request
    return render(request,'donate.html')

def organization(request):
    return render(request,'organization.html')

def getinvolved(request):
    if request.method=='POST':
        dbList=getInvolved()                                            #creating instance of the database class getInvolved
        dbList.name=request.POST.get('fullName')
        dbList.address=request.POST.get('address')
        dbList.dateOfBirth=request.POST.get('bday')
        dbList.occupation=request.POST.get('occupation')
        dbList.phoneNo=request.POST.get('phoneNumber')
        dbList.email=request.POST.get('email')
        dbList.gender=request.POST.get('gender')
        dbList.bloodGroup=request.POST.get('blood')
        dbList.RH_type=request.POST.get('bloodRh')
        dbList.ques_1=request.POST.get('donation')
        dbList.ques_2=request.POST.get('opinion')
        dbList.save()
        return render(request,'getinvolved.html')

    return render(request,'getinvolved.html')

def about(request):
    return render(request,'about.html')

def carrer_with_us(request):
    return render(request,'carrerwithus.html')

def joinhands(request):
    return render(request,'joinhands.html')

class chartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context["qs"]= app.objects.all()
        return context
