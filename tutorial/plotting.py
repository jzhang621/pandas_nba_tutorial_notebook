# TODO: move this to a utility function which will be

import matplotlib.pyplot as plt
import seaborn as sns


def box_and_strip(stat, advanced):
    sns.boxplot(x="POS", y=stat, order=['PG', 'SG', 'SF', 'PF', 'C'],
                data=advanced, palette="Set3", width=0.5)

    sns.stripplot(x="POS", y=stat, order=['PG', 'SG', 'SF', 'PF', 'C'],
                  data=advanced, jitter=True, palette="Set3", split=True, linewidth=1, edgecolor='gray')


def shorten_name(name):
    return " ".join(name.split(' ')[1:])


TEAM_COLORS = {
    'CLE': {
        'pos': '#FDBB30FF',
        'neg': '#FDBB3075',
    },
    'PHX': {
        'pos': '#1D1160FF',
        'neg': '#1D116064'
    },
    'CHI': {
        'pos': '#CE1141FF',
        'neg': '#CE114164'
    },
    'TOR': {
        'pos': '#CE1141FF',
        'neg': '#CE114164'
    },
    'GS': {
        'pos': '#006BB6FF',
        'neg': '#006BB664'
    },
    'MIL': {
        'pos': '#00471BFF',
        'neg': '#00471B64'
    },
    'DEN': {
        'pos': '#FEC524FF',
        'neg': '#FEC52464'
    },
    'NO': {
        'pos': '#00471BFF',
        'neg': '#00471B64'
    },
    'NY': {
        'pos': '#F58426FF',
        'neg': '#F5842664'
    }
}


def plot_metric(team_data, metric, ax):
    sorted_team_data = team_data.sort_values(by=metric, ascending=True)
    sorted_team_data['short_names'] = sorted_team_data.PLAYER.apply(shorten_name)
    team_name = set(team_data.index.values).pop()

    avg_value = 0 if metric == 'RPM' else 15

    pos_color = TEAM_COLORS[team_name]['pos']
    neg_color = TEAM_COLORS[team_name]['neg']

    sorted_team_data['color'] = sorted_team_data[metric].apply(lambda x: pos_color if x > avg_value else neg_color)

    title = '{0}: {1}'.format(metric, team_name)

    sorted_team_data.plot(kind='barh', x='short_names',
                          y=metric, color=sorted_team_data.color,
                          ax=ax, figsize=(16, 4), legend=False, title=title)
    ax.set_ylabel('')


def plot_team(team_data):
    fig, axs = plt.subplots(1, 2)
    plot_metric(team_data, 'RPM', ax=axs[0])
    plot_metric(team_data, 'PER', ax=axs[1])


def plot_teams(teams, data):
    fig, axs = plt.subplots(3, 2)

    for idx, team in enumerate(teams):
        team_data = data.loc[team]
        plot_metric(team_data, 'RPM', ax=axs[idx][0])
        plot_metric(team_data, 'PER', ax=axs[idx][1])
