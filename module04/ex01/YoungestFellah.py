import pandas as pd

def youngestFellah(data_set, year):
  is_ = data_set['Year'] == year
  is_good_date = data_set[is_]
  is_men = is_good_date['Sex'] == 'M'
  is_women = is_good_date['Sex'] == 'F'

  return { 'f': (is_good_date[is_women])['Age'].min(), 'm': (is_good_date[is_men])['Age'].min() }