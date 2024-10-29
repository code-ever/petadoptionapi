from django.shortcuts import render
from .models import Category, Subcategory,Uploadpets,Contact,User,Profile
from .serializer import CategorySerializer, SubcategorySerializer, ProductSerializer,ContactSerializer,UserSerializer
from rest_framework import mixins, viewsets
from rest_framework.response import Response
# Create your views here.
   
class ProductView(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Uploadpets.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
# releted products
class ReletedView(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Uploadpets.objects.order_by('?')[:5]
    serializer_class = ProductSerializer
    

class SubCategoryView(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Subcategory.objects.order_by('?')[:5]
    serializer_class = SubcategorySerializer
    lookup_field = 'id'
    
class AllCatigoryview(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = Subcategory.objects.order_by('?')
    serializer_class = SubcategorySerializer

class CategoryView(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class EachCategoryView(viewsets.ViewSet):
    def retrieve(self, Request, pk=None):
        queryset = Uploadpets.objects.filter(subcategory=pk)
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    

class ContactView(viewsets.GenericViewSet, mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer