#!/usr/bin/env python3

"""
This script generate two .csv files speed-events.csv and driver-feed.csv

Data schemas:

speed-events
driver_id:""
speed:""

driver-feed
id:""
name:""
age:""
city:""
machine_brand:""
"""
import random
import pandas as pd


def generate_random_speed(n):
    randomlist = []
    for i in range(1, n):
        n = random.randint(20, 120)
        randomlist.append(n)
    return randomlist


def generate_data_lst(data_lst, n):
    datalist = []
    for i in range(1, n):
        n = random.randint(0, 8)
        datalist.append(data_lst[n])
    return datalist


def generate_dataset_speed_events(driver_id_lst, speed_lst):
    speeds = {'driver_id': driver_id_lst,
              'speed': speed_lst
              }

    df = pd.DataFrame(speeds, columns=['driver_id',
                                       'speed'])

    compression_opts = dict(method='zip',
                            archive_name='speed-events.csv')
    df.to_csv('speed-events.zip', index=False, compression=compression_opts)
    print('\033[31m' + '>>> generated speed-events.zip')


def generate_dataset_driver_feed(id_lst, name_lst, age_lst, city_lst, machine_brand_lst):
    drivers = {'driver_id': id_lst,
               'name': name_lst,
               'age': age_lst,
               'city': city_lst,
               'machine_brand': machine_brand_lst
               }
    df = pd.DataFrame(drivers, columns=['driver_id',
                                        'name',
                                        'age',
                                        'city',
                                        'machine_brand'])

    compression_opts = dict(method='zip',
                            archive_name='driver-feed.csv')
    df.to_csv('driver-feed.zip', index=False, compression=compression_opts)
    print('\033[31m' + '>>> generated driver-feed.zip')


if __name__ == '__main__':
    records = 10000000
    print('\033[32m' + '>>> generating speed-events.zip')
    print('\033[32m' + '>>> generating driver-feed.zip')
    driver_id = [*range(1, records)]
    speed = generate_random_speed(records)
    city_lst = ['LONDON',
                'VILNIUS',
                'NEW YORK',
                'PARIS',
                'MOSCOW',
                'TOKYO',
                'DUBAI',
                'SINGAPORE',
                'BARCELONA']

    name_lst = ['Edna Mode',
                'Randle McMurphy',
                'Norman Bates',
                'Maximus',
                'Legolas',
                'Wednesday Addams',
                'Inigo Montoya',
                'Hal',
                'Gromit']

    age_lst = ['23',
               '48',
               '56',
               '32',
               '16',
               '66',
               '99',
               '100',
               '33']

    machine_brand_lst = ['Audi',
                         'Acura',
                         'BMW',
                         'Bentley',
                         'Buick',
                         'Cadillac',
                         'Chevrolet',
                         'Mitsubishi',
                         'Honda']

    generate_dataset_speed_events(driver_id, speed)

    generate_dataset_driver_feed(driver_id,
                                 generate_data_lst(name_lst, records),
                                 generate_data_lst(age_lst, records),
                                 generate_data_lst(city_lst, records),
                                 generate_data_lst(machine_brand_lst, records))

