# A Sentence-Based Markup Linter

Current version: A dumb simple filter using `panflute` that essentially does
the following:
 - For any paragraph elements (and paragraphs only at the moment), look for
   sentence breaks as indicated by `. `, `? `, or `! `. If found, replace the
   space with a softbreak

To test this out on a single file called e.g. `myfile.md`, run:

```
cat myfile.md | pandoc -s -t json | python hello_panflute.py | pandoc --wrap=preserve -s -f json -t gfm
```

## Devnotes

First example: un-linewrapped text from spec-0000.

To see pandoc AST

```
pandoc -s -t native filter-test.md
```
