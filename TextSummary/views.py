from django.views.generic import TemplateView, CreateView, UpdateView
from django.http import JsonResponse
from .models import Text


class HomeView(TemplateView):
    title = 'Text summarization app'
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PostTextView(CreateView):
    title = 'Text summarization app'
    model = Text

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        text = request.POST.get('story')
        data = {'success': True, 'text': text}
        return JsonResponse(data)
