from rest_framework import serializers
from client.models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url','id','roll','name', 'college')
