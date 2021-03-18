from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from myapp.models import Myapp
from myapp.serializers.foods_serializer import FoodsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def food_list(request):
  if request.method == 'GET':
    foods = Myapp.objects.all()

    name = request.GET.get('name', None)
    if name is not None:
      foods = foods.filter(name__icontains=name)

    food_serializer = FoodsSerializer(foods, many=True)
    return JsonResponse(food_serializer.data, safe=False)


  elif request.method == 'POST':
    food_data = JSONParser().parse(request)
    food_serializer = FoodsSerializer(data=food_data)
    if food_serializer.is_valid():
      food_serializer.save()
      return JsonResponse(food_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(food_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, pk):
  try:
    food = Myapp.objects.get(pk=pk)
  except Myapp.DoesNotExist:
    return JsonResponse({'message': 'the food does not exist'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    food_serializer = FoodsSerializer(food)
    return JsonResponse(food_serializer.data)
  
  elif request.method == 'PUT':
    food_data = JSONParser().parse(request)
    food_serializer = FoodsSerializer(food, data=food_data)
    if food_serializer.is_valid():
      food_serializer.save()
      return JsonResponse(food_serializer.data)
    return JsonResponse(food_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    food.delete()
    return JsonResponse({'message': 'food was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
