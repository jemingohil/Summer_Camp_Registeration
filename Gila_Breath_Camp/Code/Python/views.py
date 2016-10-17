from django.shortcuts import render

# Create your views here.
#from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
import sys
sys.path.append("Python")
sys.path.append("Python/Entities")
import common_functions
import user
import ast
import json
sys.path.append("Python/User_Stories")
import registration
import choose_date
import check_in_status

def test(request):
	context = ""
	return render(request,'index.html',context)

@csrf_exempt
def create_volume(request):
	c = {}
	c.update(csrf(request));
	data = request.POST["vol_name"]
	print("data"+data)
	#print(type(data))
	#data_dict = ast.literal_eval(data)
	#print(data_dict["password"])
	#k = common_functions.Common_functions()
	#ur = user.User()
	#ur.setUserId(data_dict["user_id"])
	#ur.setUserName(data_dict["user_name"])
	#ur.setUserType(data_dict["user_type"])
	#if ur.setPassword(data_dict["password"]) == "Password should be more than 5 characters":
	#	return false
	#else:
	#	ur.setPassword(data_dict["password"])
	#k.insertIntoCsv("user.csv",ur)
	try:
		regis = registration.Registration()
		st = regis.register(data)
		print(type(st))
	except Exception as e:
		st = e
		print(st)
	return HttpResponse(st,content_type="application/type")

@csrf_exempt	
def test_js(request):
	print ("in python")
	c = {}
	c.update(csrf(request));
	data = request.POST["vol_name"]
	print("data"+data)
	try:
		dt = choose_date.Choose_date()
		st = dt.chooseDate(data)
		print(st)
		cis = check_in_status.Check_in_status()
		st_get = cis.getCheckInStatus(json.dumps({"data" :[{"camp_time_slots":"2016-10-15 00:00:00.000000"}]}))
		print(st_get)
	except Exception as e:
		st_get = e
		print(st_get)
	#st = '{"jemin":"gohil","karthik":"manjunath"},{"":"","":""}'
	#st = '''{#  "data":[''' + st +''']#}'''
	return HttpResponse(st_get,content_type="application/type")






