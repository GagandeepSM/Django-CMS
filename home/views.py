from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Content
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

dummy_content = [
	{
		'author' : 'Gagandeep',
		'title'	 : 'My first post',
		'body': 'Here for Ajackus!',
		'summary': 'I am in summary'

	},
	{
		'author' : 'Gagandeep',
		'title'	 : 'My second post',
		'body': 'Here for Ajackus second time!',
		'summary' : 'I am in summary 2'
	}
]


# Create your views here.
def home_page(request):
	context = {
		'posts' : Content.objects.all()
	}
	return render(request, 'home/home.html', context)


def about_page(request):
	context = {
		'title' : 'About'
	}
	return render(request, 'home/about.html', context)

class ContentListView(ListView):
	model = Content
	template_name = 'home/home.html'
	context_object_name = 'posts'
	paginate_by = 3

class UserContentListView(ListView):
	model = Content
	template_name = 'home/user_content.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username= self.kwargs.get('username'))
		return Content.objects.filter(author=user)


class ContentDetailView(DetailView):
	model = Content


class ContentCreateView(LoginRequiredMixin, CreateView):
	model = Content
	fields = ['title', 'body', 'summary']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Content
	fields = ['title', 'body', 'summary']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class ContentDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Content	
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False