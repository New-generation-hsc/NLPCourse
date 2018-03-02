"""
2018-3-2 : N Gram Language Model
In this file, I implement the n-gram language model(default n=2)
"""

from collections import Counter


class NGram(object):
    """
    Every Sentence has n special words `<sos>` represent `start of sentence`
    and a special word `<eos>` represent `end of sentence`
    """
    def __init__(self, n, sos="<sos>", eos="<eos>"):
        assert n >=1, "The Gram N must be larger then 1"
        self.n = n
        self.memory = None
        self.sos = sos
        self.eos = eos

    def pad_sentence(self, words):
        """
        every sentence should add n sos and one eos
        :param words: list -> the sentence words
        :return:
        eg. I Love china.(n=2)
            <sos> <sos> I Love china. <eos>
        """
        words = words.append(self.eos)
        return [self.sos] * self.n + words