from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    print("//////////HELP///ON////WAY/")
    return HttpResponse("Hello World")

def new(request):
    print("//////////HELP///ON////WAY/")
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print("//////////HELP///IS////HERE/")
    return redirect('/')

def show(request, number):
    print("//////////HELP///IM////INT/")
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    print("//////////HELP///IM////INT/")
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    print(f"route to delete blog {number}")
    return redirect('/')