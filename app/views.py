from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from libs.device_data import device_data as device

@ensure_csrf_cookie
def index(request):
	if request.method == 'GET':
		return render(request, "pc/index.html")

@ensure_csrf_cookie
def profile(request):
	if request.method == 'GET':
		return render(request, "pc/profile.html")

@ensure_csrf_cookie
def rankings(request):
	if request.method == 'GET':
		return render(request, "pc/rankings.html")