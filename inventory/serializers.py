from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Item model
    """

    supplier = serializers.StringRelatedField()  # This will show the name of the supplier instead of its id.

    class Meta:
        model = Item
        fields = ('name', 'supplier', 'availability')


class ItemSerializerFullView(serializers.ModelSerializer):
    """
    Serializer for Item model that shows all the fields except the id for security reasons.
    """

    supplier = serializers.StringRelatedField()  # This will show the name of the supplier instead of its id.

    class Meta:
        model = Item
        fields = ('name', 'supplier', 'availability', 'stock', 'description', 'note')
