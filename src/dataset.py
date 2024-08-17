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

    constructor_standing = constructor_standing[(constructor_standing['year'] >= 2010)].copy()
    
    return constructor_standing, constructors

