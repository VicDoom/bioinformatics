from str_search import StrSearch
# алг Карпа-Рабена
class KR(StrSearch):
    def search(self, this):
        print("\nKR...")
        self.n = len(self.text)
        self.m = len(self.pattern)

        self.big_prime_num = 15487469
        self.x = 101
        self.text_hash = []
        result = []
        result_compare = 0
        
        # вычисляем хэш для паттерна
        self.pattern_hash = self.hash(0, self.pattern)

        # вычисляем хэш для текста последовательно, каждый следующий хэш вычисляется из предыдущего
        for i in range(self.n-self.m+1):
            self.text_hash.append(self.hash(i, self.text))

        # определяем вхождения - если хэш паттерна равен соответствующего хэша текста в данной позиции, то определено равенство подстроки и паттерна
        for i in range(len(self.text_hash)):
            if self.text_hash[i] == self.pattern_hash:
                result.append(i)
            result_compare += 1

        print(self.text_hash)
        print(self.pattern_hash)
        print()

        return result, result_compare

    # хэш считается по сложной формуле с Википедии https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%A0%D0%B0%D0%B1%D0%B8%D0%BD%D0%B0_%E2%80%94_%D0%9A%D0%B0%D1%80%D0%BF%D0%B0
    def hash(self, i, text):
        result = 0
        if i == 0:
            x = 1
            for j in range(self.m):
                summand = self.module_multiple(ord(text[self.m-1-j]), x)
                result = self.module_sum(result, summand)
                x = self.module_multiple(x, self.x)
        else:
            x = self.module_power(self.x, self.m-1)
            tmp_result = self.module_subtraction(self.text_hash[i-1], self.module_multiple(ord(text[i-1]), x))
            result = self.module_sum(self.module_multiple(tmp_result, self.x), ord(text[i+self.m-1]))
        return result % self.big_prime_num

    # эти функции определяют возведение в степень, сложение, умножение и деление по модулю (чтобы не было слишком больших чисел)
    def module_power(self, a, n):
        x = 1
        for i in range(n):
            x = (x * a) % self.big_prime_num
        return x

    def module_sum(self, a, b):
        return ((a % self.big_prime_num) + (b % self.big_prime_num)) % self.big_prime_num

    def module_multiple(self, a, b):
        return ((a % self.big_prime_num) * (b % self.big_prime_num)) % self.big_prime_num

    def module_subtraction(self, a, b):
        return ((a % self.big_prime_num) - (b % self.big_prime_num)) % self.big_prime_num
