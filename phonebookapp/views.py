import phonebookapp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.

def data(request):
    cntform=ContactForm()
    return render(request,'page1.html',{"form":cntform})


def addperson(request):
    try:
        if request.method == 'POST':
            cntform = ContactForm(request.POST)
            if cntform.is_valid():
                cntform.save()
        return render(request, 'page1.html', {"form": cntform, "msg": "Successfully Added!"})
    except Exception as e:
        print(e)
        return HttpResponse("Error Happened!")

def delete(request):
    return render(request,"deletepage.html")


def erase(request):
    try:
        person=request.POST['name']
        object1=Contact.objects.filter(name=person)
        if object1 is not None:
            object1.delete()
            return render(request,'page1.html')

    except Exception as e:
        print(e)


def displayContact(request):
    try:
        conData = Contact.objects.all()
        return render(request, 'page1.html', {"data": conData})

    except Exception as e:
        print(e)
        return render(request, 'page1.html', {"failure": "Unable to display!"})


def updations(request):
    
        return render(request, 'update.html')

def updateName(request):
    try:
        conVal = request.POST['contact']
        current = request.POST['curname']
        new     = request.POST['newname']

        contactData = Contact.objects.get(number = conVal)
        contactData.name = new
        contactData.save()
        return render(request, 'update.html', {"name": "Name Updated!"})
    except Exception as e:
        print(e)
        return render(request, 'update.html', {"name_failure": "Contact not exists!"})

def updateNumber(request):
    try:
        current = request.POST['contact']
        new = request.POST['newcontact']

        contactData = Contact.objects.get(number = current)
        contactData.number = new
        contactData.save()
        return render(request, 'update.html', {"number": "Number Updated!"})
    except Exception as e:
        print(e)
        return render(request, 'update.html', {"number_failure": "Contact not exists!"})
