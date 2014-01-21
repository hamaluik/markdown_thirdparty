"""
Module front-ends two somewhat divergent implementations of the
guess-language module--one for Python 2, one for Python 3. Provides
a unified interface to each.
"""

from guess_language import guessLanguageTag

def guess_language(text):
    """
    Given text, try to guess what natural lanuage it represents.
    NB, text needs to be plain text, not text wrapped in HTML. HTML
    tags will throw off recognition, suggesting 'en' when the content
    is clearly something else.
    """
    if text is None or text.strip() == "":
        return 'UNKNOWN'
    if len(text) < 40:
        # If the text is very short, replicate it before guessing at it
        return guessLanguageTag(''.join([text, ' '] * 6))
    else:
        return guessLanguageTag(text)
