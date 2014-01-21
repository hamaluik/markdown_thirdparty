
<!-- saved from url=(0059)https://raw.github.com/FND/markdown-checklist/master/README -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">[Markdown Checklist](https://github.com/FND/markdown-checklist)
[![build status](https://secure.travis-ci.org/FND/markdown-checklist.png)](http://travis-ci.org/FND/markdown-checklist)
[![coverage](https://coveralls.io/repos/FND/markdown-checklist/badge.png)](https://coveralls.io/r/FND/markdown-checklist)

a [Python Markdown](http://pythonhosted.org/Markdown/) extension for lists of
tasks with checkboxes

inspired by
[GitHub task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

    * [ ] foo
    * [x] bar
    * [ ] baz

becomes

    &lt;ul&gt;
    &lt;li&gt;&lt;input type="checkbox" disabled&gt; foo&lt;/li&gt;
    &lt;li&gt;&lt;input type="checkbox" disabled checked&gt; bar&lt;/li&gt;
    &lt;li&gt;&lt;input type="checkbox" disabled&gt; baz&lt;/li&gt;
    &lt;/ul&gt;

* a dash can be used instead of an asterisk for list items
* both upper- and lowercase "x" are accepted to activate checkboxes


Installation
------------

    $ pip install markdown-checklist


Usage
-----

    import markdown
    html = markdown.markdown(source, extensions=['markdown_checklist.extension'])

or

    import markdown
    from markdown_checklist.extension import ChecklistExtension
    html = markdown.markdown(source, extensions=[ChecklistExtension()])

There is also a small JavaScript/jQuery library to make checkboxes interactive:

    new Checklists("article", function(checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.get(uri, callback);
    }, function(markdown, checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.ajax({
            type: "put",
            uri: uri,
            data: markdown,
            success: callback
        });
    });

See included `checklists.js` for details.
</pre></body></html>