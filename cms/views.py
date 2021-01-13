from django.db import models
# from config.settings.common import LOGIN_REDIRECT_URL
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)

from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import QuestionAndAnswer

from .judge_the_answer import judge_the_answer

UserModel = get_user_model()


class TopView(TemplateView):
    template_name = 'cms/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'cms/login.html'

class Logout(LogoutView):
    pass

class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signup.html'
    success_url = reverse_lazy('cms:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class UserUpdate(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'cms/user_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

class UserDetail(OnlyYouMixin, DetailView):
    model = UserModel
    template_name = 'cms/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class UserList(ListView):
    model = UserModel
    template_name = 'cms/user_list.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = UserModel
    template_name = 'cms/user_delete.html'
    success_url = reverse_lazy('cms:top')

class QuestionList(LoginRequiredMixin, ListView):
    model = QuestionAndAnswer
    template_name = 'cms/question_list.html'
    login_url = '/login/'

class QuestionDetail(LoginRequiredMixin, DetailView):
    model = QuestionAndAnswer
    template_name = 'cms/question_detail.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        text = request.POST['text']
        ans = request.POST['answer'].strip()
        score = judge_the_answer(text, ans)
        if score > 0:
            pass
        else:
            score = 0
            
        context = {
            'text': text.strip(), 
            'answer': ans,
            'result': score
            }

        return render(request, 'cms/question_detail.html', context)
class Home(LoginRequiredMixin, TemplateView):
    model = UserModel
    template_name = 'cms/home.html'
    login_url = '/login/'