__author__ = 'waynejessen'


#from django.forms import ModelForm
from django import forms
from django.forms import widgets
from localflavor.us.forms import USPhoneNumberField, USPSSelect, USStateSelect, USStateField

from shows.models import Band, genre

bands = Band.objects.all()

genres = genre.objects.all()

bandNameList = []
bandGenreList = []

for band in bands:

  smallNameTuple = (band.bandID, band.bandName)

  bandNameList.append(
    smallNameTuple
    )

for genre in genres:
  smallGenreTuple = (genre.genreID, genre.genreName)
  bandGenreList.append(smallGenreTuple) 

#sort genres
bandGenreList = sorted(bandGenreList, key = lambda genre:genre[1])

class addBandForm(forms.Form):

  bandName = forms.CharField(widget=forms.TextInput({'class' : 'bandName editLock',
                                                      'id' : 'bandNameID'}))

  bandTown = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-group-control editLock',
                                                          'id' : 'bandTownID'}))

  bandState = USStateField(widget=USStateSelect(attrs={'class':'form-control editLock',
                                                        'id':'bandStateID'})) 

  genre = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control editLock',
                                                        'id':'genreID'}),
                           choices=bandGenreList)


