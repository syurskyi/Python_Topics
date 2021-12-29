___ capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""


    end_characters = ['.','!','?'] 

    words =  text.s..

    
    first_word_after_end_of_sentence_index = 0
    ___ i,word __ enumerate(words):

        __ any(word.endswith(character) ___ character __ end_characters):
            words[first_word_after_end_of_sentence_index] = words[first_word_after_end_of_sentence_index].capitalize()
            first_word_after_end_of_sentence_index = i + 1 


    r.. ' '.join(words)
            















