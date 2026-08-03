from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.minFreq = 0
        self.val = {}
        self.freq = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.val:
            return -1

        value, f = self.val[key]

        del self.freq[f][key]

        if not self.freq[f]:
            del self.freq[f]
            if self.minFreq == f:
                self.minFreq += 1

        self.val[key] = [value, f + 1]
        self.freq[f + 1][key] = 1

        return value

    def put(self, key, value):
        if self.cap == 0:
            return

        if key in self.val:
            self.val[key][0] = value
            self.get(key)
            return

        if len(self.val) == self.cap:
            old, _ = self.freq[self.minFreq].popitem(last=False)
            del self.val[old]

        self.val[key] = [value, 1]
        self.freq[1][key] = 1
        self.minFreq = 1