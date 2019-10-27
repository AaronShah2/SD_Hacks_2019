import re
from pytube import YouTube
import nltk
from nltk.corpus import wordnet


def retrieve_captions(url):
    """
    Returns the audio transcript, in the form of an array of
    strings in which each string is one sentence, of a YouTube video.
    The final character of each string is a standard period, ASCII 46.
    :param string url: URL of the YouTube video, the captions of which are retrieved.
    """
    source = Youtube(url)
    en_caption = source.captions.get_by_language_code('en')
    en_caption_convert_to_srt = en_caption.generate_srt_captions()
    en_caption_full_lines = en_caption_convert_to_srt.split('\n\n')

    num = 0
    en_caption_lines = []
    for full_line in en_caption_full_lines:
        num += 1
        i = 31 + len(str(num))
        en_caption_lines.append(full_line[i:] + ' ')

    en_caption_paragraph = ''
    for en_caption_line in en_caption_lines:
        en_caption_paragraph += en_caption_line
    en_caption_sentences = en_caption_paragraph.split('. ')
    for sentence in en_caption_sentences:
        sentence += '.'
    return en_caption_sentences


def filter_captions(captions, *keywords):
    """
    Returns an array of strings containing only the sentences in which the relevant keyword(s)
    or synonym(s) occurs at least a particular number of times in relation to the length of
    the sentences; the longer the sentence, the higher the minimum number of occurrences
    of said word(s) or synonym(s) for the sentence to be considered relevant.
    :param string[] captions: Audio transcript in the form of an array of strings.
    :param *args keywords: Keyword(s) which is (are) relevant for the user.
    """
    avg_len = 0
    num_sentences = 0
    for sentence in captions:
        avg_len += len(sentence)
        num_sentences += 1
    
    relevant_captions = []
    for keyword in keywords:
        kw = keyword.lower()
        for caption in captions:
            min_num_relevant_words = len(caption) / (2.5 * avg_len / num_sentences) + 1
            count = 0
            words = caption.split(' ')
            for word in words:
                w = re.sub(r'\W+', '', word).lower()
                w = re.sub(r'_+', ' ', w)

                synonyms = []
                for syn in wordnet.synsets(kw):
                    for l in syn.lemmas():
                        s = re.sub(r'\W+', '', l.name()).lower()
                        synonyms.append(re.sub(r'_+', ' ', s))

                if w == kw or w in synonyms:
                    count += 1
            
            if count >= min_num_relevant_words:
                if caption not in relevant_captions:
                    relevant_captions.append(caption)
            
    return relevant_captions

