from str_search import StrSearch

class Naive_Search(StrSearch):
    def search(self, this):
        print("\nNaive Search...")

        n = len(self.text)
        m = len(self.pattern)
        result = []
        result_compare = 0
        sch = 0
        for i in range(n - m + 1):
            for j in range(m):
                result_compare += 1
                if self.text[i + j] == self.pattern[j]:
                    sch += 1
            if sch == m:
                result.append(i)
            sch = 0
        return result, result_compare



