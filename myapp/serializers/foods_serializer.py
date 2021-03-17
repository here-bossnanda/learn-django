from rest_framework import serializers
from myapp.models import Myapp

class FoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Myapp
    fields = ('id', 'name', 'asal')
