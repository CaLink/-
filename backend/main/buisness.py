from .serializers import CarSerializer
from .translator import translate
from .dbwork import prettyCarSaver, carList

def postDirtyCar(serializer):
    try:

        ans = {}
        data = dict(serializer.data)

        for key, value in data.items():
            ans[key] = translate(key, value)
        carSerializer = CarSerializer(data=ans)
        if carSerializer.is_valid():
            if prettyCarSaver(carSerializer):
                return carSerializer.data
            else:
                return '200'
    except BaseException as e:
        print(e)

def getCar():
    data = CarSerializer(carList(), many=True)
    return data.data