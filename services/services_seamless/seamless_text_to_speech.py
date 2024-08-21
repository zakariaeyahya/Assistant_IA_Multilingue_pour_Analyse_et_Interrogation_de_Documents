from transformers import AutoProcessor, SeamlessM4Tv2Model
import torch

class SeamlessTextToSpeech:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
        self.model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large").to(self.device)

    def text_to_speech(self, text, tgt_lang):
        inputs = self.processor(text=text, src_lang="fra", return_tensors="pt").to(self.device)
        with torch.no_grad():
            audio_array = self.model.generate(**inputs, tgt_lang=tgt_lang)[0].cpu().numpy().squeeze()
        return audio_array