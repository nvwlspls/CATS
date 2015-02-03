# This goal of this script is to create 100 sample shows to populate the moogit
# database in order to create an environment suitable for testing

from shows.models import Venue, Band, showOrder, show
from shows import bandNames, genres, venues2

from faker import Factory

import random

# import insertFunctions

noRecords = 100

fake = Factory.create()

venues = venues2.venues

genreDict = genres.genres
 
area_choices = {"NC": "North County",
              "EC": "East County",
              "CC": "Central",
              "SB": "South Boy" }


neighborhoodFillers = ["Downtown",
                        "uptown",
                        "midtown",
                        "crosstown",
                        "nicetown",
                        "hill valley",
                        "sun canyon"]


for i in range(1,100):

  '''Create 100 Bands, Contacts and Venues'''
  
  '''bands'''
  fakeBandName =    random.choice(bandNames)
  fakeHomeTown     = fake.city()
  fakeBandState    = fake.state()
  fakeBandGenre    = random.choice(g.keys())
  fakeBandSubGenre = g[fakeBandGenre][random.randint(0 , 
                        len(g[fakeBandGenre]) -1 )]
  insertBand(fakeBandName, fakeHomeTown, fakeBandState, fakeBandGenre, fakeBandSubGenre)
  # insertContact(email, firstName, lastName, nickName)
  # insertVenue(venueName, description, area, venueNeighborhood,
  #             venueStreetAddress, venueCity, venueState, venueZip, venuePhone = venuePhone)

neighborhoodFillers

from faker import Factory
from shows import venues2
import random


from shows.modes import Venue, contact

venues = venues2.venues
fake = Factory.create()

for i in range(1, 100):

  fakeVenueName = random.choice(venues)
  fakeContact = random.choice(contact.objects.all())
  fakeDescription = fake.text()
  fakeArea = random.choice(area_choices.keys())
  fakeNeighborhood = random.choice(neighborhoodFillers)
  fakeVenueStreetAddress = fake.street_address()
  fakeVenueCity          = fake.city()
  fakeVenueState         = fake.state()
  fakeVenueZip           = str(fake.postcode())
  fakeVenuePhone         = fake.phone_number()
  insertVenue(fakeVenueName, fakeContact ,fakeDescription, fakeArea, 
              fakeNeighborhood, fakeVenueStreetAddress, fakeVenueCity, 
              fakeVenueState, fakeVenueZip, fakeVenuePhone)

