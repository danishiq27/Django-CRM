from django.urls import path
from .views import (leads,lead_detail,lead_create,lead_update,
 lead_delete,LeadListView,LeadDetailView,LeadCreateView, LeadUpdateView, LeadDeleteView)

app_name= "leads"
urlpatterns= [
    path('', LeadListView.as_view(), name='leads'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('create/',LeadCreateView.as_view(), name='lead-create'),
]