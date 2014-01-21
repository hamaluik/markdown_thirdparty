# -*- coding: utf-8 -*-
"""
Markdown Third Party
============================

This plugin allows you to use various third-party
Markdown extensions to make writing posts in Markdown
easier and better.
"""

from pelican import signals, readers

import os, sys, inspect

class MarkdownThirdParty(readers.MarkdownReader):
	def __init__(self, *args, **kwargs):
		super(MarkdownThirdParty, self).__init__(*args, **kwargs)
		self.extensions = list(self.settings['MD_EXTENSIONS'])
		# always make sure we have the 'meta' extension
		if 'meta' not in self.extensions:
			self.extensions.append('meta')

		# add our current folder to the path so Markdown can find the extension
		cmdFolder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
		if cmdFolder not in sys.path:
			sys.path.insert(0, cmdFolder)

def addReader(readers):
	# re-route all markdown extensions to be our reader
	extensions = ['md', 'markdown', 'mkd', 'mdown']
	for ext in extensions:
		readers.reader_classes[ext] = MarkdownThirdParty

def register():
	signals.readers_init.connect(addReader)