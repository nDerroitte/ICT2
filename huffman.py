from util import *
from CST import *


class Huffman:
    def __init__(self, nb_char=1):
        self.length = 0
        self.huffman_dict = {}

    def binaryHuffmanCoding(self, dict):
        """
        From a probability distribution, compute the binary huffman coding
        """
        self.huffman_dict, tmp = self.binaryHuffmanCodingAux(dict)
        self.length += tmp
        return self.huffman_dict


    def binaryHuffmanCodingAux(self, dict):
        """
        From a probability distribution, compute the binary huffman coding
        Auxialary function used in order to set the huffman class wiht the good
        dict and good length
        """
        if(len(dict) == 2):
            k1  = lowestKeyDict(dict)
            v1 = dict.pop(k1)
            k2 = lowestKeyDict(dict)
            v2 = dict.pop(k2)
            return {k1 : '1', k2 : '0'}, v1+v2

        k1 = lowestKeyDict(dict)
        v1 = dict.pop(k1)
        k2 = lowestKeyDict(dict)
        v2 = dict.pop(k2)
        dict[k1 + k2] = v1 + v2

        huffman_dict, count = self.binaryHuffmanCodingAux(dict)
        self.length += count

        current_coding = huffman_dict.pop(k1 + k2)
        huffman_dict[k1] = current_coding + '1'
        huffman_dict[k2] = current_coding + '0'
        return huffman_dict, v1 + v2

    def encode(self, size=1):
        """
        Enocde the text.csv file using the huffman encoding
        """
        str_out = ""
        f = open(CST.TEXT_FILE, "r")
        char = f.read(1)
        symbol = ""
        # While not at the EOF
        while char:
            # Put in lowercase
            if char.isupper():
                char = char.lower()
            symbol +=char
            if len(symbol) == size:
                str_out+= self.huffman_dict[symbol]
                symbol = ""
            char = f.read(1)
        return str_out

    def expectedAvgLength(self, prob_dict):
        """
        Compute the expected Average Length of the code
        """
        avg_l = 0
        for key in self.huffman_dict:
            avg_l += prob_dict[key]* len(self.huffman_dict[key])
        return avg_l
