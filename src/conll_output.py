

import re
from typing import List, Union

from src.classes import Token


def print_to_conll(string_lines):
    for line in string_lines:
        print(line)

def text_tuples_to_string(
        text_tuples: List[List[tuple]], 
        annotations: Union[List[str], None]=None, 
        sentences: Union[List[str], None]=None
    ):
    if sentences is not None: 
        # filter out empty lines
        sentences = list(filter(lambda x : len(re.sub(r"\s+", "", x, flags=re.UNICODE)) > 0, sentences))
    # get treeTokens
    tokens = [[tup[1] for tup in sent] for sent in text_tuples]

    string_lines: List[str] = []
    for i, sentence_tuples in enumerate(text_tuples):
        if sentences:
            string_lines.extend(
                (
                    f"# text = {sentences[i].strip()}",
                    f"# treeTokens = {' '.join(tokens[i])}",
                )
            )
        elif annotations:
            string_lines.append(annotations[i])

        for token_tuple in sentence_tuples:
            token = Token(*token_tuple)
            string_lines.append(token.to_conll_row())

        string_lines.append('') # add empty line between trees
    
    return string_lines