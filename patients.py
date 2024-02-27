from pandas import read_csv
from numpy.random import normal
from random import choice, choices

from Domains import Domains

patients = (
    Domains()
    .add('Zip Code', False,
         lambda: int(choice([
             normal(12500, 200),
             normal(14500, 200),
             normal(17500, 250),
         ])))
    .add('Age', False,
         lambda: int(normal(45, 12)))
    .add_from_df(read_csv('data/columns/Nationality.csv'))
    .add_from_df(read_csv('data/columns/Condition.csv'))
    .add_from_df(read_csv('data/columns/Sex.csv'))
)

if __name__ == '__main__':
    n = 10
    d = patients.generate(n)
    s = d.to_csv()
    print(s)
    # with open(f'data/generated/{n}.csv', 'w') as f:
    #     f.write(s)
