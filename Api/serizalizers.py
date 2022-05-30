from rest_framework import serializers
from Links.models import Link

#not in use :(
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        
#serializer for data getting in req 
class PostLinkSerizalizer(serializers.Serializer):
    url = serializers.CharField()