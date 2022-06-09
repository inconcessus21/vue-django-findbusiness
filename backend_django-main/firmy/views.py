from django.shortcuts import render
from .serializer import CategoriesSerializer, CategorySerializer, BusinessDetailSerializer, LocalizationSerializer
from rest_framework import viewsets
from .models import Business, Categories
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response

@permission_classes([AllowAny])
class BusinessDetail(viewsets.ModelViewSet):
    serializer_class = BusinessDetailSerializer
    queryset = Business.objects.all()
    lookup_field = 'uuid'


@permission_classes([AllowAny])
class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

@permission_classes([AllowAny])
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Business.objects.all()
    lookup_field = 'category__category_name'

    def get_queryset(self, *args, **kwargs):
        context = super().get_queryset(*args, **kwargs)
        tmp_cat = self.kwargs.get("category__category_name")
        context =  self.queryset.all().filter(category__category_name=tmp_cat) 
      
        return context

    def retrieve(self, request, *args, **kwargs): # Change is here <<
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)


@permission_classes([AllowAny])
class LocalizationView(viewsets.ModelViewSet):
    serializer_class = LocalizationSerializer
    queryset = Business.objects.all()
    


class AddBusinessView(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Business.objects.all()


    def create(self, request):
        data = request.data
        business_name = data.get('businessName')
        description = data.get('description')
        city = data.get('city')
        www = data.get('www')
        phone_number = data.get('phoneNumber')
        email = data.get('email')
        category = data.get('category')
        image = data.get('image')
     
        temp = Business.objects.create(business_name=business_name, image=image, description=description, city=city, website=www, phone=phone_number, email=email)
        temp.category.add(category)
        return Response(data = {'message': ' Project created'})