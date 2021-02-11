# A Sentence-Based Markup Linter

## Devnotes

First example: un-linewrapped text from spec-0000.

To see pandoc AST

```
pandoc -s -t native filter-test.md
```

#### Panflute

Run panflute filter `hello_panflute.py` on a markdown file, e.g. `filter-test.md`:

```
cat filter-test.md | pandoc -s -t json | python hello_panflute.py
```
