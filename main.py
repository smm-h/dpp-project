from pandas import read_csv

from Table import Table
from patients import patients

if __name__ == '__main__':
    # # load tables
    # t1 = Table(patients, read_csv('data/1_inpatient_microdata.csv'))
    # t2 = Table(patients, read_csv('data/2_inpatient_microdata_4_anonymous.csv'))
    # # t3 = Table(patients, read_csv('data/2_inpatient_microdata_4_anonymous.csv'))
    # # t4a = Table(read_csv('data/4a_data_description_adults.csv'))
    # # t4b = Table(read_csv('data/4b_data_description_lands_end.csv'))
    #
    # print(t1.get_k())
    # print(t2.get_k())

    fn = 'data/generated/1000'
    k = 4
    t = Table(patients, read_csv(fn + '.csv'))
    print(t.get_k())
    a = t.k_anonymize(k)
    print(a)
    print(a.get_k())
    s = a.to_csv(",")

    with open(fn + f'_{k}.csv', 'w') as f:
        f.write(s)
