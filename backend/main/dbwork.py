from .models import Car

def prettyCarSaver(ser):
    Car.objects.create(**ser.data)
    return True

def carList():
    return Car.objects.all()
