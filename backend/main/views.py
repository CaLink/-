from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.decorators import send_some_analytics, logging
from rest_framework.parsers import JSONParser
from main.models import Car
from main.serializers import CarSerializer
from snatcher.main import main_func


# Мега Управление доступностью, которое я хз как иначе сделать
# Костыль для мега грязной функции
check = False

@csrf_exempt
@logging
@send_some_analytics
def car(request):
    if request.method == 'GET':
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print(serializer.errors)
        return HttpResponse(serializer.errors, status=400)

@logging
@send_some_analytics
def car_current(request, pk):
    car = Car.objects.filter(pk=pk)
    if len(car) != 1:
        return HttpResponse(status=404)
        #TODO: Лог ошибки много одного ключа
    car = car[0]
     
    if request.method == 'GET':
        serialize = CarSerializer(car)
        return JsonResponse(serialize.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        return JsonResponse(serialize.data)

    
    elif request.method == 'DELETE':
        car.delete()
        return HttpResponse(staus=200)

    else:
        return HttpResponse(status=404)

@logging
@send_some_analytics
def start_scrapping(request):
    global check
    if not check:
        check = True
        main_func()
        check = False
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

#TODO: Мб добавить логи

# Разбить модели на более сложную структуру
# Понять что мне вообще нужно и что парсить будем
# Добавить метод для поднятия парсера
# Научить парсер отправлять данные на бэк