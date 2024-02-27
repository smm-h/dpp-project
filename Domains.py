from pandas import DataFrame, Series
from typing import List

from Domain import Domain


# an object that stores a list of Domain objects along with
# some cache, for the purpose of optimization
class Domains:
    def __init__(self, domains: List[Domain]) -> None:
        self.domains: List[Domain] = domains
        self.names = [d.name for d in domains]

        # quasi-identifiers vs. sensitive attributes
        self.q: List[str] = [d.name for d in domains if not d.sensitive]
        self.s: List[str] = [d.name for d in domains if d.sensitive]

        self.sort_order: List = \
            [d for d in sorted(domains, key=lambda d: d.sort_rank) if not d.sensitive]

    # generate a fake Table
    def generate(self, n: int):
        df = DataFrame(
            data=[[d.generator() for d in self.domains] for _ in range(n)],
            columns=self.names,
        )
        # importing here to avoid circular imports
        from Table import Table
        return Table(self, df)

    def get_csv_header(self, delimiter: str = ',') -> str:
        return delimiter.join(self.names)

    def __str__(self):
        return f'Domains:{self.names}'

    def anonymize(self, rows: List[Series]):
        s = self.s
        results = [dict() for _ in rows]

        for s in self.s:
            for rid in range(len(rows)):
                results[rid][s] = rows[rid][s]

        i = 0
        while i < len(self.sort_order):
            d = self.sort_order[i]
            g = d.generalizer
            v = [row[d.name] for row in rows]
            while len(set(v)) > 1:
                # print(v)
                v = [g(x) for x in v]
            i += 1
            for r in results:
                r[d.name] = v[0]

        return results
