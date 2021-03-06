from nbSymbol import *
from probDistrib import *
from util import *
from huffman import *

def sourceCoding():
    print("QUESTION 1:")
    alphabet = getAlphabet()
    print("Number of symbols : {}".format(nbSymbols(alphabet)))
    print("QUESTION 2:")
    print("Marginal probability distribution of all symbols from the text sample:")
    prob_distrib, total_length = getProbDistrib(alphabet)
    printSortedDict(prob_distrib)
    print("QUESTION 3:")
    huff = Huffman()
    huffman_dict = huff.binaryHuffmanCoding(dict(prob_distrib))
    printSortedDict(huffman_dict)
    print("QUESTION 4:")
    print("Encoding of the text file ...", end=' ')
    huffman_encode = huff.encode()
    print("  done! Uncomment in code to see the encoded text (quite large)")
    # UNCOMMENT HERE to see the encoded text
    # print(str_encode)
    simple_encode = SimpleEncode()
    print("Total length of the encoded text sample : {}".format(len(huffman_encode)))
    print("Total length of the simple encoded text sample: {}".format(len(simple_encode)))
    print("Total length of the not enconded text sample : {}".format(total_length))
    print("QUESTION 5:")
    print("Expected average length for this code : {}".format(huff.expectedAvgLength(prob_distrib)))
    print("Empirical average length for this code : {}".format(huff.length))

    print("QUESTION 6:")
    print("Compression rate of the algoritm: {}".format(len(simple_encode)/len(huffman_encode)))
    print("QUESTION 7:")
    print("Using 2 characters for huffman coding")
    alphabet_2 = getAlphabet(2)
    prob_distrib_2, _ = getProbDistrib(alphabet_2, 2)
    huff_2 =  Huffman()
    huffman_dict_2 = huff_2.binaryHuffmanCoding(prob_distrib_2)
    huffman_encode_2 = huff_2.encode(2)
    print("Total length of the new encoded text sample : {}".format(len(huffman_encode_2)))
    print("Compression rate of the new algoritm: {}".format(len(simple_encode)/len(huffman_encode_2)))
