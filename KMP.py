from str_search import StrSearch
# алг Кнута-Морриса-Пратта (сначала вычисляется массив граней, потом уже в зависимости от него двигается паттерн)
class KMP(StrSearch):
    def search(self, this):
        print("\nKMP...")

        result = []
        result_compare = 0
        # получаем массив граней (бетта)
        betta = self.get_edges(self.pattern)

        print(betta)
        print()
        k = 0
        # тут если есть несовпадение, то сравнение сдвигается вправо/вправо в соответствием со значением в массиве граней
        for i in range(len(self.text)):
            result_compare += 1
            # несовпадение? - сдвиг вслево
            while k > 0 and self.text[i] != self.pattern[k]:
                k = betta[k-1]
                result_compare += 1
            result_compare += 1
            # совпадение? - движемся вправо по паттерну
            if self.text[i] == self.pattern[k]:
                k += 1
            # конец паттерна? - заносим позицию в результат + сдвигаем указатель k в соответствии с массивом граней
            if k == len(self.pattern):
                result.append(i - len(self.pattern) + 1)
                k = betta[k-1]
        return result, result_compare


