from urllib import request
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])



def drink_list(request): 
    #get all the drinks
    #serlize them
    #retrun json
    if request.method == 'GET':

        drinks = Drink.objects.all()
        serializer =  DrinkSerializer(drinks,many=True)
        
        return JsonResponse({"drinks":serializer.data},safe=False)
    
    if request.method == 'POST':

        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOTFOUND)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass