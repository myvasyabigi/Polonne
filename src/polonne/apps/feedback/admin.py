from django.contrib import admin

from models import Message
from models import Replay

class MessageAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'pub_date', 'informated', 'published', 'replayed']

admin.site.register(Message, MessageAdmin)


class ReplayAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'pub_date']

admin.site.register(Replay, ReplayAdmin)
