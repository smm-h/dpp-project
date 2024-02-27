from pandas import DataFrame
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
