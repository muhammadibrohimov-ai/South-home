from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.Form):
    phone = forms.CharField(max_length=20, label="Phone")
    first_name = forms.CharField(max_length=50, label="First name")
    last_name = forms.CharField(max_length=50, label="Last name")
    email = forms.CharField(max_length=150, label="Email")
    profession = forms.CharField(max_length=100, label="Profession")
    image = forms.FileField(label="Image", required=False)
    password = forms.CharField(max_length=50, label="Password")
    confirm_password = forms.CharField(max_length=50, label="Confirm password")


    def clean(self): # bir nechta fieldlarni bir-biri bilan tekshirish uchun ishlatilinadi
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parollar bir biriga mos emas!")

        return  cleaned_data


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if '@' not in email or '.' not in email or not len(email.split("@")[0]) >= 5 or not email.endswith("gmail.com"):
            raise forms.ValidationError("Email formati xato!")

        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError("Ushbu emaildan oldin foydalanilgan!")

        return email


    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if phone.startswith("+998"):
            if len(phone) != 13 or not phone[1:].isdigit():
                raise forms.ValidationError("Telefon raqami +998 formatida noto‘g‘ri!")

        elif phone.startswith("998"):
            if len(phone) != 12 or not phone.isdigit():
                raise forms.ValidationError("Telefon raqami 998 formatida noto‘g‘ri!")

        elif phone.isdigit():
            if len(phone) != 9:
                raise forms.ValidationError("Telefon raqami 9 xonali bo‘lishi kerak!")
        else:
            raise forms.ValidationError("Telefon raqami noto‘g‘ri formatda!")

        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Bu telefon raqam allaqachon ishlatilgan!")

        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Telefondan avval foydalanilgan!")

        return phone



    

            
    
    
    
