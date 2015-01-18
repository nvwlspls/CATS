from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, render_to_response

from django.http import HttpResponse

# Create your views here.
import datetime
import csv

# from forms import 
from django.http           import HttpResponse
from django.template       import RequestContext, loader
from django.shortcuts      import get_object_or_404, render_to_response, redirect, render
from django.utils          import timezone
from django.contrib        import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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