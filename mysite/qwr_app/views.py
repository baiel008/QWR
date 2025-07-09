from .serializers import *
from rest_framework import viewsets, generics
from .models import *



class QuoteListAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteListSerializer


class QuoteCreateAPIView(generics.CreateAPIView):
    serializer_class = QuoteCreateSerializer


class ReactionCreateAPIView(generics.CreateAPIView):
    serializer_class = ReactionCreateSerializer