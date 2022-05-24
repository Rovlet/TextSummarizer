from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

class Summarizer:
    def __init__(self):
        self.loop_model = GPT2LMHeadModel.from_pretrained("philippelaban/summary_loop46")
        self.loop_tokenizer = GPT2TokenizerFast.from_pretrained("philippelaban/summary_loop46")

        self.bart_model = BartForConditionalGeneration.from_pretrained("ainize/bart-base-cnn")
        self.bart_tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/bart-base-cnn")

    def summarize_using_loop_model(self, document):
        tokenized_document = self.loop_tokenizer([document], max_length=300, truncation=True, return_tensors="pt")[
            "input_ids"]
        input_shape = tokenized_document.shape
        outputs = self.loop_model.generate(tokenized_document, do_sample=False, max_length=500, num_beams=4,
                                           num_return_sequences=1, no_repeat_ngram_size=6, return_dict_in_generate=True,
                                           output_scores=True)
        candidate_sequences = outputs.sequences[:,
                              input_shape[1]:]  # Remove the encoded text, keep only the summary
        candidate_scores = outputs.sequences_scores.tolist()

        for candidate_tokens, score in zip(candidate_sequences, candidate_scores):
            summary = self.loop_tokenizer.decode(candidate_tokens)
            return summary[:summary.index("END")]

    def summarize_using_bert(self, document):
        input_ids = self.bart_tokenizer.encode(document, return_tensors="pt")
        summary_text_ids = self.bart_model.generate(
            input_ids=input_ids,
            bos_token_id=self.bart_model.config.bos_token_id,
            eos_token_id=self.bart_model.config.eos_token_id,
            length_penalty=2.0,
            max_length=142,
            min_length=56,
            num_beams=4,
        )
        print(summary_text_ids[0], flush=True)
        return self.bart_tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)




summarizer = Summarizer()
