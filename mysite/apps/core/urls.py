from django.urls import path

from . import views

urlpatterns = [
    # Dashboard page
    path('', views.DashboardView.as_view(), name='home'),
    path('cases', views.MyCasesView.as_view(), name='cases'),
    path('lawyers', views.LawyersView.as_view(), name='lawyers'),
    path('case-list', views.CasesListView.as_view(), name='case_list'),
    path('add-case', views.AddCaseView.as_view(), name='add_case'),
    path('my-client-list', views.MyClientListView.as_view(), name='my_client_list'),
]
