from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.


def login_view(request):
    
    if request.POST:
        
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(request=request, phone = phone, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request=request, message="Siz muvaffaqiyalti login qildingiz!")
            return redirect('/')
            
        else:
            
            messages.error(request=request, message="Phone yoki Password xato")     
            return render(request=request, template_name='accounts/login.html')
    
    return render(request=request, template_name='accounts/login.html')


def register_view(request):
    
    if request.POST:

        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data_from_form = form.cleaned_data

            user = CustomUser.objects.create_user(
                first_name=cleaned_data_from_form.get("first_name"),
                last_name=cleaned_data_from_form.get("last_name"),
                email=cleaned_data_from_form.get("email"),
                password=cleaned_data_from_form.get("password"),
                phone=cleaned_data_from_form.get("phone"),
                profession=cleaned_data_from_form.get("profession"),
                image=cleaned_data_from_form.get("image"),
            )

            login(request=request, user=user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect("/")

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()} maydonida - {error}')

    return render(request=request, template_name='accounts/register.html')


def logout_view(request):
    
    logout(request=request)
    
    return redirect('/')