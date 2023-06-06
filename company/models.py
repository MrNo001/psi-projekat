from django.db import models
from account.models import User
from offer.models import Offer

RATE_CHOICES = [
	(1, '1 - VeryBad'),
	(2, '2 - Bad'),
	(3, '3 - Average'),
	(4, '4 - Good'),
	(5, '5 - Excelent'),
]


class Review(models.Model):
	user = models.ForeignKey(User,related_name='Ocenjivac',on_delete= models.CASCADE)
	firm = models.ForeignKey(User,related_name='Ocenjeni',on_delete= models.CASCADE)
	offer = models.ForeignKey(Offer, on_delete=models.CASCADE,default=None,null=True)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=3000, blank=True)
	rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
	likes = models.PositiveIntegerField(default=0)
	unlikes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.user.username
