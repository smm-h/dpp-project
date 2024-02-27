from pandas import DataFrame
from random import choices

from generalizers import get_list_generalizer


class Domain:
    def __init__(self, name: str, sensitive: bool, generator, generalizer):
        self.name: str = name
        self.sensitive: bool = sensitive
        self.generator = generator
        self.generalizer = generalizer

    @staticmethod
    def make_from_df(name: str, sensitive: bool, df: DataFrame):
        v = list(df['Value'])
        w = list(df['Weight']) if 'Weight' in df else None  # nullable
        g = list(df['Generalization']) if 'Generalization' in df else []
        return Domain(name, sensitive, lambda: choices(v, w)[0], get_list_generalizer(g))
