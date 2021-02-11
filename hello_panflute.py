"""
Hello world panflute filter.
"""

import panflute as pf

def echo_paragraphs(elem, doc):
    if type(elem) == pf.Para:
        print(elem, "\n\n\n")

def simple_sbd(elem, doc):
    """
    Simplest possible search for sentence boundaries, as follows:
      - Grab the previous element (assuming the current one is a pf.Space)
      - If the previous element is a pf.Str and ends with '.', '?', or '!',
        then treat this as a sentence boundary and convert the current element
        to a SoftBreak instead.
    """
    if isinstance(elem, pf.Space):
        prev_elem = elem.offset(-1)  # Should be None if prev elem doesn't exist
        if isinstance(prev_elem, pf.Str):
            if prev_elem.text.endswith(('.', '!', '?')):
                return pf.SoftBreak
    return elem
        

def paragraph_sentence_splitter(elem, doc):
    """
    Walk through the elements of a Para object looking for sentence boundaries.

    When found, add a softbreak
    """
    if type(elem) == pf.Para:
        return elem.walk(simple_sbd)
    return elem


def main(doc=None):
    return pf.run_filter(paragraph_sentence_splitter, doc=doc)

if __name__ == "__main__":
    main()
