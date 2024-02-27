from pandas import DataFrame
from random import choices


class Domain:
    def __init__(self, name: str, sensitive: bool, generator, generalizer):
        self.name: str = name
        self.sensitive: bool = sensitive
        self.generator = generator
        self.generalizer = generalizer

    @staticmethod
    def make_from_df(name: str, sensitive: bool, df: DataFrame):
        v = list(df['Value'])  # non-nullable
        w = list(df.get('Weight'))
        g = list(df.get('Generalization'))
        return Domain(name, sensitive,
                      lambda: choices(v, w)[0],
                      lambda x: g[0] if x not in g else g[1 + g.index(x)])
