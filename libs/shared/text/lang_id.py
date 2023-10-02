from nltk.tag import CRFTagger
from nltk.tokenize import wordpunct_tokenize


class LangIdCRF:
    def __init__(self) -> None:
        self.model = CRFTagger()
        self.model.set_model_file("./static/model/lang_id.tagger")

    def tag(self, text):
        tokens = wordpunct_tokenize(text)
        tagged = self.model.tag(tokens)
        return tagged
