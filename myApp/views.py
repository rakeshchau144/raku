from django.shortcuts import render
from . models import Employee


def home(request):  
    return render(request,'home.html')

def index(request):
    return render(request, 'index.html')

##mydata = Employee.objects.all().values()
  #  if request.method == 'POST':   
   ###   print(email, passe)
      #  print(mydata)
       # Employee.objects.create(Email=email, paass = passe)
  
        # print(context)
        #print(type(mydata))
