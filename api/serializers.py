from rest_framework import serializers
from .models import HandbookCategory, HandbookEntry

class HandbookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookCategory
        fields = ['id', 'name', 'slug']  # Only include necessary fields for serialization

class HandbookEntrySerializer(serializers.ModelSerializer):
    category = HandbookCategorySerializer()  # Use nested serializer for category field

    class Meta:
        model = HandbookEntry
        fields = ['id', 'category', 'title', 'content', 'image', 'video', 'attachment']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = HandbookCategory.objects.get_or_create(**category_data)[0]
        entry = HandbookEntry.objects.create(category=category, **validated_data)
        return entry

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category = HandbookCategory.objects.get_or_create(**category_data)[0]
            instance.category = category

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
