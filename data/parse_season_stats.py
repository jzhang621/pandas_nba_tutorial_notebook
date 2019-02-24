import pandas as pd

data = pd.read_csv('season_stats.csv')

diff = data[['PW', 'PL', 'W', 'L', 'Team']]
diff.set_index('Team', inplace=True)
diff['difference'] = diff['PW'] - diff['W']
