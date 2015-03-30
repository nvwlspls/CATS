from django.db import models

from localflavor.us.forms import USPhoneNumberField, USStateSelect, USZipCodeField


class contact(models.Model):

    email = models.EmailField(max_length = 100,
                              default = 'email@email.com',
                              primary_key = True)
    firstName = models.CharField(max_length = 100,
                                default = 'first name')
    lastName = models.CharField(max_length = 100,
                                default = 'last name')
    nickname = models.CharField(max_length = 100,
                                default = 'nickname')


# Create your models here.
class Venue(models.Model):
    AREA_CHOICES = (
        ("NC", "North County"),
        ("EC", "East County"),
        ("CC", "Central"),
        ("SB", "South Boy") 
    )


    venueID        = models.AutoField(primary_key = True)
    venueName      = models.CharField(max_length = 75,
                                default = "Venue Name")
    description    = models.TextField()
    area           = models.CharField(choices =  AREA_CHOICES,
                            max_length = 20)
    neighborhood   = models.CharField(max_length = 75,
                                        default = "Neighborhood")
    venueDateAdded = models.DateTimeField(auto_now_add = True)
    venueLastMod   = models.DateTimeField(auto_now = True)
    streetAddress  = models.CharField(max_length = 150,
                                        default = "Street Address")
    city           = models.CharField(max_length = 150,
                                      default = "City")
    state          = models.CharField( max_length = 50,
                                        default = "None")
    zipCode        = models.CharField(max_length = 9,
                                        default = '00000', null = True)
    phone          = USPhoneNumberField()
    contact2       = models.ForeignKey('contact', related_name = 'contact2',
                                        null = True)
    # contact        = models.ForeignKey('contact', related_name = 'venueContact',
    #                                     default = 1)
    # conFirstName   = models.CharField(max_length = 100,
    #                                 default = "First Name")
    # conLastName    = models.CharField(max_length = 100,
    #                                 default  = "Last Name")
    # conEmail       = models.EmailField(max_length = 100,
    #                             default = "email@email.com")

    def __unicode__(self):
       return unicode(self.venueName)  

class Band(models.Model):
    bandID        = models.AutoField(primary_key = True)
    bandName      = models.CharField(max_length = 200,
                                      default = "Band Name")
    homeTown      = models.CharField(max_length = 100,
                                    default = "Home Town")
    homeState      = models.CharField( max_length = 50, null = True)
    homeState2     = models.CharField( max_length = 50, null = True)
    #TODO: Add a genre selection field
    genre         = models.CharField(max_length = 75 )
    subGenre      = models.CharField(max_length = 75)
    bandDateAdded = models.DateTimeField(auto_now_add = True)
    bandDateMod   = models.DateTimeField(auto_now = True)
    # shows         = models.ManyToManyField(Show2)
    
    def __unicode__(self):
       return unicode(self.bandName) 

class showOrder(models.Model):
    showOrderID    = models.AutoField(primary_key = True)
    order          = models.IntegerField()
    showID         = models.ForeignKey("show", related_name = 'showIDOrder')
    bandID         = models.ForeignKey("Band", related_name = 'bandIDOrder')

    class Meta:
        ordering = ['order']


class show(models.Model):
    show2ID        = models.AutoField(primary_key = True)
    showVenueID    = models.ForeignKey("Venue")
    Date           = models.DateField()
    Time           = models.TimeField()
    DateTimeAdded  = models.DateTimeField(auto_now_add = True)
    DateTimeMod    = models.DateTimeField(auto_now = True)
    bands          = models.ManyToManyField(Band, related_name = "bands", 
                                                    null = True )
    orders         = models.ManyToManyField(showOrder, related_name = 'orders', null = True)
    bandExtraTesxt = models.TextField()
    age            = models.CharField(max_length = 3, null = True)
    cost           = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __unicode__(self):
       return unicode(self.show2ID) 

class genre(models.Model):

    genreID = models.AutoField(primary_key = True)
    genreName = models.CharField(max_length=100)\

    def __unicode__(self):
        return unicode(self.genreName)

class subGenre(models.Model):

    fk_GenreID = models.ForeignKey("genre", related_name = 'subGenre_Genre')
    subGenreName = models.CharField(max_length=100)




