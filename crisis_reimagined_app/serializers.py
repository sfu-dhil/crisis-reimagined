from rest_framework import serializers
from polymorphic.contrib.drf.serializers import PolymorphicSerializer

from .models import Response, \
    KnowledgeResponse, RestitutionResponse, TechnologyResponse, \
    GeopoliticsResponse, MarketizationResponse, MassificationResponse

# PolymorphicSerializers
class KnowledgeResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class RestitutionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestitutionResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class TechnologyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class GeopoliticsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeopoliticsResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class MarketizationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketizationResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class MassificationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassificationResponse
        fields = ['id', 'year', 'question_1', 'question_2']

class ResponseSerializerPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Response: None,
        KnowledgeResponse: KnowledgeResponseSerializer,
        RestitutionResponse: RestitutionResponseSerializer,
        TechnologyResponse: TechnologyResponseSerializer,
        GeopoliticsResponse: GeopoliticsResponseSerializer,
        MarketizationResponse: MarketizationResponseSerializer,
        MassificationResponse: MassificationResponseSerializer,
    }

    # needed for default/empty set
    class Meta:
        model = Response
        fields = ['id']