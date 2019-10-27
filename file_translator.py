from translate import Translator

def translateFile(filename, lang):
    translator =Translator(to_lang =lang)
    try:
        rFile = open(filename, "r")
        wFile = open(filename[0:len(filename)-4] +"-"+ lang + filename[len(filename)-4: len(filename)], "w")
        for line in rFile:
            trans_text = translator.translate(line).encode("utf-8")
            wFile.write(trans_text)
        rFile.close()
        wFile.close() 
    except :
        print("File does not exist")

def translateSentence(sentence, lang):
    translator = Translator(to_lang = lang)
    return translator.translate(sentence).encode("utf-8")
