from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage

def index(request):

	return render(request, "main.html" )


def chatboxindex(request):    
	
#	t1 = TextMessage.objects.create(talker='Michael' , message= 'How is everybody doing?')
#	t2 = TextMessage.objects.create(talker='Alex' , message= 'I fine.')
#	t3 = TextMessage.objects.create(talker='Chard' , message= 'I fine too.')
	talker = request.GET.get("name",False)
	message = request.GET.get("msg",False)
	db = TextMessage.objects.create( talker=talker, message=message)
	msg = TextMessage.objects.all()

	return render(request, "chatbox.html" ,locals())

def picindex(request):

	import random
	list20 = []
	i = 28
	while i>0:
		pics = str(random.randint(1,1088))
		list20.append("https://picsum.photos/200/200/?image="+pics)
		i-=1
    

	return render(request, "pic.html" ,{'list20':list20})

#def results(request):
#	guess = request.GUESS.get('msg')
#	result = 1
#	return HttpResponse(render(guess,result))