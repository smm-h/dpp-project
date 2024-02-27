from pandas import DataFrame
from typing import List

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

    def k_anonymize(self, k: int) -> None: