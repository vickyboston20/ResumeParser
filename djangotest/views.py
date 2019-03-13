from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginPage,RegisterPage

def home_page(request):
    context = {
    "top":"perficient",
    "title":"home_page",
    "content":"welcome to home_page",
    }
    if request.user.is_authenticated:
        context["premium_content"]="Hello user logged in successfully"
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
    "top":"About-perficient",
    "title":"about_page",
    "content":"welcome to about_page",
    }
    return render(request,"about.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    "top":"Contact-perficient",
    "title":"Perficient",
    "content":"welcome to contact_page",
    "form":contact_form,
    }
    if contact_form.is_valid():
        return redirect("contact")
    return render(request,"contacts/views.html",context)
    # if request.method=="POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))

def login_page(request):
    form = LoginPage(request.POST or None)
    context ={
    "top":"SignIn-perficient",
    "title":"Perficient",
    "content":"Login page",
    "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("error")
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterPage(request.POST or None)
    context = {
    "top":"Register-perficient",
    "title":"Perficient",
    "content":"Sign up",
    "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("error")
    return render(request,"auth/register.html",context)
