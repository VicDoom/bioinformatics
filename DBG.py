from str_search import StrSearch

class DBG(StrSearch):
    def search(self, this):
        # Демелки Бейза Ятса Гоннета
        print("\nDBG...")
        self.alphabet = self.get_alphabet(self.text, self.pattern)
        self.t = self.get_t()
        self.n = len(self.text)
        self.m = len(self.pattern)

        result = []
        result_compare = 0

        s = list('0'+'1'*self.m)
        for i in range(self.n):
            for j in range(self.m):
                s[j] = int(s[j]) or int(self.t[self.text[i]][j])
            for j in range(self.m):
                s[self.m-j] = s[self.m-1-j]
            s[0] = 0
            result_compare += 1
            if s[self.m] == 0:
                result.append(i-self.m+1)

        return result, result_compare

    def get_alphabet(self, t1, t2):
        alphabet = set(t1)
        alphabet_pattern = set(t2)

        alphabet.update(alphabet_pattern)
        return alphabet

    def get_t(self):
        t = dict()
        for i in self.alphabet:
            cur_t = []
            for j in range(len(self.pattern)):
                if i == self.pattern[j]:
                    cur_t.append(0)
                else:
                    cur_t.append(1)
            t[i] = cur_t
        return t