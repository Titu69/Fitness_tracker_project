from rest_framework import serializers
from .models import Profiles_mongo_data
class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles_mongo_data
        fields='__all__' 