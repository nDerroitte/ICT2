from textHandling import *

def getProbDistrib(alphabet, size=1):
    """
    From the alphabet, determine the prob distrib of each symbols
    Assumption : all char are in the alphabet
    """
    dict_symbols, char_count = getSymbolCount(alphabet, size)
    prob_distrib = dict(dict_symbols)
    for key in prob_distrib:
        prob_distrib[key] /= char_count
    return prob_distrib, char_count
