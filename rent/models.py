from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    picture = models.CharField(max_length=500)
    # Table Keys:
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Profil de {}".format(self.user.username)


class Pool(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=300)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    picture = models.CharField(max_length=(500))
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
    type = models.CharField(max_length=100, choices=POOL_TYPE_CHOICES)
    # Table Keys:
    profil = models.ForeignKey('Profil', on_delete=models.CASCADE)

    def __str__(self):
        return "Piscine: {}, à {}, {}€ par personne".format(self.title, self.address, self.price)


class Booking(models.Model):
    state = models.CharField(max_length=100)
    date = models.DateField()
    # Table Keys:
    profil = models.ForeignKey('Profil', on_delete=models.CASCADE)
    pool = models.ForeignKey('Pool', on_delete=models.CASCADE)

    def __str__(self):
        return "Location de la piscine: {}, le {}, statut: {}".format(self.pool.title, self.date, self.state)