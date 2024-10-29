from .models import Uploadpets,Category,Subcategory
from rest_framework import routers
from django.urls import path,include
from .views import CategoryView, SubCategoryView, ProductView,EachCategoryView,ContactView,ReletedView,Allpets

router = routers.SimpleRouter()

router.register('category', CategoryView, basename='category')
router.register('subcategory', SubCategoryView, basename='subcategory')
router.register('prductView', ProductView, basename='prductView')
router.register('eachCategoryView',EachCategoryView,basename='eachCategoryView')
router.register('contact',ContactView,basename='contact')
router.register('reletedprduct',ReletedView,basename='reletedprduct')
router.register('allpets',Allpets,basename='allpets')


urlpatterns = [
    path('',include(router.urls))
]
 