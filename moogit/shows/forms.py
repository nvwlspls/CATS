__author__ = 'waynejessen'


#from django.forms import ModelForm
from django import forms
from django.forms import widgets
from localflavor.us.forms import USPhoneNumberField, USPSSelect, USStateSelect, USStateField
from django.forms.extras.widgets import SelectDateWidget



from shows.models import Band, genre, Venue

bands = Band.objects.all()
genres = genre.objects.all()
venues = Venue.objects.all()


bandNameList = []
bandGenreList = []

venueNameList = []


for band in bands:

  smallNameTuple = (band.bandID, band.bandName)

  bandNameList.append(
    smallNameTuple
    )

for genre in genres:
  smallGenreTuple = (genre.genreID, genre.genreName)
  bandGenreList.append(smallGenreTuple) 

for venue in venues:
  smallVenueTuple = (venue.venueID, venue.venueName)
  venueNameList.append(smallVenueTuple)




#sort genres
bandGenreList = sorted(bandGenreList, key = lambda genre:genre[1])
#sort venues
venueNameList = sorted(venueNameList, key = lambda venue:venue[1])

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

class addShowForm(forms.Form):

  showTime = forms.DateField(widget=forms.TextInput({'class' :' time ui-timepicker-input',
                                                     'id' : 'timePicker'}))

  showDate = forms.CharField(widget=forms.TextInput({'id' : 'datePicker'}))

  showVenue = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control'}),
                                                    choices=venueNameList)
