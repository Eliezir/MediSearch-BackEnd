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
    filters = request.GET.copy()
    limit = filters.pop('limit', 25) 
    page = filters.pop('page', 1)  
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

    medicines = Medicine.objects.filter(query)
    paginator = PageNumberPagination()
    paginator.page_size = limit
    result_page = paginator.paginate_queryset(medicines, request)
    serializer = MedicineSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

#url example for filters 

