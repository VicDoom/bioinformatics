from str_search import StrSearch

class BM(StrSearch):
    def search(self, this):
        print("\nBM...")
        self.delta1, self.delta2 = self.get_table()
        result = []
        result_compare = 0
        n = len(self.text)
        m = len(self.pattern)
        # l = m-1
        # k = m-1
        i = m - 1
        while i < n:
            j = m - 1
            result_compare += 1
            while 0 <= i and 0 <= j  and self.text[i] == self.pattern[j]:
                i -= 1
                j -= 1
                result_compare += 1
            if j == -1:
                result.append(i+1)
            if self.text[i] in self.delta1:
                index_delta1 = self.delta1[self.text[i]]
            else:
                index_delta1 = self.delta1["else"]

            if j >= 0:
                index_delta2 = self.delta2[j]
            else:
                index_delta2 = self.delta2[0] + 1
            i += max(index_delta1, index_delta2)

        return result, result_compare

    def get_table(self):
        delta1 = self.get_delta1()
        delta2 = self.get_delta2()
        print(delta1, delta2)
        print()
        return delta1, delta2

    def get_delta1(self):
        table = dict()
        pattern_list = list(self.pattern)
        for i in range(len(pattern_list)):
            cur = len(pattern_list) - i - 1
            if cur == -1:
                break
            if pattern_list[cur] not in table:
                table[pattern_list[cur]] = len(pattern_list) - cur - 1

        if pattern_list[len(pattern_list) - 1] not in table:
            table[pattern_list[len(pattern_list) - 1]] = len(pattern_list)
        table["else"] = len(pattern_list)

        return table

    def get_delta2(self):
        # get betta
        betta = self.get_edges(self.pattern)

        # get transposed betta
        pattern_list = list(self.pattern)
        pattern_list.reverse()
        reversed_pattern = ''.join(pattern_list)
        betta_transposed = self.get_edges(reversed_pattern)

        # get po
        betta_transposed.reverse()
        po = betta_transposed.copy()
        betta_transposed.reverse()

        # get g1
        g1 = [0]
        for j in range(len(self.pattern)):
            if j == 0: continue
            delta_j = len(self.pattern) - j - 1
            current = j
            while current > 0:
                if po[current] == delta_j and po[current - 1] != (delta_j + 1):
                    break
                current -= 1

            if current == 0:
                g1.append(0)
            else:
                g1.append(current)

        # get g2
        m = betta[len(self.pattern)-1]
        g2 = [m]
        Sm = [m]
        while 0 < Sm[len(Sm)-1]:
            m = betta[m-1]
            Sm.append(m)
        for i, b_m in enumerate(Sm):
            m = len(self.pattern)
            if i == 0:
                for j in range(m - Sm[0]):
                    if j == 0: continue
                    g2.append(Sm[0])
            else:
                start = len(self.pattern) - Sm[i-1] + 1
                while start <= m - Sm[i]:
                    g2.append(Sm[i])
                    start += 1

        delta2 = []
        for i in range(len(g1)):
            m = len(self.pattern)
            if g1[i] != 0:
                delta2.append(m - g1[i])
            else:
                delta2.append(m - i + m - g2[i] - 1)

        return delta2








