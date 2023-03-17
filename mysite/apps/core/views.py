from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView
from core.forms import NewCaseForm
from core.models import Case
from django.db.models import Q

# Create your views here.


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView, ListView):
    ''' Dashboard View '''
    model = Case
    template_name = 'core/dashboard.html'
    context_object_name = 'cases'


@method_decorator(login_required, name='dispatch')
class MyCasesView(TemplateView):
    template_name = 'core/cases.html'


@method_decorator(login_required, name='dispatch')
class LawyersView(ListView):
    model = User
    template_name = 'core/lawyers.html'
    context_object_name = 'lawyers'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_info__user_type="Lawyer")
        queryset = queryset.exclude(id=self.request.user.id)
        return queryset


@method_decorator(login_required, name='dispatch')
class AddCaseView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewCaseForm
    template_name = 'core/add_cases.html'
    success_url = '/'
    success_message = 'Your Case Added Successfully!'
    extra_context = {'value': 'Add'}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.save(commit=False)
        form.instance.user_name = self.request.user
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


@method_decorator(login_required, name='dispatch')
class CasesListView(ListView):
    model = Case
    template_name = 'core/cases_list.html'
    context_object_name = 'cases'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(client=self.request.user) | Q(lawyer=self.request.user))
        return queryset


@method_decorator(login_required, name='dispatch')
class MyClientListView(ListView):
    model = User
    template_name = 'core/my_client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(client_cases__lawyer=self.request.user)
        return queryset
