# This goal of this script is to create 100 sample shows to populate the moogit
# database in order to create an environment suitable for testing

from shows.models import Venue, Band, showOrder, show

from faker import Factory

import words, venues2, genres, 


def insertBand(name, bandHomeTown, bandHomeState, bandGenre):
    '''to create and save a band object '''
    from shows.models import Band
    b = Band(  bandName = name,
            homeTown = bandHomeTown,
            homeState = bandHomeState,
            genre = bandGenre)
    b.save()

def insertVenue(name, venueDescription, venueArea, venueNeighborhood,
                venueStreetAddress, venueCity, venueState, 
                venueZip, venuePhone):
    '''to create and save a Venue Object'''
    from shows.models import Venue
    v = Venue(  venueName = name,
                description = venueDescription,
                area = venueArea,
                neighborhood = venueNeighborhood,
                streetAddress = venueStreetAddress,
                city = venueStreetAddress,
                state = venueState,
                zip = venueZip)
    v.save()









# #number of records needed
# noRecords = 100

# # noNouns = Number of nouns requested
# # noVerbs = Number of verbs requested
# # number 
#     bandName      = models.CharField(max_length = 200,
#                                       default = "Band Name")


#     homeTown      = models.CharField(max_length = 100,
#                                     default = "Home Town")
    

#     homeState     = "Ca"
#     #TODO: Add a genre selection field
#     genre         = models.CharField(max_length = 75 )
#     bandDateAdded = models.DateTimeField(auto_now_add = True)
#     bandDateMod   = models.DateTimeField(auto_now = True)
#     # shows         = models.ManyToManyField(Show2)
# area_choices = {"NC": "North County",
#               "EC": "East County",
#               "CC": "Central",
#               "SB": "South Boy" }


# bandGenres[apples][random.randint(0 , len(bandGenres[apples]))]

# fake = Factory.create()
# fake.text()

# fullAddress = fake.address()

# streetAddress = fullAddress.split('\n')[0]

# city = fullAddress.split('\n')[1].split()[0]
# state = fullAddress.split('\n')[1].split()[1]
# zipCode = fullAddress.split('\n')[1].split()[2]
