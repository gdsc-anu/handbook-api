from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import HandbookCategory, HandbookEntry
from .serializers import HandbookCategorySerializer, HandbookEntrySerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET', 'POST'])
def handbook(request):
    if request.method == 'GET':
        categories = HandbookCategory.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(categories, request)
        serializer = HandbookCategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

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

@api_view(['POST', 'GET'])
def entry(request):
    if request.method == 'GET':
        entries = HandbookEntry.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(entries, request)
        serializer = HandbookEntrySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = HandbookEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def category_entries(request, category_pk):
    if request.method == 'GET':
        entries = HandbookEntry.objects.filter(category=category_pk)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(entries, request)
        serializer = HandbookEntrySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        request.data['category'] = category_pk  # Attach category information to the entry data
        serializer = HandbookEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_entry_detail(request, category_pk, entry_pk):
    try:
        entry = HandbookEntry.objects.get(category=category_pk, pk=entry_pk)
    except HandbookEntry.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

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