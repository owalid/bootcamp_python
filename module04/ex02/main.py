from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
from ProportionBySport import proportionBySport
proportionBySport(data, 2004, 'Tennis', 'F')