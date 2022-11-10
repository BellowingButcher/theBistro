from django.db import models

#  models.IntegerField(default=SpicyLevel.mild, choices = SpicyLevel.choices)
class FullMenu(models.Model):
    SPICY_LEVEL_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    spicy_level = models.IntegerField(choices=SPICY_LEVEL_CHOICES, default=1)

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    

class Cuisine(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# -----------------------------------------------------------------------------------------------------------------
# using this for a reference to my spicy level subclass
# class Ticket(models.Model):
#     class Statuses(models.IntegerChoices):
#         OPEN = 2, 'Open'
#         PENDING = 3, 'Pending'
#         RESOLVED = 4, 'Resolved'
#         CLOSED = 5, 'Closed'
#     class Priorities(models.IntegerChoices):
#         LOW = 1, 'Low'
#         MEDIUM = 2, 'Medium'
#         HIGH = 3, 'High'
#         URGENT = 4, 'Urgent'
    
#     priority = models.IntegerField(default=Priorities.LOW, choices = Priorities.choices)
#     status = models.IntegerField(default=Statuses.OPEN, choices=Statuses.choices)