from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        std_id = request.POST['std_id']
        email = request.POST['email']
        message = request.POST['message']
        
        user = Contact.objects.filter(email = email)
        
        if user:
            message = "Message Already Send !!"
            return render(request, 'contact.html', {'msg':message})
        else:
            newUser = Contact.objects.create(name = name, std_id = std_id, email = email, message = message)
            message = "Message Send Successfully...."
            return render(request, 'contact.html', {'msg':message})
        
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        std_id = request.POST['std_id']
        club = request.POST['club']
        email = request.POST['email']
        password = request.POST['password']
        
        user = SignUp.objects.filter(std_id = std_id)
        if user:
            message = "User Already Exist !"
            return render(request, 'signup.html', {'msg': message})
        else:
            newUser = SignUp.objects.create(image = image, name = name, std_id = std_id, club = club, email = email, password = password)
            message = "Registration Successfully !"
            return render(request, 'payment.html', {'msg': message})
        
    return render(request, 'signup.html')

def eucc(request):
    return render(request, 'eucc.html')

def vac(request):
    return render(request, 'vac.html')

def debate(request):
    return render(request, 'debate.html')

def culture(request):
    return render(request, 'culture.html')

def bsec(request):
    return render(request, 'bsec.html')

def payment(request):
    return render(request, 'payment.html')


def member(request):
    memberData = Member.objects.all()
    # for members search
    search = request.GET.get('search')
    
    if search != None:
        memberData = Member.objects.filter(mem_name__icontains = search)
        
    data = {
        'memberData' : memberData,
        
    }
    
    return render(request, 'member.html', data)

