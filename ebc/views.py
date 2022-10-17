from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import receive_message, delete, ebc_notification, send_mess
from .models import wamessage_log, customer #test
# Create your views here.



@api_view(['GET','POST'])
def wacallback(request):#whatsapp
    if request.method == 'GET':
        if request.GET['hub.verify_token'] == '12345678qwertyuiopasdfg':
            x =int(request.GET['hub.challenge'])
        else:
            x = 'wrong verification token or format'
            
    
    if request.method =='POST':
        payload = request.data
        receive_message.apply_async(args = [payload])
        #test.objects.create(test = payload)

        sponse = {
            'message': 'done'
        }
        x = sponse
    return Response(x)

def wadel(request):
    if request.user.is_authenticated:
        x = delete.apply_async()
        return HttpResponse('Deleted successfully' +str(x))
    else:
        return HttpResponse('permission denied')


def icallback(request):#instagram
    if request.method == 'GET':
        if request.GET['hub.verify_token'] == '12345678qwertyuiopasdfg':
            x =int( request.GET['hub.challenge'])
        else:
            x = 'wrong verification token or format'
            
    
    if request.method =='POST':
        payload = request.data
        #wa.receive_message(payload)
        sponse = {
            'message':'success'
        }
        x = sponse
    return Response(x)

def mecallback(request):#messanger
    if request.method == 'GET':
        if request.GET['hub.verify_token'] == '12345678qwertyuiopasdfg':
            x =int( request.GET['hub.challenge'])
        else:
            x = 'wrong verification token or format'
            
    
    if request.method =='POST':
        payload = request.data
        #wa.receive_message(payload)
        sponse = {
            'message':'success'
        }
        x = sponse
    return Response(x)

def msan1(request):#Manual send notification
    if request.user.is_authenticated:
        ebc_notification.apply_async()
        return HttpResponse('Notification sent' )
    else:
        return HttpResponse('Access Denied')


def msan(request, num):#Manual send notification
    if request.user.is_authenticated:
        ebc_notification.apply_async(args = [num])
        return HttpResponse('Notification send to ' + num )
    else:
        return HttpResponse('Access Denied')
def pp(request):
    return render(request, 'privacy_policy.html')


def chat_agent(request, nums):
    #try:
    chat_log = customer.objects.all
    chat_log1 = wamessage_log.objects.filter(customer = customer.objects.get(customer_no = nums))
    context = {'all_chat':chat_log, 'current_chat':chat_log1}
    return render (request, 'chat_app.html', context)
    #except:
    #    return HttpResponse('WRONG NUMBER')

def chat_ag_pst(request):
    if request.method == 'POST':
        payload ={'phone':request.POST['number'], 'message' : request.POST['message'], 'bot_id':request.POST['bot_id'] }
        abc = send_mess.apply_async(args = [payload])
        print(abc)
        return redirect('/chat_agent/'+request.POST['number'])
