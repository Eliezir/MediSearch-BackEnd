from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Medicine
from .serializers import MedicineSerializer
from django.db.models import Q



#get medicines with a limit and pagination

@api_view(['GET'])
def get_medicines(request):
    class CustomPagination(PageNumberPagination):
        page_size_query_param = 'limit'  
    paginator = CustomPagination()
    limit = request.GET.get('limit', 25)
    medicines = Medicine.objects.all()
    result_page = paginator.paginate_queryset(medicines, request)
    serializer = MedicineSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)




#filters for medicines

@api_view(['GET'])
def filter_medicines(request):
    print(request.META.get('HTTP_ORIGIN'))
    filters = request.GET.dict()
    limit = request.GET.get('limit', 25) 
    query = Q()
    for key, value in filters.items():
        if '__' in key:
            field, operation = key.split('__', 1)
            if operation == 'ne':
                query &= ~Q(**{field: value})
            else:
                query &= Q(**{key: value})
        else:
            query &= Q(**{key: value})
    medicines = Medicine.objects.filter(query)[:limit]
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)

def filter_medicines(request):
    class CustomPagination(PageNumberPagination):
        page_size_query_param = 'limit'  
    paginator = CustomPagination()
    include_filter = request.GET.get('include', None)
    limit = request.GET.get('limit', 25)
    if include_filter is not None:
        medicines = Medicine.objects.filter(your_field__in=include_filter)
    else:
        medicines = Medicine.objects.all()
    result_page = paginator.paginate_queryset(medicines, request)
    serializer = MedicineSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
