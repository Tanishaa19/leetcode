class SQL:

    def __init__(self, names, columns):
        self.db = {}
        for n, c in zip(names, columns):
            self.db[n] = [c, 1, {}]   # cols, next_id, rows

    def ins(self, name, row):
        if name not in self.db or len(row) != self.db[name][0]:
            return False

        cols, nxt, rows = self.db[name]
        rows[nxt] = row
        self.db[name][1] += 1
        return True

    def rmv(self, name, rowId):
        if name in self.db:
            self.db[name][2].pop(rowId, None)

    def sel(self, name, rowId, columnId):
        if name not in self.db:
            return "<null>"

        rows = self.db[name][2]

        if rowId not in rows:
            return "<null>"

        row = rows[rowId]

        if columnId < 1 or columnId > len(row):
            return "<null>"

        return row[columnId - 1]

    def exp(self, name):
        if name not in self.db:
            return []

        rows = self.db[name][2]
        return [str(i) + "," + ",".join(rows[i]) for i in sorted(rows)]