from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        #get all drinks
        drinks = Drinks.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinks, many=True)
        #get json
        return JsonResponse({'drinks': serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    