from django.db import models

# Create your models here.
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Felix', 'Alley Cat', 'smells funny', 5),
    Cat('Harvey', 'sphynx', 'black', 1),
    Cat('Mittens', 'siamese', 'very friendly', 14)
]
