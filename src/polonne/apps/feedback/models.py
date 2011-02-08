#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage


class Message(models.Model):
    title = models.CharField(verbose_name=("Заголовок"), max_length=255)
    email = models.EmailField()
    site = models.URLField(verbose_name=("Сайт"),
        blank=True, null=True)
    author = models.CharField(verbose_name = "Автор", 
        max_length=255, blank=True, null=True)
    text = models.TextField(verbose_name=("Сообщение"))
    informated = models.BooleanField(default=False, verbose_name=("Проинформирована администратора"))
    published = models.BooleanField(default = False, verbose_name=("Опубликовано"))
    replayed = models.BooleanField(default = False, verbose_name=("Отвечено"))
    pub_date = models.DateField(auto_now_add=True) 
    change_date = models.DateField(auto_now = True)
    
    class Meta:
        verbose_name = ("Сообщения")
        verbose_name_plural = ("Сообщения")
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
        
    def save(self):
        super(Message, self).save()
        if not self.informated:
            message = u"""Вы получили новое сообщения от %s <%s> \n
            %s\n
            Вы можете ответить на сообщение пройдя по ссылке http://localhost:8000/admin/messages/feedback/%s
            """ % (self.author, self.email, self.text, self.id)
            email = EmailMessage('[Новое сообщение на сайте]', message, to=[settings.OWNER_EMAIL])
            email.send()
            self.informated = True
            self.save()
            
            
        

class Replay(models.Model):
    message = models.ForeignKey(Message, verbose_name=("Сообщения на которое отвечали"))
    text = models.TextField(verbose_name=("Текст ответа"))
    pub_date = models.DateField(auto_now_add=True) 
    
    class Meta:
        verbose_name = ("Ответ на сообщение")
        verbose_name_plural = ("Ответы на сообщения")
        ordering = ['-pub_date',]
        
    def __unicode__(self):
        return self.message.title
        
        
        
        
    
       
    
