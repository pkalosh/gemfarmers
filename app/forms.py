from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User
from app.models import *

from django.forms import BaseModelFormSet




from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from django.utils.encoding import force_text
from django.db import transaction
from app.models import *

from djrichtextfield.widgets import RichTextWidget
class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=("Enter your Username"), max_length=254)

from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = False
    last_name = forms.CharField(max_length=35, label='Other Names')
    first_name = forms.CharField(max_length=35, label='First Name', )
    id_number = forms.CharField(max_length=200, label="ID Number")
    cell = forms.CharField(max_length=100, label="Phone Number")
    field_order = ['first_name', 'last_name','id_number','email', 'cell', 'password1','password2' ]
    
    @transaction.atomic
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email =self.cleaned_data['email']
        #Assigning email to the username
        user.username=self.cleaned_data['email']
        phone_number=self.cleaned_data['cell']
        id_number=self.cleaned_data['id_number']
       
        user.save()
        userprofile = Profile(user=user,
                                cell=phone_number,id_number=id_number)
        userprofile.save()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['email'].required = True
            
    class Meta:

        model=User
        fields=['email','password']


class FarmerForm(forms.ModelForm):
     class Meta:
        model=Farmer
        fields=['farm','size',]

class ProfileForm(forms.ModelForm):
     class Meta:
        model=Profile
        fields=['id_number','cell', 'county', 'sub_county','town', 'market_center' ,'twitter_link','facebook_link',]

class StudentForm(forms.ModelForm):
     class Meta:
        model=Student
        fields=['institution','course',]

class InstitutionForm(forms.ModelForm):
     class Meta:
        model=Institution
        fields=['name','cell','county','sub_county','town','twitter_link','facebook_link']


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label=("Enter your Email"), max_length=254)

class PassForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('password',)


class UForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(UForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['first_name'].label = "First Name"
            self.fields['last_name'].label = "Other Names"
    class Meta:
        model=User
        fields=['last_name','first_name']



class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model=Entrepreneur
        fields=('business','registration','business_type',)

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('good',)
