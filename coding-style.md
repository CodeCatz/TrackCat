# CodeCatz Coding Style Guide

First read [why coding style matters](http://www.smashingmagazine.com/2012/10/25/why-coding-style-matters/).

Examples of other _good_ coding styles and best practices:
- [Front-end Code Standards & Best Practices](http://isobar-idev.github.io/code-standards/)
- [Google HTML/CSS style guide](http://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml)


## General formatting rules

**Indentation**
- We use _tabs_ to indent code. Indent by one tab at the time.

**Capitalization**
- Use lowercase, e.g. `<table>` in HTML, `#cccccc` for colors in css

**Trailing whitespace**
- Remove trailing white space (even when on an empty line).
[Why is trailing space such a big issue](http://programmers.stackexchange.com/questions/121555/why-is-trailing-whitespace-a-big-deal) anyway?

**Newline at the end of a file**
- Always add a newline at the end of any file you edit. [Why, you ask](http://robots.thoughtbot.com/no-newline-at-end-of-file)?

**Naming**

## HTML
- Always close tags.
- Tables shouldn't be used for page layout.
- Always use quotes around attributes in a tag.  
`<p class="headline" data-attribute="106">This is my paragraph of special text.</p>`

## CSS
- Indent CSS code.
- Don’t use inline css.
- Never edit framework css files (e.g. bootstrap). Override styles in your custom css file.

## JavaScript
 - Always use semicolons.

## Python
- unless specifically mentioned otherwise, we basically follow the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008)
- when importing from the same module, it's ok to use the following syntax  
`from module import class, another, many`
