from faker import Factory
from shows import venues2
import random, time


from shows.modes import Venue, contact, Show, showOrder

venues = venues2.venues
fake = Factory.create()


noOfBands = random.int(1,5)

for i in range(1,1000):


	randMonth  = str(random.randint(1, 12)).zfill(2)
	randDate   = str(random.randint(1, 31)).zfill(2)
	randHour   = str(random.randint(0, 23)).zfill(2)
	randMinute = str(random.randint(0, 59)).zfill(2)

	randShowTimeString  = ('2014' + randMonth + randDate + randHour + randMinute)

	randShowTime = time.strptime(randShowTime, format = '%Y%m%d%H%M')


	showVenueID = random.choice(Venue)


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

