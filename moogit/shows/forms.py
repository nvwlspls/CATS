__author__ = 'waynejessen'


#from django.forms import ModelForm
from django import forms
from localflavor.us.forms import USPhoneNumberField, USPSSelect, USStateSelect

class addBandForm(forms.Form):

    bandName = forms.CharField(max_length= 200,
                               label= "Band Name",
                               widget= forms.TextInput(attrs = {'class': 'form-control',
                                                                'placeholder' : "Band Name"}))

    bandTown = forms.CharField(max_length= 100,
                               label = "Band Home Town",
                               widget= forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder' : 'Band Town'}))

    bandState = USStateSelect()

    genre = forms.ChoiceField()

    subGenre = forms.CharField()