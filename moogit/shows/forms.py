__author__ = 'waynejessen'


#from django.forms import ModelForm
from django import forms
from django.forms import widgets
from localflavor.us.forms import USPhoneNumberField, USPSSelect, USStateSelect, USStateField

class addBandForm(forms.Form):

  bandName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-group-control'}))

  bandTown = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-group-control'}))

  bandState = USStateField(widget=USStateSelect(attrs={'class':'form-control'})) 

  genre = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))

  subGenre = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))


    # bandName = forms.CharField(max_length= 200,
    #                            label= "Band Name",
    #                            widget= forms.TextInput(attrs = {'class': 'form-control',
    #                                                             'placeholder' : "Band Name"}))

    # bandTown = forms.CharField(max_length= 100,
    #                            label = "Band Home Town",
    #                            widget= forms.TextInput(attrs={'class': 'form-control',
    #                                                           'placeholder' : 'Band Town'}))

    # bandState = forms.

    # genre = forms.ChoiceField()

    # subGenre = forms.CharField()