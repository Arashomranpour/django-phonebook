from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from . import models
from django.http import HttpResponse
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ContactForm
from .models import Contact

# Home view
def home(request):
    if request.user.is_authenticated:
        messages.info(request, f"{request.user.username} Welcome!")
        records=models.Contact.objects.all()
        if records:
            context = {"records":records}
            return render(request, "home.html", context)
        else:
            return render(request,"home.html")
    else:
        messages.info(request, "Welcome Guest!")
        return render(request,"home.html")
# Signup view
def signup(request):
    # Prevent authenticated users from accessing the signup page
    if request.user.is_authenticated:
        messages.success(request, "You already have an account.")
        return redirect("home")  

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            messages.success(request, "Account Created Successfully")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form": form})
def create(request):
    return HttpResponse(content="test")

# Logout view
@login_required
def Logoout(request):
    messages.success(request, "Account Logout Successfully")
    logout(request)
    return redirect("/login/")  # Redirect to the login page

@login_required(login_url="login")
def RecordView(request,pk):
    record_id=models.Contact.objects.get(id=pk)
    return render(request, "record.html", {"record": record_id})
    
class RecordUpdateView(UpdateView):
    model = models.Contact  # Ensure Contact model is correctly defined
    template_name = "record.html"
    fields = ['username', 'phone', 'email', 'address']  # Include fields to be updated
    success_url = reverse_lazy('home')  # Replace with the name of your success page

    # Optionally, you can override the form_valid method if additional logic is required.
    def form_valid(self, form):
        return super().form_valid(form)
    
    
    
    
class RecordDeleteView(DeleteView):
    model = Contact
    template_name = 'delete_record.html'
    success_url = reverse_lazy('home')


class AddRecordView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')  # Replace with your desired success page
