from django.views.generic import TemplateView, CreateView, UpdateView
from django.http import JsonResponse
from summarize import summarizer


class HomeView(TemplateView):
    title = 'Text summarization app'
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PostTextView(CreateView):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('story')
        make_summary_using_loop_model = request.POST.get('loop')

        print("Processing started...", flush=True)
        if make_summary_using_loop_model == "loop":
            summary = summarizer.summarize_using_loop_model(text)
        else:
            summary = summarizer.summarize_using_bert(text)
        data = {'success': True, 'summary': summary}
        return JsonResponse(data)
