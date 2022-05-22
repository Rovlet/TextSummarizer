from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration

class Summarizer:
    def __init__(self):
        self.GPT2_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.GPT2_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.summarizer = pipeline('summarization')

    def summarize(self, document):
        tokenized_document = self.GPT2_tokenizer([document], max_length=300, truncation=True, return_tensors="pt")["input_ids"]
        input_shape = tokenized_document.shape
        outputs = self.GPT2_model.generate(tokenized_document, do_sample=False, max_length=500, num_beams=4,
                                 num_return_sequences=1, no_repeat_ngram_size=6, return_dict_in_generate=True,
                                 output_scores=True)
        candidate_sequences = outputs.sequences[:, input_shape[1]:]
        candidate_scores = outputs.sequences_scores.tolist()
        return candidate_sequences


summarizer = Summarizer()
