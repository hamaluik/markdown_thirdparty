"""
An extension to Python Markdown that uses smartypants to provide typographically
nicer ("curly") quotes, proper ("em" and "en") dashes, etc.
"""

from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension
from mdx_smartypants.spants import smartyPants, Quotes
from namedentities import named_entities, numeric_entities, unicode_entities

entity_handling = {
    'named': named_entities,
    'numeric': numeric_entities,
    'unicode': unicode_entities,
    None : lambda x: x,
    'none': lambda x: x
}

class SmartypantsPost(Postprocessor):
    """
    The smartypants_mdx postprocessor does its heavy lifting here.
    """
    def __init__(self, *args, **kwargs):
        self.entities = (kwargs.get('entities', 'none') or 'none').lower()
        if self.entities not in entity_handling:
            raise ValueError("entities must be named, numeric, unicode, or none")
        self.entity_izer = entity_handling[self.entities]

    def run(self, text):
        # Must guess language here, before HTML markup added
        if Quotes.direction is None or not Quotes.direction_explicit:
            Quotes.configure_for_text(text)

        return self.entity_izer(smartyPants(text))

class SmartypantsExt(Extension):
    """
    Registers SmartypantsPost as a post processor.
    """
    def __init__(self, configs=None):
        self.configs = dict(configs)

    def extendMarkdown(self, md, md_globals):
        entities_desired = self.configs.get('entities', None)
        post = SmartypantsPost(md, entities=entities_desired)
        md.postprocessors.add('smartypants', post, '_end')

def makeExtension(configs=None):
    """
    Make the extension.
    """
    return SmartypantsExt(configs=configs)
