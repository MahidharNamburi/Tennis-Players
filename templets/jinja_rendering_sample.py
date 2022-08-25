import pandas as pd
from jinja2 import Environment, FileSystemLoader, Template


def getData(row):
    data = {
        'first_name':str(row['first_name']),
        'last_name':str(row['last_name']),
        'plays':str(row['plays']),
        'gender':str(row['gender']),
        'country':str(row['country']),
        'age':str(row['age']),
        'DOB':str(row['DOB']),
        'height':str(row['height']),
        'weight':str(row['weight']),
        'current_singles':str(row['current_singles']),
        'highest_singles':str(row['highest_singles']),
        'current_doubles':str(row['current_doubles']),
        'highest_doubles':str(row['highest_doubles']),
        'singles_main_tournaments':str(row['singles_main_tournaments']),
        'singles_lower_tournaments':str(row['singles_lower_tournaments']),
        'doubles_main_tournaments':str(row['doubles_main_tournaments']),
        'doubles_lower_tournaments':str(row['doubles_lower_tournaments']),
        'wins_singles':str(row['wins_singles']),
        'losses_singles':str(row['losses_singles']),
        'total_singles_matches':str(row['total_singles']),
        'reference':str(row['References']),
    }
    return data

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)
template = env.get_template('players.j2')
data = pd.read_csv("tennis players sample.csv")

ids = data['first_name'].tolist()

for i in range(len(ids)):
     text=template.render(getData(data.iloc[i]))
     print(text)
