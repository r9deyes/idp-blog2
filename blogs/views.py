# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render('blogs/index.html')

def detail(request, article_id=None):
	return render('blogs/detail,html')
	
def userProfile(request, user_id=None):
	return render('blogs/userProfile.html')

 