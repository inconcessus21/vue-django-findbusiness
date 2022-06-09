from .models import Business, Categories
from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField


class BusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        lookup_field = 'uuid'
        

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    category = SlugRelatedField(slug_field="category_name", queryset=Categories.objects.all(),  many=True )

    class Meta:
        model = Business
        lookup_field = 'category__category_name'
        fields = '__all__'

class LocalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('business_name','uuid','localization',)





