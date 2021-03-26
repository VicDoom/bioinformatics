from str_search import StrSearch
from naive_search import Naive_Search
from KMP import KMP
from BM import BM
from KR import KR
from DBG import DBG
import timeit
import time

class BioLab:
    def __init__(self, StrSearch):
        f = open('input.txt')
        self.text = f.readline()[:-1]
        self.pattern = f.readline()
        self._str_search = StrSearch(self.text, self.pattern)

    @property
    def str_search(self):
        return self._str_search

    @str_search.setter
    def str_search(self, StrSearch):
        self._str_search = StrSearch(self.text, self.pattern)

    def calc_result(self):
        return self._str_search.search(self._str_search)

    def get_result(self):
        start_time = time.perf_counter_ns() / 1e6
        result, result_compare = self.calc_result()
        end_time = time.perf_counter_ns() / 1e6
        return [(end_time - start_time), result, result_compare]


if __name__ == '__main__':
    lab = BioLab(Naive_Search)
    result = lab.get_result()
    print("time: ", result[0])
    print("result: ", result[1])
    print("symbol compare amount: ", result[2])

    lab.str_search = KMP
    result = lab.get_result()
    print("time: ", result[0])
    print("result: ", result[1])
    print("symbol compare amount: ", result[2])

    lab.str_search = BM
    result = lab.get_result()
    print("time: ", result[0])
    print("result: ", result[1])
    print("symbol compare amount: ", result[2])

    lab.str_search = KR
    result = lab.get_result()
    print("time: ", result[0])
    print("result: ", result[1])
    print("symbol compare amount: ", result[2])

    lab.str_search = DBG
    result = lab.get_result()
    print("time: ", result[0])
    print("result: ", result[1])
    print("symbol compare amount: ", result[2])
