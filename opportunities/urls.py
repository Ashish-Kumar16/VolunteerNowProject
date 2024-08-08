from django.urls import path
from .views import VolunteerOpportunityListCreate, ApplicationCreate, DonationCreate, OrganizationListCreate

urlpatterns = [
    path('organizations/', OrganizationListCreate.as_view(), name='organization-list-create'),
    path('opportunities/', VolunteerOpportunityListCreate.as_view(), name='volunteer-opportunity-list-create'),
    path('applications/', ApplicationCreate.as_view(), name='application-create'),
    path('donations/', DonationCreate.as_view(), name='donation-create'),
]