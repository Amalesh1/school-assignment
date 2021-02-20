from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import datetime
from students.models import Contact, EnglishAssignment, PhysicsAssignment, MathAssignment
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    context={
        "variable1":"hello"
    }
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Class=request.POST.get('Class')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, Class=Class, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Feedback has been recorded!')
    return render(request, 'contact.html')

def teachers(request):
    return render(request, 'teachers.html')

def subjects(request):
    return render(request, 'subjects.html')

def assignments(request):
    if request.method == "POST":
        roll=request.POST.get('roll')
        topics=request.POST.get('topics')
        dept=request.POST.get('dept')
        sem=request.POST.get('sem')
        ans = request.POST.get('ans')
        assignments=EnglishAssignment(roll=roll, topics=topics, dept=dept, sem=sem, ans=ans, date=datetime.today(), time=datetime.now())
        assignments.save()
        messages.success(request, messages, 'Assignment submitted successfully!')
    return render(request, 'assignments.html')

def physicsassignments(request):
    if request.method == "POST":
        roll=request.POST.get('roll')
        topics=request.POST.get('topics')
        dept=request.POST.get('dept')
        sem=request.POST.get('sem')
        ans = request.POST.get('ans')
        physicsassignments=PhysicsAssignment(roll=roll, topics=topics, dept=dept, sem=sem, ans=ans, date=datetime.today(), time=datetime.now())
        physicsassignments.save()
        messages.success(request, messages, 'Assignment submitted successfully!')
    return render(request, 'physicsassignment.html')

def mathassignments(request):
    if request.method == "POST":
        roll=request.POST.get('roll')
        topics=request.POST.get('topics')
        dept=request.POST.get('dept')
        sem=request.POST.get('sem')
        ans = request.POST.get('ans')
        mathassignments=MathAssignment(roll=roll, topics=topics, dept=dept, sem=sem, ans=ans, date=datetime.today(), time=datetime.now())
        mathassignments.save()
        messages.success(request, messages, 'Assignment submitted successfully!')
    return render(request, 'mathassignments.html')


    
    

