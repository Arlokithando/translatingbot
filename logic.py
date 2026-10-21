# Görev #3
from collections import defaultdict
from translate import Translator
# Görev #5

class TextAnalysis():   
    
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "tr", "en")

        # Görev #6
        self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            cevirmen= Translator(from_lang=from_lang, to_lang=to_lang)
            ceviri= cevirmen.translate(text)
            return ceviri
        except:
            return "Çeviri girişimi başarısız oldu"




