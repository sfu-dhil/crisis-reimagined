import json
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Response, Config
from .serializers import ResponseSerializerPolymorphicSerializer
# Create your views here.

@cache_page(settings.CACHE_SECONDS)
def home(request):
    responses = Response.objects.filter(status=Response.Status.APPROVED)

    return render(request, 'index.html', {
        'responses_json': json.dumps(ResponseSerializerPolymorphicSerializer(responses, many=True).data),
        'config_json': json.dumps({
            'responses_enabled': Config.get_solo().responses_enabled,
            'git_repo_link': f"{settings.GIT_REPO}/tree/{settings.GIT_TAG if settings.GIT_TAG else settings.GIT_COMMIT}",
            'git_repo_link_text': f"GitHub{' ' + settings.GIT_TAG if settings.GIT_TAG else ''}",
        }),
    })