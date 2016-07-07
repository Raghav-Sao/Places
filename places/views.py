from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import State

# Create your views here.

def index(request):
	return HttpResponse("ok")

def place_details(request, place_id):
	state = State.objects.filter()
	result = []
	for s in state:
		state_result = {}
		print s.name
		state_result['name'] = s.name
		result.append(state_result);
	response = HttpResponse(json.dumps(state_result), content_type="application/json")
	return response


