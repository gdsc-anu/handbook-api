from rest_framework import serializers
from .models import HandbookCategory, HandbookEntry

class HandbookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookCategory
        fields = ['name', 'slug']

class HandbookEntrySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=HandbookCategory.objects.all())

    class Meta:
        model = HandbookEntry
        fields = [ 'category', 'title', 'content', 'slug', 'image', 'video', 'attachment']

    def create(self, validated_data):
        category_slug = validated_data.pop('category')
        category = HandbookCategory.objects.get(slug=category_slug)
        entry = HandbookEntry.objects.create(category=category, **validated_data)
        return entry

    def update(self, instance, validated_data):
        category_slug = validated_data.pop('category', None)
        if category_slug:
            category = HandbookCategory.objects.get(slug=category_slug)
            instance.category = category

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
