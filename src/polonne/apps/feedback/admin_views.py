#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from models import  Message
from models import Replay
from forms import ReplayForm


def message_replay(request, id):
    
    msg = Message.objects.get(id=id)
    
    if request.method == 'POST': 
            form = ReplayForm(request.POST) 
            if form.is_valid(): 
                # Saving replay for current message
                replay = Replay()
                replay.message = msg
                replay.text = form.cleaned_data['text']
                replay.save()
                # Set status for message 
                msg.replayed = True
                msg.save()
                # Send email with text for message owner
                replay_msg = replay.text
                email = EmailMessage('[KaDeBo] Ответ на Ваше сообщение', replay_msg, to=[msg.email])
                email.send()
                
                messages.info(request, 'Ваше сообщение было отправлено!')
                
                return HttpResponseRedirect('/admin/feedback/message/%s'%(id)) 
    else:
        form = ReplayForm() 

    data = {
        "form":form,
        "msg":msg,
    
    }
   
    return render_to_response(
            "admin/feedback/message/replay-admin-form.html",
            data,
            RequestContext(request, {}),
        )

message_replay = staff_member_required(message_replay)
    
    