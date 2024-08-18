import pandas as pd
from datetime import datetime

today = datetime.today()
current_year = today.year

def load_races():
    races = pd.read_csv('./data/raw/races.csv', sep=',', decimal=';')
    circuits = pd.read_csv('./data/raw/circuits.csv', sep=',', decimal=';')

    races = races.merge(right=circuits, how='left', on=['circuitId'], suffixes=('','_c'))
    races['date'] = pd.to_datetime(races['date'], format='%Y-%m-%d')

    return races

def load_constructors_perf(selection:list=None):
    constructors = pd.read_csv('./data/raw/constructors.csv', sep=',', decimal=';')
    constructor_standing = pd.read_csv('./data/raw/constructor_standings.csv', sep=',', decimal=';')
    constructor_standing = constructor_standing.merge(right=constructors, how='left', on=['constructorId'], suffixes=('','_c'))

    races = load_races()
    constructor_standing = constructor_standing.merge(right=races, how='left', on=['raceId'], suffixes=('','_r'))
    constructor_standing['points'] = constructor_standing['points'].astype(float)
    constructor_standing['year'] = constructor_standing['year'].astype(int)

    if selection == None:
        constructor_standing = constructor_standing[(constructor_standing['year'] >= 2000)].copy()
    else:
        constructor_standing = constructor_standing[(constructor_standing['year'] >= 2000) & (constructor_standing['name'].isin(selection))].copy()


    return constructor_standing, constructors

def load_drivers_perf(selection:list=None):
    drivers = pd.read_csv('./data/raw/drivers.csv', sep=',', decimal=';')
    driver_standing = pd.read_csv('./data/raw/driver_standings.csv', sep=',', decimal=';')
    driver_standing = driver_standing.merge(right=drivers, how='left', on=['driverId'], suffixes=('','_d'))

    races = load_races()
    driver_standing = driver_standing.merge(right=races, how='left', on=['raceId'], suffixes=('','_r'))
    driver_standing['points'] = driver_standing['points'].astype(float)
    driver_standing['year'] = driver_standing['year'].astype(int)

    if selection == None:
        driver_standing = driver_standing[(driver_standing['year'] >= 2000)].copy()
    else:
        driver_standing = driver_standing[(driver_standing['year'] >= 2000) & (driver_standing['surname'].isin(selection))].copy()
    
    return driver_standing, drivers

def load_pitstop():
    pit = pd.read_csv('./data/raw/pit_stops.csv', sep=',', decimal=';')
    races = pd.read_csv('./data/raw/races.csv', sep=',', decimal=';')
    pit = pit.merge(right=races, how='left', on=['raceId'], suffixes=('','_r'))

    drivers = pd.read_csv('./data/raw/drivers.csv', sep=',', decimal=';')
    pit = pit.merge(right=drivers, how='left', on=['driverId'], suffixes=('','_d'))

    result = pd.read_csv('./data/raw/results.csv', sep=',', decimal=';')
    pit = pit.merge(right=result, how='left', on=['raceId','driverId'], suffixes=('','_v'))

    constructors = pd.read_csv('./data/raw/constructors.csv', sep=',', decimal=';')
    pit = pit.merge(right=constructors, how='left', on=['constructorId'], suffixes=('','_c'))

    return pit, races


