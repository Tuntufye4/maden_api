from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
     
    def get_queryset(self):    
        queryset = Document.objects.all()
        # Dynamic filtering: only apply filters that exist
        for field in ['document_type','file_url']:   
            value = self.request.query_params.get(field)
            if value:
                queryset = queryset.filter(**{f"{field}__iexact": value})
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
