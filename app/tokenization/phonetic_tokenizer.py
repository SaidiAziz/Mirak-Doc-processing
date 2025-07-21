import re

import unicodedata
from nltk import word_tokenize
import soundex

# nltk.download('punkt')


french_soundex = soundex.Soundex()
english_soundex = soundex.Soundex()


# Import necessary libraries
def tokenize_text(text):
    """
    Tokenizes the input text into words.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokens (words).
    """
    tokens = word_tokenize(text)
    return tokens  # Print the tokens for debugging purposes


def remove_accents(text):
    """Normalize French diacritics to base characters"""
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd_form if not unicodedata.combining(c))


def phonetic_tokenization(text):
    """
    Convert text to Soundex phonetic tokens with French optimization
    Handles mixed-language documents and preserves critical numbers
    """
    # Text normalization pipeline
    text = text.lower()  # Case normalization
    text = remove_accents(text)  # Diacritic removal
    text = re.sub(r'[^\w\s]', '', text)  # Punctuation removal

    # Tokenize with French context
    tokens = word_tokenize(text, language='french')

    phonetic_tokens = []
    for token in tokens:
        if not token:
            continue

        # Number preservation (critical for invoices/IDs)
        if token.isdigit():
            phonetic_tokens.append(token)
            continue

        # Mixed token handling (e.g., "REF-2023")
        if any(char.isdigit() for char in token):
            phonetic_tokens.append(token)
            continue

        # Language detection heuristic
        is_french = any(char in 'àâäéèêëîïôöùûüç' for char in token.lower())

        try:
            # Apply appropriate Soundex variant
            code = french_soundex.soundex(token) if is_french \
                else english_soundex.soundex(token)

            # Handle Soundex's 4-character fixed length
            phonetic_tokens.append(code)
        except Exception as e:
            print(f"Tokenization error for '{token}': {str(e)}")
            phonetic_tokens.append(token)  # Fallback to original

    return phonetic_tokens
