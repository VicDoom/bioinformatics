from str_search import StrSearch
class KMP(StrSearch):
    def search(self, this):
        print("\nKMP...")

        result = []
        result_compare = 0
        betta = self.get_edges(self.pattern)

        print(betta)
        print()
        k = 0
        for i in range(len(self.text)):
            result_compare += 1
            while k > 0 and self.text[i] != self.pattern[k]:
                k = betta[k-1]
                result_compare += 1
            result_compare += 1
            if self.text[i] == self.pattern[k]:
                k += 1
            if k == len(self.pattern):
                result.append(i - len(self.pattern) + 1)
                k = betta[k-1]
        return result, result_compare


