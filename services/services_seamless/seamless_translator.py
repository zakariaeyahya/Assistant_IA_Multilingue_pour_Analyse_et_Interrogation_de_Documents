from transformers import AutoProcessor, SeamlessM4Tv2Model
import torch
import re
class SeamlessTranslator:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
        self.model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large").to(self.device)
    def clean_output(self, text):
        print("Début de la fonction clean_output...")
        cleaned_text = text.replace('</s>', '').strip()
        cleaned_text = re.sub(r'__\w+__\s*', '', cleaned_text)
        print("Fin de la fonction clean_output...")
        return cleaned_text

    def translate_text(self, text, src_lang, tgt_lang):
        inputs = self.processor(text=text, src_lang=src_lang, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, tgt_lang=tgt_lang, generate_speech=False)
        token_ids = outputs.sequences[0].cpu().tolist()
        translated_text = self.clean_output(self.processor.decode(token_ids))
        return translated_text