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
def category_detail(request, pk):
    try:
        category = HandbookCategory.objects.get(pk=pk)
    except HandbookCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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
        return Response('Handbook Category deleted successfully')
    
@api_view(['POST', 'GET'])
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
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def entry_detail(request, pk):
    try:
        entry = HandbookEntry.objects.get(pk=pk)
    except HandbookEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
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
        return Response('Handbook deleted successfully')
    
