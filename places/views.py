import os, sys, util
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import State
from utils import validate_fields
# Create your views here.

def places(request):
	state = State.objects.filter()
	return HttpResponse(json.dumps(serialize(State.objects.filter())), content_type="application/json")


def place_details(request, place_id):
	state = State.objects.filter()
	return HttpResponse(json.dumps(serialize(State.objects.filter(id = place_id))), content_type="application/json")

@csrf_exempt
def add_place(request):
	print 'here'
	if request.method == 'POST':
		try:
			params = json.loads(request.body)
		except:
			return HttpResponseBadRequest(json.dumps({'error': 'Json Data Required'}),content_type = 'application/json')
		all_fields_names = State._meta.get_all_field_names()
		params = validate_fields(all_fields_names, params)
		return HttpResponse(json.dumps({'success': all_fields_names}), content_type= 'applicaton/json')




