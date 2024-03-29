def insertBand(name, bandHomeTown, bandHomeState, bandGenre, stupid):
  '''to create and save a band object '''
  from shows.models import Band
  b = Band(  bandName = name,
             homeTown    = bandHomeTown,
             homeState2   = bandHomeState,
             genre       = bandGenre,
             subGenre    = stupid)
  b.save()

def insertVenue(name, venueContact , venueDescription, venueArea, venueNeighborhood,
                venueStreetAddress, venueCity, venueState, 
                venueZip, venuePhone):
  '''to create and save a Venue Object'''
  from shows.models import Venue
  v = Venue(  venueName     = name,
              contact2  = venueContact,
              description   = venueDescription,
              area          = venueArea,
              neighborhood  = venueNeighborhood,
              streetAddress = venueStreetAddress,
              city          = venueStreetAddress,
              state         = venueState)
  v.save()

def insertContact(contactEmail, contactFirstName, contactLastName,
                  contanctNickname):
  '''to create and save a conact object'''
  from shows.models import contact
  c = contact(  email     = contactEmail,
                firstName = contactFirstName,
                lastName  = contactLastName,
                nickname  = contanctNickname )
  c.save()

def insertShow(venueID, showDate, showTime, showBandExtraTesxt, showAge, showCost):
  from shows.models import show
  s = show( showVenueID = venueID,
            Date = showDate,
            Time = showTime,
            bandExtraTesxt = showBandExtraTesxt,
            age = showAge,
            cost = showCost)
  s.save()

def insertShowOrder(bandOrder, orderBandID, orderShowID):
  from shows.models import show, Band, showOrder
  o = showOrder(order = bandOrder, 
                bandID =  orderBandID,
                showID = orderShowID )
  o.save()
