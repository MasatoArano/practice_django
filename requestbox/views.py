from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReqCreateForm
from .models import Req
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'requestbox/top.html'

class AddView(generic.CreateView):
    model = Req
    form_class = ReqCreateForm
    success_url = reverse_lazy('requestbox:index')

class Mypage(LoginRequiredMixin, generic.ListView):
    model = Req
    login_url = '/admin/'
    paginate_by = 10

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Req
    success_url = reverse_lazy('requestbox:mypage')
