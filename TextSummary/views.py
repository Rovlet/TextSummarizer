from django.views.generic import TemplateView, CreateView, UpdateView
from django.http import JsonResponse
from summarize import summarizer
import os

class HomeView(TemplateView):
    title = 'Text summarization app'
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PostTextView(CreateView):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('story')
        model_type = request.POST.get('model_selection')
        summary = str()
        scores = list()
        metric = ['rouge1', 'rougeL']


        print("Processing started...", flush=True)
        if model_type == "loop":
            summary, scores = summarizer.summarize_using_loop_model(text, metric)
            
        elif model_type == "bart":
            summary, scores = summarizer.summarize_using_bert(text, metric)

        elif model_type == "t5":
            summary, scores = summarizer.summarize_using_t5(text, metric)

        data = {'success': True, 'summary': summary, 'rouge_score': scores}
        return JsonResponse(data)
