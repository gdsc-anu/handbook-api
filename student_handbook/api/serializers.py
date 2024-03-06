from rest_framework import serializers
from .models import HandbookCategory, HandbookEntry

class HandbookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookCategory
        fields = '__all__'

class HandbookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookEntry
        fields = '__all__'
