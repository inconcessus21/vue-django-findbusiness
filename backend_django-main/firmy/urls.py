from django.urls import path, include

from rest_framework.routers import DefaultRouter


from .views import AddBusinessView, CategoryViewSet, CategoriesViewSet, BusinessDetail ,LocalizationView

router = DefaultRouter()
router.register('businessdetail', BusinessDetail, basename='firma')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('category', CategoryViewSet, basename='category')
router.register('lokalizacje', LocalizationView, basename='lokalizacje')
router.register('addfirma', AddBusinessView, basename='addfirma')

urlpatterns = [
    path('', include(router.urls)),
]