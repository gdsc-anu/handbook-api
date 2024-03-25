from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HandbookCategory, HandbookEntry
from .serializers import HandbookCategorySerializer, HandbookEntrySerializer

@api_view(['GET', 'POST'])
def handbook(request):
    if request.method == 'GET':
        categories = HandbookCategory.objects.all()
        serializer = HandbookCategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HandbookCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, slug):
    try:
        category = HandbookCategory.objects.get(slug=slug)
    except HandbookCategory.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HandbookCategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HandbookCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'detail': 'Handbook Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def entry(request):
    if request.method == 'GET':
        entries = HandbookEntry.objects.all()
        serializer = HandbookEntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HandbookEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def category_entries(request, category_slug):
    try:
        category = HandbookCategory.objects.get(slug=category_slug)
    except HandbookCategory.DoesNotExist:
        return Response({'detail': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        entries = HandbookEntry.objects.filter(category=category)
        serializer = HandbookEntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['category'] = category.id  # Attach category ID to the entry data
        serializer = HandbookEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_entry_detail(request, category_slug, entry_slug):
    try:
        category = HandbookCategory.objects.get(slug=category_slug)
        entry = HandbookEntry.objects.get(category=category, slug=entry_slug)
    except HandbookCategory.DoesNotExist:
        return Response({'detail': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
    except HandbookEntry.DoesNotExist:
        return Response({'detail': 'Entry not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HandbookEntrySerializer(entry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HandbookEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response({'detail': 'Handbook entry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
