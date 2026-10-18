from django.shortcuts import render
from rest_framework import viewsets
from .models import BookData
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='sciencefiction')
    serializer_class = BookSerializer

class HighFantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='highfantasy')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='mystery')
    serializer_class = BookSerializer

class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='historicalfiction')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='romance')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='biography')
    serializer_class = BookSerializer

class ScienceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='science')
    serializer_class = BookSerializer

class SelfHelpViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='selfhelp')
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='history')
    serializer_class = BookSerializer

class GraphicNovelViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='graphicnovel')
    serializer_class = BookSerializer