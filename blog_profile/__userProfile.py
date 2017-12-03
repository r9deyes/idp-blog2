from django.db import models

class __UserProfile:
	#avatar = models.ImageField()
	phone = models.CharField(max_length = 25)
	skype = models.CharField(max_length = 100)
	reduces_to_sql = False