from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from myapps.models import Student, Faculty, Staff


class LoginForm(forms.Form):
    username = forms.CharField(max_length=18)
    password = forms.CharField(widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError(
                "Password is too short"
            )
        return password

    def clean(self):
        clean_data = super(ResetPasswordForm, self).clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password does not match."
            )
        return clean_data

class StudentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     user=kwargs.pop('user')
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     self.fields['phone'].input = 'xxx-xxxxxxx'
    #     if user is not None:
    #         if hasattr(user, 'first_name'):
    #             self.fields['first_name'].initial = user.first_name
    #         if hasattr(user, 'last_name'):
    #             self.fields['last_name'].initial = user.last_name
    #         if hasattr(user, 'address'):
    #             self.fields['address'].initial = user.address
    #         if hasattr(user, 'email'):
    #             self.fields['email'].initial = user.email
    #         if hasattr(user, 'city'):
    #             self.fields['city'].initial = user.city
    #         if hasattr(user, 'province'):
    #             self.fields['province'].initial = user.province
    #         if hasattr(user, 'phone'):
    #             self.fields['phone'].initial = user.phone
    #         if hasattr(user, 'age'):
    #             self.fields['age'].initial = user.age

    class Meta:
        model = Student
        #exclude = ()
        fields = [ "first_name", "last_name", "address", "email", "city", "province","phone", "age", "status", "gender"]
        widgets = {'gender': forms.RadioSelect(attrs={'class': 'radio-inline'}),}

class FacultyForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     user=kwargs.pop('user')
    #     super(FacultyForm, self).__init__(*args, **kwargs)
    #     self.fields['phone'].input = 'xxx-xxxxxxx'
    #     if user is not None:
    #         if hasattr(user, 'first_name'):
    #             self.fields['first_name'].initial = user.first_name
    #         if hasattr(user, 'last_name'):
    #             self.fields['last_name'].initial = user.last_name
    #         if hasattr(user, 'address'):
    #             self.fields['address'].initial = user.address
    #         if hasattr(user, 'email'):
    #             self.fields['email'].initial = user.email
    #         if hasattr(user, 'city'):
    #             self.fields['city'].initial = user.city
    #         if hasattr(user, 'province'):
    #             self.fields['province'].initial = user.province
    #         if hasattr(user, 'phone'):
    #             self.fields['phone'].initial = user.phone
    #             self.fields['phone'].input = 'xxx-xxxxxxx'
    #         if hasattr(user, 'Fac_position'):
    #             self.fields['Fac_position'].initial = user.age

    class Meta:
        model = Faculty
        #exclude = ()
        fields = [ "first_name", "last_name", "address", "email", "city", "province", "phone", "Fac_position"]

class StaffForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     user=kwargs.pop('user')
    #     super(StaffForm, self).__init__(*args, **kwargs)
    #     self.fields['phone'].input = 'xxx-xxxxxxx'
    #     if user is not None:
    #         if hasattr(user, 'first_name'):
    #             self.fields['first_name'].initial = user.first_name
    #         if hasattr(user, 'last_name'):
    #             self.fields['last_name'].initial = user.last_name
    #         if hasattr(user, 'address'):
    #             self.fields['address'].initial = user.address
    #         if hasattr(user, 'email'):
    #             self.fields['email'].initial = user.email
    #         if hasattr(user, 'city'):
    #             self.fields['city'].initial = user.city
    #         if hasattr(user, 'phone'):
    #             self.fields['phone'].initial = user.phone
    #         if hasattr(user, 'province'):
    #             self.fields['province'].initial = user.province

    class Meta:
        model = Staff
        #exclude = ()
        fields = [ "first_name", "last_name", "address", "email", "city", "province", "phone" ]

