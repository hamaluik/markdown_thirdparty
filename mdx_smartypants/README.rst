
<!-- saved from url=(0101)https://bitbucket.org/jeunice/mdx_smartypants/raw/3894e71c987bf0b554c1bf5a628c19fd045fd6f2/README.rst -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">Markdown is great, but if you want pretty "curled" quotes, real em- and
en-dashes, and the other typographic prettification that our modern Unicode- and
Web-savvy world affords, it needs to be married with ``smartypants`` (or an
equivalent module) to turn ugly, programmer-ish punctuation into pretty
typographic punctuation. This module does that.

Usage
=====

::

    import markdown

    text = """
    Markdown makes HTML from simple text files. But--it lacks typographic
    "prettification." That... That'd be sweet. Definitely 7---8 on a '10-point
    scale'. Now it has it.

    Huzzah!
    """

    print markdown.markdown(text, extensions=['smartypants(entities=named)'])

This produces nice HTML output, including typographically "pretty" quotes and
other punctuation. It also (optionally) renders HTML entities in their named rather than
numeric form, which is easier on the eyes and more readily comprehended::

    &lt;p&gt;Markdown makes HTML from simple text files. But&amp;mdash;it lacks
    typographic &amp;ldquo;prettification.&amp;rdquo; That&amp;hellip; That&amp;rsquo;d be
    sweet. Definitely 7&amp;ndash;8 on a &amp;lsquo;10-point scale&amp;rsquo;. Now it has
    it.&lt;/p&gt;
    &lt;p&gt;Huzzah!&lt;/p&gt;

Note that you don't really need to do an ``import mdx_smartypants``.
You're welcome to if you like, and it may help to advertise that the code
depends on ``mdx_smartypants`` being available. But ``markdown`` will
look for ``mdx_smartypants`` simply
by virtue of the ``extensions=['smartypants']`` declaration.

``mdx_smartypants`` will not massage code blocks (either indentded or fenced), or
HTML included within ``&lt;pre&gt;`` sections, so your
program snippets are safe.

RTL Languages and Alternative Quotation Marks
=============================================

`Right-to-left languages &lt;http://en.wikipedia.org/wiki/Right-to-left&gt;`_ such as
Arabic, Hebrew, Persian, and Urdu reverse the convention seen in English and
other left-to-right languages. The "left" quotation mark is really the
"starting" quotation mark--and it should appear to the right of the "right"
quotation mark. The "right" quotation mark, similarly, is really the "ending"
mark, and appears to the left of the "right" mark. This is clearly not something
that was front-and-center even to the internationally-minded Unicode community,
given how "left" and "right" are embedded in the official glyph names--a
misnomer that carries over into HTML entities.

The historical ``smartypants`` module similarly thinks in LTR terms. It even
hard-codes the HTML entities used for quotation marks. To address this, this
module's bundled ``spants`` derivative uses variable quotation marks, and
provides a middleman class ``Quotes`` which allows defining which HTML entities
should be used for starting single, ending single, starting double, and ending
double quotation marks, respectively. It also provides a mechanism for defining
the directionality of text. When emitting for RTL languages, the normal
left/right conventions are reversed.

``Quotes.set(ssquo, esquo, sdquo, edquo, dir)`` allows you to set one or more of
these values. If you are changing the direction of quoting  away from LTR, it's
best to redefine all of the quotes so that everything is consistently defined and
ordered.

``Quotes.reset()`` puts everything back to factory defaults. Perhaps most
usefully, ``Quotes.configure_for_text(text)`` guesses what direction the
language is rendered, and sets quotes accordingly. In order to provide a
fire-and-forget experience, unless the user sets the language direction
explicitly, this heuristic will be invoked as a normal part of
``mdx_smartypants`` operation. Also note: If called directly, this API must be
provided pure, plain text--not text wrapped in HTML or other markup (which will
fool the language guesser into improperly guessing English). If the user has
explicitly set language direction, the guess will not be made--but an optional
``force`` Boolean parameter can be supplied to specify that previous explicit
direction setting should be ignored, and guessing commenced.

This API and functionality is brand new; tests have been added and successfully
passed for it, but it should be considered somewhat experimental for now.


.. |lsquo| unicode::  U+2018 .. left single quote
    :trim:
.. |rsquo| unicode::  U+2019 .. right single quote
    :trim:
