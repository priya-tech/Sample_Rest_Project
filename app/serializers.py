from rest_framework import serializers
from .models import UserModel

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=30)
#     email = serializers.EmailField(max_length=30)
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return UserModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
