from rest_framework import serializers
from .models import VolunteerOpportunity, Application, Donation, Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'about']

class VolunteerOpportunitySerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = VolunteerOpportunity
        fields = ['id', 'title', 'organization', 'description', 'is_remote', 'location']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'opportunity', 'applicant_name', 'applicant_email']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'organization', 'amount', 'donor_name', 'donor_email']
