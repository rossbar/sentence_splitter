"""
Hello world panflute filter.
"""

import panflute as pf

def echo_paragraphs(elem, doc):
    if type(elem) == pf.Para:
        print(elem, "\n\n\n")

def main(doc=None):
    return pf.run_filter(echo_paragraphs, doc=doc)

if __name__ == "__main__":
    main()
