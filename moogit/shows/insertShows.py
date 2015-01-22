from faker import Factory
from shows import venues2
import random, time


from shows.modes import Venue, contact, Show, showOrder

venues = venues2.venues
fake = Factory.create()




for i in range(1,1000):
    
    '''create random time'''
    randMonth  = str(random.randint(1, 12)).zfill(2)
    randDate   = str(random.randint(1, 28)).zfill(2)
    randHour   = str(random.randint(0, 23)).zfill(2)
    randMinute = str(random.randint(0, 59)).zfill(2)
    # format random date/time
    randShowTimeString  = ('2014' + randMonth + randDate + randHour + randMinute)
    randShowDateTime = time.strptime(randShowTimeString, '%Y%m%d%H%M')
    # random date
    stringShowDate  = time.strftime("%Y-%m-%d", randShowDateTime)
    # random time
    randShowTime = str(randShowDateTime.tm_hour).zfill(2) + ':' + random.choice(['00', '15', '30', '45'])
    showVenueID = random.choice(Venue.objects.all())
    Date = stringShowDate
    Time = randShowTime
    bandExtraTesxt = fake.text()
    age = random.choice([0, 18, 21])
    cost = random.choice([10.00, 15.00, 12.50, 18.50])
    insertShow( showVenueID ,stringShowDate, randShowTime, bandExtraTesxt, age, cost)

shows = show.objects.all()


#Insert Bands into Shows
for s in shows:
    noOfBands = random.randint(2 ,5)
    allBands = Band.objects.all()
    showBands = random.sample(allBands, noOfBands)
    for band in showBands:
        s.bands.add(band)
        s.save()

for e in shows:
    from shows.models import showOrder
    sortOrder = 1
    showBands = e.bands.all()
    for band in showBands:
        insertShowOrder(sortOrder, band, e)
        thisSortOrder = showOrder.objects.filter(bandID = band, showID = e )[0]
        e.orders.add(thisSortOrder)
        sortOrder += 1



    e.orders.add(order)
    e.save


    showVenueID    = models.ForeignKey("Venue")
    Date           = models.DateField()
    Time           = models.TimeField()
    DateTimeAdded  = models.DateTimeField(auto_now_add = True)
    DateTimeMod    = models.DateTimeField(auto_now = True)
    bands          = models.ManyToManyField(Band, related_name = "bands" )
    orders         = models.ManyToManyField(showOrder, related_name = 'orders')
    bandExtraTesxt = models.TextField()
    age            = models.IntegerField()
    cost           = models.DecimalField(max_digits = 5, decimal_places = 2)
    order          = models.IntegerField()
    showID         = models.ForeignKey("show", related_name = 'showIDOrder')
    bandID         = models.ForeignKey("Band", related_name = 'bandIDOrder')

