from django.forms import ModelForm

from models import Replay
from models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['informated', 'published', 'replayed',]
        
        
class ReplayForm(ModelForm):
    class Meta:
        model = Replay
        exclude = ('message', )