.. |ldquo| unicode::  U+201C .. left double quote
    :trim:
.. |rdquo| unicode::  U+201D .. right double quote
    :trim:
.. |laquo| unicode::  U+00AB .. left angle quote  / guillemet
    :trim:
.. |raquo| unicode::  U+00BB .. right angle quote / guillemet
    :trim:
.. |lasquo| unicode:: U+2039 .. left single angle quote
    :trim:
.. |rasquo| unicode:: U+203A .. right single angle quote
    :trim:
.. |bdquo| unicode::  U+201E .. low double quote
    :trim:
.. |sbquo| unicode::  U+201A .. low single quote
    :trim:
.. |space| unicode::  U+0020 .. space


Digging even deeper, `a great variety and vast diversity of different
quotation styles &lt;https://en.wikipedia.org/wiki/Non-English_usage_of_quotation_marks&gt;`_
are used in different languages. While there is no automatic support
for styles that differ from English, ``Quotes.set`` can be called
with any HTML entities,
allowing pretty much any convention to be supported. For example::

    Quotes.set(r'&amp;lasquo;', r'&amp;rasquo;', r'&amp;laquo;', r'&amp;raquo;')  # Swiss French
    Quotes.set(r'&amp;sbquo;',  r'&amp;lsquo;',  r'&amp;bdquo;', r'&amp;ldquo;')  # German or Czech

For |space| |laquo| Swiss |raquo| |space| and
|space| |lasquo| French |rasquo| |space| (first one)
and |space| |bdquo| German |ldquo| |space| and
|space| |sbquo| Czech |lsquo| |space| (second one).

**NB** I do not have any experience with RTL, top-to-bottom languages such as
traditional Chinese and Japanese scripts. If additional changes are required to
properly support that directionality, I'd be happy to hear about it.

Entities
========

Originally ``mdx_smartypants`` output named HTML entities. That behavior is
now configurable. By default, Unicode characters and entities are not
changed from whatever ``markdown`` emits. But you can choose that non-ASCII
characters are mapped to ``named`` entities, ``numeric`` entities, ``unicode``
entities (really not entities, just Unicode characters), or ``None`` (no
mapping performed).

Notes
=====

 *  As of version 1.5, named entities are no longer the default. One can
    still request named entities, as shown in the example above.

 *  As of version 1.4, ``mdx_smartpants`` attempts to automagically guess the
    direction of text flow used by the underlying language (e.g. LTR or RTL) and
    arrange quotation marks accordingly. Thanks to `Ahmad Khayyat
    &lt;https://bitbucket.org/akhayyat&gt;`_ for the bug report and discussion that
    led to this upgrade. This release also moved to a package-oriented distribution,
    given the additional modules required.

 *  As of version 1.2, ``mdx_smartpants`` no longer uses the stock
    ``smartypants`` module from PyPI. It incorporates a copy of the module,
    called ``spants``, in order to tweak the code for Python 3 compatibility, to
    fix the incorrect munging of punctuation within style blocks, and to make
    other improvements. This is a partial step towards a rewrite of
    ``smartypants`` itself to support Python 3 and be more in-line with modern
    Python idioms.

 *  Now successfully packaged for, and tested against, against Python 2.6, 2.7,
    and 3.3, as well as against PyPy 1.9 (based on 2.7.2). As of Version 1.4,
    official support for Python 2.5 and 3.2 withdrawn; while it may work on
    these, I can no longer test those versions. Also, they're obsolete. Time to
    upgrade!

 *  Automated multi-version testing managed by the awesome `pytest
    &lt;http://pypi.python.org/pypi/pytest&gt;`_ and `tox
    &lt;http://pypi.python.org/pypi/tox&gt;`_.

 *  The author, `Jonathan Eunice &lt;mailto:jonathan.eunice@gmail.com&gt;`_ or
    `@jeunice on Twitter &lt;http://twitter.com/jeunice&gt;`_ welcomes your comments
    and suggestions.

Installation
============

::

    pip install -U mdx_smartypants

To use ``pip`` to install under a specific Python version, look for a
program such as ``pip-3.3`` (e.g. ``which pip-3.3`` on Unix derived systems).
Failing this, you may be able to ``easy_install`` under a specific Python version
(3.3 in this example) via::

    python3.3 -m easy_install --upgrade mdx_smartypants

(You may need to prefix these with "sudo " to authorize installation.)
</pre></body></html>