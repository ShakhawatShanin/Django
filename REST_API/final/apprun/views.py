from rest_framework import viewsets
from .serializers import ClassifierSerializer
from .models import Classifier

# Create your views here.
class ClassifierViewSet(viewsets.ModelViewSet):
    queryset = Classifier.objects.all().order_by('-date_uploaded')
    serializer_class = ClassifierSerializer