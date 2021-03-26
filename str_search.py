class StrSearch:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def search(self, this):
        pass

    def get_edges(self, str):
        betta = []
        for i in range(len(str)):
            betta.append(0)
        betta[0] = 0
        for i in range(len(str) - 1):
            b = betta[i]
            while (b > 0 and str[i+1] != str[b]):
                b = betta[b-1]
            if str[i+1] == str[b]:
                betta[i+1] = b + 1
            else:
                betta[i+1] = 0
        return betta
