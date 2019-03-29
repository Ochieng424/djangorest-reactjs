from rest_framework import serializers
from .models import Lead


class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '_all_'
