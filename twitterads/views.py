import datetime
from dateutil.parser import parse

from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from twitterads.models import Tweets
from forms import GreetingsForm,TweetingForm
from tasks import send_twitter_status
from utils import twitter_now

class TweetFeatures(ListView):
    template_name = "twitterads/features.html"
    model = Tweets
    

class GreetingCreate(CreateView):
    template_name = "twitterads/add-greeting-tweets.html"
    model = Tweets
    form_class = GreetingsForm
    success_url=reverse_lazy('tweet_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GreetingCreate, self).form_valid(form)
    
    def get_success_url(self):
        eta = datetime.datetime.combine(self.object.start_date,self.object.start_time)
        work = send_twitter_status.apply_async((self.request.user, self.object), eta=eta)
        self.object.task_id = work.id
#         send_twitter_status.apply_async((2, 2), eta=self.object.start_date, expires=datetime.now() + timedelta(days=1))
        # add.apply_async((2, 2), retry=True, retry_policy={
        #     'max_retries': 3,
        #     'interval_start': 0,
        #     'interval_step': 0.2,
        #     'interval_max': 0.2,
        # })
        self.object.save()
        return super(GreetingCreate, self).get_success_url()
    
    
class TweetList(ListView):
    template_name = "twitterads/list-tweets.html"
    model = Tweets
    paginate_by = 10
    context_object_name = 'tweets'
    
    def get_queryset(self):
        return Tweets.objects.filter(created_by=self.request.user.id).order_by('-created_on')
    
class DeleteList(ListView):
    template_name = "twitterads/list-tweets.html"
    model = Tweets
    context_object_name = 'tweets'

    def get_queryset(self):
        Tweets.objects.filter(created_by=self.request.user.id,id=self.kwargs['pk']).delete()
        return Tweets.objects.filter(created_by=self.request.user.id)
    
class PostTweet(CreateView):
    template_name = "twitterads/add-n-tweet.html"
    model = Tweets
    form_class = TweetingForm
    success_url=reverse_lazy('tweet_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GreetingCreate, self).form_valid(form)
    
    def get_success_url(self):
        twitter_now(self.request.user, self.object)
        return super(GreetingCreate, self).get_success_url()