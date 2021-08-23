from rest_framework import serializers
from blog.models import Transactions

class Transactserializers(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'
        