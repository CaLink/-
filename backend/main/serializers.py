from rest_framework import serializers
from main.models import Car

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(allow_null=True)
#     content = serializers.CharField(allow_null=True)
#     tags = serializers.CharField(allow_null=True)
#     dt = serializers.DateField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         [setattr(instance, k, v) for k, v in validated_data.items()]
#         instance.save()
#         return instance


class CarSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    sub_brand_name = serializers.CharField(allow_null=True)
    official_price = serializers.CharField(allow_null=True)
    fuel_form = serializers.CharField(allow_null=True)
    market_time = serializers.CharField(allow_null=True)
    engine_description = serializers.CharField(allow_null=True)
    energy_elect_max_power = serializers.CharField(allow_null=True)
    gearbox_description = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance
