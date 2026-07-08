
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import BasePermission
from rest_framework.renderers import JSONRenderer

from .serializers import ResponseSerializerPolymorphicSerializer
from .models import Response, Config

class ResponsesEnabled(BasePermission):
    def has_permission(self, request, view):
        return Config.get_solo().responses_enabled

class ResponseApiView(CreateModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Response.objects.filter(status=Response.Status.APPROVED).all()
    serializer_class = ResponseSerializerPolymorphicSerializer
    permission_classes = [ResponsesEnabled]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

router = DefaultRouter(use_regex_path=False, trailing_slash=False)
router.register('responses', ResponseApiView)