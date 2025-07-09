from .models import *
from rest_framework import serializers


class QuoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'



class ReactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'



class QuoteListSerializer(serializers.ModelSerializer):
    get_reaction_counts = serializers.SerializerMethodField()
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'get_reaction_counts']


    def get_reaction_counts(self, obj):
        return obj.get_reaction_counts()