from pandas import read_csv
from numpy.random import normal
from random import randint

from Domain import Domain
from Domains import Domains
from generalizers import *

dm_zip_code = Domain(
    'Zip Code', False,
    lambda: str(int(normal(randint(12, 80) * 1000, 200))),
    asterisks_right_to_left
)

dm_age = Domain(
    'Age', False,
    lambda: str(int(normal(45, 12))),
    age_generalizer
)

dm_sex = Domain.make_from_df(
    'Sex', False,
    read_csv('data/columns/Sex.csv'))
dm_nationality = Domain.make_from_df(
    'Nationality', False,
    read_csv('data/columns/Nationality.csv'))
dm_condition = Domain.make_from_df(
    'Condition', True,
    read_csv('data/columns/Condition.csv'))

patients = Domains([
    dm_zip_code,
    dm_age,
    dm_sex,
    dm_nationality,
    dm_condition,
])

if __name__ == '__main__':
    n = 1000
    d = patients.generate(n)
    s = d.to_csv()
    # print(s)
    with open(f'data/generated/{n}.csv', 'w') as f:
        f.write(s)
