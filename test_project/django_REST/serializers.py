# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import AccountModel

# Create a model serializer
class AccountSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = AccountModel
		fields = ('title', 'description')
