from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('quote/', QuoteListAPIView.as_view(), name='quote_list'),
    path('quote/create/', QuoteCreateAPIView.as_view(), name='quote_create'),
    path('reaction/create/', ReactionCreateAPIView.as_view(), name='reaction_create'),
]