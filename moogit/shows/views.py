from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, render_to_response

from django.http import HttpResponse

# Create your views here.
import datetime
import csv
import json



from django.http           import HttpResponse
from django.template       import RequestContext, loader
from django.shortcuts      import get_object_or_404, render_to_response, redirect, render
from django.utils          import timezone
from django.contrib        import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.formsets import formset_factory

from django.views.generic import TemplateView, View, ListView, \
    UpdateView, DeleteView, CreateView, FormView


class homePage(View):

    def get(self, request, *arg, **kwargs):

        from models import show, showOrder
        showsByDate = show.objects.all().order_by('Date')
        next10shows =  showsByDate[:10]
        return render_to_response('home.html',
                                    {'shows' : next10shows },
                                    context_instance = RequestContext(request))

class viewEditHome(View):

    def get(self, request, *args, **kwargs):

        from shows.models import Band
        from shows.forms import addBandForm, addShowForm

        form = addBandForm
        showForm = addShowForm

        BandFormSet = formset_factory(addBandForm, extra = 3)

        bands = Band.objects.all()

        bandDictList = []
        idDictList = []
        bandNameList = []
        bandObjectDict = {}

        for band in bands:

            idDict= { 'label' : band.bandName,'value' : band.bandID }

            bandList =  [band.bandName, band.homeTown, band.homeState2, band.genre, band.subGenre]


            bandObjectDict[band.bandID] = bandList
         

            idDictList.append(idDict)
            bandDictList.append(bandObjectDict)

        bandObjectDict = json.dumps(bandObjectDict)
        bandDictList = json.dumps(bandDictList)
        idDictList = json.dumps(idDictList)

        return render_to_response('editHome.html', {'form': form,
                                                'addShowForm': addShowForm,
                                                'bands': bands,
                                                'bandObjectDict' : bandObjectDict,
                                                'BandFormSet' : BandFormSet,
                                                'bandDictList' : bandDictList,
                                                'idDictList': idDictList},
                              context_instance = RequestContext(request))

    def post(self, request, *args, **kwargs):

        from shows.models import show, Band, Venue

        

        return HttpResponse("<p>Apples</p>")

class editShows(View):

    def get(self, request, *arg, **kwargs):

        from shows.models import show, showOrder

        #get shows from database, filter by permissions

        # return venues that the user can add shows to
        # return venues that the user can edit the information for (address etc)
        # return shows that user can edit
        # Display form allowing user to add shows to their venue

    def post(self, request, *arg, **kwargs):

        from models import show, showOrder

        # validate form
            #if valid save object
            #return to editShows

        # if not valid
            # return reason not valid, send back to editShows

class editBands(View):

    def get(self, request, *args, **kwargs):

        from shows.models import Band

        # return list of bands
        # display form that will allow for band editing
        # when a band edit is chosen, form is filled in with that band's info

    def post(self, request, *args, **kwargs):

        from shows.models import Band

        #if form valid
            #save band changes
        #if form not valid
            #return to editBands.get()

class editVenues(View):

    def get(self, request, *args, **kwargs):

        from shows.models import Venue

        # return a list of venues that the user is allowed to edit
        # display form for adding and editing a value

    def post(self, request, *args, **kwargs):

        from shows.models import Venue

        #if form is valid
            #save Venue data
        #if form is not valid
            #return to editVenues.get()