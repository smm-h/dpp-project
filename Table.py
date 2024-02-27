from pandas import read_csv, DataFrame

from Domains import Domains


class Table:
    def __init__(self, domains: Domains, data: DataFrame):
        self.dm: Domains = domains
        self.df: DataFrame = data

    # returns k; k=1 means not anonymous
    def get_k(self) -> int:
        return self.df.groupby(self.dm.q).size().min()

    def to_csv(self, delimiter: str = ',') -> str:
        return (self.dm.get_csv_header(delimiter) + '\n' +
                '\n'.join((delimiter.join((str(i) for i in row.values)) for _, row in self.df.iterrows())))

    def __str__(self):
        return str(self.df)

    def __repr__(self):
        return repr(self.df)

    def k_anonymize(self, k: int):
        sort_order = self.dm.sort_order
        rows = [row for _, row in self.df.sort_values(sort_order).iterrows()]
        chunks = [self.dm.anonymize(rows[i:i + k]) for i in range(0, len(self.df), k)]
        anonymized_rows = []
        for c in chunks:
            for i in c:
                anonymized_rows.append(i)
        return Table(self.dm, DataFrame(anonymized_rows, columns=self.df.columns))
