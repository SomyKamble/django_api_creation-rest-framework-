from rest_framework import serializers
from .models import sampleweb

class samplewebSerailizers(serializers.ModelSerializer):

    class Meta:
        model =sampleweb
        fields = '__all__'#for all fields

