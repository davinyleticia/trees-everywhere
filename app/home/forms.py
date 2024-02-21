from django import forms
from .models import PlantedTree, Tree, Account, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['tree', 'age', 'latitude', 'longitude', 'account']


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['name', 'scientific_name']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'active']


class UserCreateForm(UserCreationForm):
    about = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'about')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create the profile object
            Profile.objects.create(user=user, about=self.cleaned_data['about'])
        return user
