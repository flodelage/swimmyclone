from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.FileField(upload_to='profile_images', blank=True)

    def __str__(self):
        return "Profil de {}({} {})".format(self.user.username, self.user.first_name, self.user.last_name)


class Pool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=300)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    image = models.FileField(upload_to='pool_images', blank=True)
    price = models.PositiveIntegerField()
    length = models.FloatField()
    width = models.FloatField()
    heated = models.BooleanField(default=False)
    OUTDOOR = 'OUTDOOR'
    INDOOR = 'INDOOR'
    COVERED = 'COVERED'
    POOL_TYPE_CHOICES = [
        (OUTDOOR, 'Outdoor'),
        (INDOOR, 'Indoor'),
        (COVERED, 'Covered'),
    ]
    type = models.CharField(max_length=100, choices=POOL_TYPE_CHOICES, default=OUTDOOR)

    def __str__(self):
        return "Piscine: {}, à {}, {}€ par personne".format(self.title, self.address, self.price)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    pool = models.ForeignKey('Pool', on_delete=models.CASCADE)

    participants = models.PositiveIntegerField(default=0)
    date = models.DateField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return "Location de la piscine: {}, le {}, par: {} {}, statut: {}".format(self.pool.title, self.date,
                                                                                  self.user.first_name,
                                                                                  self.user.last_name, self.state)
