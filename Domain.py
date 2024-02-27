from pandas import DataFrame
from random import choices

from generalizers import make_taxonomy_generalizer


class Domain:
    def __init__(self, name: str, sensitive: bool, sort_rank: int, generator, generalizer):
        self.name: str = name
        self.sensitive: bool = sensitive
        self.sort_rank: int = sort_rank
        self.generator = generator
        self.generalizer = generalizer

    @staticmethod
    def make_from_df(name: str, sensitive: bool, sort_rank: int, df: DataFrame):
        v = list(df['Value'])
        w = list(df['Weight']) if 'Weight' in df else None  # nullable
        t = list(df['Taxonomy'])
        taxonomy = dict()
        for i in range(len(v)):
            b = t[i].split(';')
            taxonomy[v[i]] = b[0]
            for j in range(len(b) - 1):
                taxonomy[b[j]] = b[j + 1]
            taxonomy[b[-1]] = '*'
        g = make_taxonomy_generalizer(taxonomy)
        return Domain(name, sensitive, sort_rank, lambda: choices(v, w)[0], g)
