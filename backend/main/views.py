from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from main.decorators import send_some_analytics, logging
from rest_framework.parsers import JSONParser
from main.models import Car
from main.serializers import CarSerializer, DirtyCarSerializer
from snatcher.main import main_func
from rest_framework.decorators import api_view, schema, APIView
from rest_framework.schemas import AutoSchema
from drf_spectacular.utils import extend_schema
from .dirtyCar import DirtyCar
from .buisness import postDirtyCar, getCar


# Мега Управление доступностью, которое я хз как иначе сделать
# Костыль для мега грязной функции
check = False


#@logging
#@send_some_analytics

class CarList(APIView):
    
    @extend_schema(summary="Получить все машинки",
                   responses={200: CarSerializer},)
    @logging
    @send_some_analytics
    def get(self, request):
        if request.method == 'GET':
            data = getCar()
            return JsonResponse(data, safe=False)
    
    @extend_schema(summary="Добавить новую машинку",
                   request=DirtyCarSerializer,
                   responses={201: CarSerializer},)
    @logging
    @send_some_analytics
    def post(self, request):    
        if request.method == 'POST':
            data = request.data
            serializer = DirtyCarSerializer(data=data)
            if serializer.is_valid():
                data = postDirtyCar(serializer)
            return JsonResponse(data)

class CarDetail(APIView):

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist: 
            raise Http404

    @extend_schema(summary="Получить конкретную машинку",
                   responses={200: CarSerializer},)
    @logging
    @send_some_analytics
    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    @extend_schema(summary="Обновить конкретную машинку",
                   request=DirtyCarSerializer,
                   responses={201: CarSerializer},)
    @logging
    @send_some_analytics
    def put(self, request, pk):
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            car = self.get_object(pk)
            serializer = CarSerializer(car, data=data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(serializer.data)

    @extend_schema(summary="Удалить конкретную машинку",
                   request=DirtyCarSerializer,)
    @logging
    @send_some_analytics
    def delete(self, request, pk):
        if request.method == 'DELETE':
            car = self.get_object(pk)
            car.delete()
            return HttpResponse('Delete Done', status=200)
        
@api_view(['GET'])
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
        return HttpResponse("Занято",status=400)