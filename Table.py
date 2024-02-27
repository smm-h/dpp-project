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

    def k_anonymize(self, k: int):
        return self.df.groupby(self.dm.q)


if __name__ == '__main__':
    from patients import patients

    t = Table(patients, read_csv('data/generated/1000.csv'))
    print(t.k_anonymize(2))
