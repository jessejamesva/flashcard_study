from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    
)
from .models import FCard


# Create your views here.
def home(request):
    
    return render(request, 'flash/home.html', {'title': 'Home'})#context will pull db info

def create(request):
    return render(request, 'flash/create.html', {'title': 'Create'})

def study(request):
    context = {
        'cards': FCard.objects.all()
    }
    return render(request, 'flash/study.html', context)

class CardListView(ListView):
    model = FCard
    template_name = 'flash/study.html'
    context_object_name ='cards'
    # ordering = ['date_created'] #default, place a (-) infront of date to reverse, overridden by query below
    paginate_by = 5
    
class UserCardListView(ListView):
    model = FCard
    template_name = 'flash/study_start.html'
    context_object_name ='cards'
    #ordering = ['date_created'] #default, place a (-) infront of date to reverse
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FCard.objects.filter(creator=user).values('subject').distinct()
    
class UserSelectCardListView(ListView):
    model = FCard
    template_name = 'flash/user_study.html'
    context_object_name ='cards'
    #ordering = ['date_created'] #default, place a (-) infront of date to reverse
    paginate_by = 9
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        sub = self.kwargs.get('subject')
        if sub == 'All':
            return FCard.objects.filter(creator=user)
        else:
            return FCard.objects.filter(creator=user, subject=sub)
        print(user, sub)


class CardDetailView(DetailView):
    model = FCard
    
class CardCreateView(LoginRequiredMixin, CreateView):
    model = FCard
    fields = ['subject', 'question', 'answer'] #determines what fields to show on
    
    def form_valid(self, form):
        form.instance.creator = self.request.user #overides form validation to add in user as creator
        return super().form_valid(form)

class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #Update veiw needs to come last
    model = FCard
    fields = ['subject', 'question', 'answer'] #determines what fields to show on
    
    def form_valid(self, form):
        form.instance.creator = self.request.user #overides form validation to add in user as creator
        return super().form_valid(form)
    
    def test_func(self):
       fcard = self.get_object()
       if self.request.user == fcard.creator:
           return True
       return False
   
class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FCard
    success_url= '/'
    
    def test_func(self):
       fcard = self.get_object()
       if self.request.user == fcard.creator:
           return True
       return False