import pandas as pd

def proportionBySport(data_set, year, sport, gender):
  is_ = data_set['Year'] == year
  year_group = data_set[is_]
  gender_group = year_group['Sex'] == gender
  sport_group = year_group['Sport'] == sport

  all_sport = year_group[gender_group]
  one_sport = year_group[(sport_group) & (gender_group)]


  return len(one_sport) / len(all_sport)


# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load('../data/athlete_events.csv')
# from ProportionBySport import proportionBySport
# proportionBySport(data, 2004, 'Tennis', 'F')