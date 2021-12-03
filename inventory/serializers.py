from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Item model
    """

    supplier = serializers.StringRelatedField()  # This will show the name of the supplier instead of its id.

    class Meta:
        model = Item
        fields = ('id','name', 'supplier', 'availability')
