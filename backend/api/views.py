from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Goodthing
from .serializers import GoodthingSerializer

class GoodthingViewSet(viewsets.ModelViewSet):
    queryset = Goodthing.objects.all()
    serializer_class = GoodthingSerializer
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        goodthing = self.get_object()
        goodthing.likes_count += 1
        goodthing.save()
        return Response({'likes_count': goodthing.likes_count})
    
    @action(detail=True, methods=['post'])
    def not_good(self, request, pk=None):
        goodthing = self.get_object()
        goodthing.not_good_count += 1
        goodthing.save()
        return Response({'not_good_count': goodthing.not_good_count})