___ capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""


    end_characters = ['.','!','?'] 

    words =  text.split()

    
    first_word_after_end_of_sentence_index = 0
    for i,word in enumerate(words):

        __ any(word.endswith(character) for character in end_characters):
            words[first_word_after_end_of_sentence_index] = words[first_word_after_end_of_sentence_index].capitalize()
            first_word_after_end_of_sentence_index = i + 1 


    return ' '.join(words)
            















