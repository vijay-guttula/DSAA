# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size

        # find parent and compress path
        temp_src = src
        temp_dst = dst
        src = self.get_parent(src)
        dst = self.get_parent(dst)

        while self.row_counts[dst] is None:
            dst = self.get_parent(dst)
        else:
            while self.row_counts[temp_dst] is None:
                prev = temp_dst
                temp_dst = self.parents[temp_dst]
                self.parents[prev] = dst

        while self.row_counts[src] is None:
            prev = src
            src = self.get_parent(src)
            self.parents[prev] = dst
        else:
            while self.row_counts[temp_src] is None:
                prev = temp_src
                temp_src = self.parents[temp_src]
                self.parents[prev] = src

        if src == dst:
            return

        if self.row_counts[dst] is not None and self.row_counts[src] is not None:
            self.row_counts[dst] += self.row_counts[src]
            self.row_counts[src] = None
            self.parents[src] = dst
            self.max_row_count = max(self.max_row_count, self.row_counts[dst])
            return

    def get_parent(self, table):

        # remember you need to get the parents who's rows are not None
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
