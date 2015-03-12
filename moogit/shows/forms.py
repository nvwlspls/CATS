__author__ = 'waynejessen'


#from django.forms import ModelForm
from django import forms
from django.forms import widgets
from localflavor.us.forms import USPhoneNumberField, USPSSelect, USStateSelect, USStateField

from shows.models import Band

bands = Band.objects.all()

bandNameList = []

for band in bands:

  smallTuple = (band.bandID, band.bandName)

  bandNameList.append(
    smallTuple
    )



class addBandForm(forms.Form):

  bandName = forms.CharField(widget=forms.TextInput({'class' : 'bandName ',
                                                      'id' : 'bandNameID'}))

  bandTown = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-group-control',
                                                          'id' : 'bandTownID'}))

  bandState = USStateField(widget=USStateSelect(attrs={'class':'form-control',
                                                        'id':'bandStateID'})) 

  genre = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',
                                                        'id':'genreID'}),
                            choices=bandNameList)

  subGenre = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',
                                                          'id': 'subGenreID'}))


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