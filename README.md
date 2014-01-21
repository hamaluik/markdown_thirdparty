# Markdown Third-Party

This plugin adds a few third-party markdown extensions to Pelican:

* MathJax: https://github.com/mayoff/python-markdown-mathjax
* SmartyPants: https://bitbucket.org/jeunice/mdx_smartypants
* Checklist: https://github.com/FND/markdown-checklist
* Video: http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/
* Iconfonts: https://github.com/MadLittleMods/markdown-icons
* QRCode: https://github.com/airtonix/python-markdown-qrcode

The files have been modified slightly to streamline into the plugin

## Prerequisities

* MathJax
    * MathJax to be added to your template's `<head>` tag
* SmartyPants
    * guess-language: `sudo pip install guess-language`
    * namedentities (v 1.5.2+): https://pypi.python.org/pypi/namedentities/1.5.2
* Checklist
    * None
* Video
    * None
* Iconfonts
    * An icon font (such as [Font Awesome](http://fortawesome.github.io/Font-Awesome/)) to be implemented in your template.
* QRCode
    * None

## Usage

Add the desired extensions to your `MD_EXTENSIONS` setting in **pelicanconf.py**. Example:

```python
MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra', 'mathjax', 'smartypants(entities=named)', 'checklist', 'video', 'iconfonts', 'qrcode']
```

### MathJax

Add the following to the `<head>` of your template:

```html
<!-- mathjax config similar to math.stackexchange -->
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
	jax: ["input/TeX", "output/HTML-CSS"],
	tex2jax: {
		inlineMath: [ ['$', '$'] ],
		displayMath: [ ['$$', '$$']],
		processEscapes: true,
		skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
	},
	messageStyle: "none",
	"HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] }
});
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

Then anywhere in your markdown posts, add some math:

```latex
$$
\begin{align}
x(t) &= At^3 + Bt^2 + Ct + D \\
y(t) &= Et^3 + Ft^2 + Gt + H \\
\end{align}
$$
```

See the documentation at https://github.com/mayoff/python-markdown-mathjax for more information.

### SmartyPants

Applies typographic 'prettification', ie converts `--` to `&mdash;`, `---` to `&ndash;`, `...` to `&hellip;`, etc. Caution: may add a significant amount of time to page processing!

See the documentation at https://bitbucket.org/jeunice/mdx_smartypants for more information.

### Checklist

Easily add GitHub-flavoured markdown checklists:

```md
* [ ] foo
* [x] bar
* [ ] baz
```

to get:

```html
<ul>
<li><input type="checkbox" disabled> foo</li>
<li><input type="checkbox" disabled checked> bar</li>
<li><input type="checkbox" disabled> baz</li>
</ul>
```

See the documentation at https://github.com/FND/markdown-checklist for more information.

### Video

Just add a youtube, etc, url and the video will be embedded!

See the documentation at http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/ for more information.

### Iconfonts

Use [HTML Entity](http://www.w3schools.com/html/html_entities.asp) like syntax:

```md
I love &icon-html5; and &icon-css3;
&icon-spinner:large,spin; Sorry we have to load...
```

To get:

```html
I love <i aria-hidden="true" class="icon-html5"></i> and <i aria-hidden="true" class="icon-css3"></i>
<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...
```

See the documentation at https://github.com/MadLittleMods/markdown-icons for more information.

### QRCode

Encode strings between `[-[` and `]-]` as QR codes and embed them.

See the documentation at https://github.com/airtonix/python-markdown-qrcode for more information.
