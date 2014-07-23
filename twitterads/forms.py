from django import forms
from django.utils.translation import ugettext as _
from models import Tweets

class GreetingsForm(forms.ModelForm):
    post = forms.CharField(required=True, max_length=140, widget=forms.Textarea(attrs={'placeholder':_('Enter your tweet'),'cols':150,'rows':5}), error_messages={'required': _('Title Required')})
    start_date = forms.DateField(required=True,input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={'placeholder':_('Start Date'),'autocomplete':'off'}), error_messages={'required': _('Start Date Required')})
    start_time = forms.TimeField(required=False,input_formats=['%I:%M %p'], widget=forms.TimeInput(attrs={'placeholder':_('Start Time')}), error_messages={'required': _('Start Time Required')})

    class Meta:
        model = Tweets
        fields = ('post', 'start_date', 'start_time')
    
class TweetingForm(forms.ModelForm):
    post = forms.CharField(required=True, max_length=140, widget=forms.Textarea(attrs={'placeholder':_('Enter your tweet'),'cols':150,'rows':5}), error_messages={'required': _('Title Required')})

    class Meta:
        model = Tweets
        fields = ('post',)