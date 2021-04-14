from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    stdid = serializers.IntegerField()
    stdName = serializers.CharField(max_length=100)
    stdGrade = serializers.CharField(max_length=10)
    stdRest = serializers.CharField(max_length=10)
