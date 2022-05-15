from transformers import pipeline


class Summarizer:
    def __init__(self):
        self.summarizer = pipeline('summarization')

    def summarize(self, text):
        return self.summarizer(text)[0]['summary_text']


summarizer = Summarizer()
