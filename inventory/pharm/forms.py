from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,PasswordInput
from django import forms

from . models import Items

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['category','item_name','batch_number','expiry_date','quantity_of_packs','cost_per_pack','units_per_pack','cost_per_unit_bp','markup','cost_per_unit_sp','issued_from','issued_by','issued_to','received_by','phone_number_r','entered_by','phone_number_e']

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['category','item_name','batch_number','expiry_date','quantity_of_packs','cost_per_pack','units_per_pack','cost_per_unit_bp','markup','cost_per_unit_sp','issued_from','issued_by','issued_to','received_by','phone_number_r','entered_by','phone_number_e']

class ItemSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Items
        fields = ['item_name']

class IssueForm(forms.ModelForm):
    class Meta:
        model  = Items
        fields = ['quantity_issued','issued_from_internally','issued_by_internally','issued_to_internally']

class ReceiveForm(forms.ModelForm):
    class Meta:
        model  = Items
        fields = ['quantity_received','received_by_internally']

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model  = Items
        fields = ['reorder_level']