from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Item model
    """

    supplier = serializers.StringRelatedField() # This will show the name of the supplier instead of the id.

    class Meta:
        model = Item
        # For security reasons, uuid (i.e. id in our case) should NOT be included (exposed) in the serializer.
        # But in order to make it easier to use detail view I will expose it.
        # So that any tester can copy the uuid and use it to get the detail view.

        fields = '__all__'
        #fields = ('name', 'description', 'note', 'stock', 'availability', 'supplier', 'image')# A better way!
