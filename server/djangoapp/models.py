from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Add any other fields you want for CarMake

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    # Choices for the type field
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=SEDAN,
    )
    
    year = models.DateField()
    
    # Add any other fields you want for CarModel
    
    def __str__(self):
        return f"{self.car_make} {self.name}"

class CarDealer(models.Model):
    # Placeholder class for CarDealer
    pass

class DealerReview(models.Model):
    # Placeholder class for DealerReview
    pass
