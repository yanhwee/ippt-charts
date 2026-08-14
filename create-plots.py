from functools import partial
from itertools import chain
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Globals

PLOT_OUTPUT_FOLDER = os.path.join(os.getcwd(), 'plots')

MEN_PUSHUPS = pd.read_csv('scores-pushup-men.csv', index_col=0)
MEN_SITUPS = pd.read_csv('scores-situp-men.csv', index_col=0)
MEN_RUNS = pd.read_csv('scores-run-men.csv', index_col=0)

WOMEN_PUSHUPS = pd.read_csv('scores-pushup-women.csv', index_col=0)
WOMEN_SITUPS = pd.read_csv('scores-situp-women.csv', index_col=0)
WOMEN_RUNS = pd.read_csv('scores-run-women.csv', index_col=0)

AGES = MEN_PUSHUPS.columns

# Seaborn Configuration

sns.set_theme(style="whitegrid", font="sans-serif")

# Single Line Plot

def create_line_plot(series, color, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax = sns.lineplot(ax=ax, data=series, color=color)
    ax.set_title(title, pad=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.grid(visible=True, which='minor', linestyle=':', alpha=0.9)
    return fig

def create_men_pushup_plot(age):
    return create_line_plot(
        series=MEN_PUSHUPS[age],
        color='#1F77B4',
        title=f'Push-up Scores (Age {age}) (Servicemen)',
        xlabel='Repetitions',
        ylabel='Score'
    )

def create_men_situp_plot(age):
    return create_line_plot(
        series=MEN_SITUPS[age],
        color='#FF7F0E',
        title=f'Sit-up Scores (Age {age}) (Servicemen)',
        xlabel='Repetitions',
        ylabel='Score'
    )

def create_men_run_plot(age):
    return create_line_plot(
        series=MEN_RUNS[age],
        color='#2CA02C',
        title=f'2.4km Scores (Age {age}) (Servicemen)',
        xlabel='Time (in secs)',
        ylabel='Score'
    )

def create_women_pushup_plot(age):
    return create_line_plot(
        series=WOMEN_PUSHUPS[age],
        color='#56B4E9',
        title=f'Bent-Knee Push-up Scores (Age {age}) (Servicewomen)',
        xlabel='Repetitions',
        ylabel='Score'
    )

def create_women_situp_plot(age):
    return create_line_plot(
        series=WOMEN_SITUPS[age],
        color='#E69F00',
        title=f'Sit-up Scores (Age {age}) (Servicewomen)',
        xlabel='Repetitions',
        ylabel='Score'
    )

def create_women_run_plot(age):
    return create_line_plot(
        series=WOMEN_RUNS[age],
        color='#009E73',
        title=f'2.4km Scores (Age {age}) (Servicewomen)',
        xlabel='Time (in secs)',
        ylabel='Score'
    )

# Multi Line Plot

def create_multi_line_plot(dataframe, title, xlabel, ylabel, legend_loc):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.lineplot(ax=ax, data=dataframe)
    ax.set_title(title, pad=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    sns.move_legend(ax, loc=legend_loc)
    return fig

def create_men_multi_pushup_plot():
    return create_multi_line_plot(
        dataframe=MEN_PUSHUPS,
        title='Push-up Scores (All Ages) (Servicemen)',
        xlabel='Repetitions',
        ylabel='Score',
        legend_loc='lower right'
    )

def create_men_multi_situp_plot():
    return create_multi_line_plot(
        dataframe=MEN_SITUPS,
        title='Sit-up Scores (All Ages) (Servicemen)',
        xlabel='Repetitions',
        ylabel='Score',
        legend_loc='lower right'
    )

def create_men_multi_run_plot():
    return create_multi_line_plot(
        dataframe=MEN_RUNS,
        title='2.4km Scores (All Ages) (Servicemen)',
        xlabel='Time (in secs)',
        ylabel='Score',
        legend_loc='lower left'
    )

def create_women_multi_pushup_plot():
    return create_multi_line_plot(
        dataframe=WOMEN_PUSHUPS,
        title='Bent-Knee Push-up Scores (All Ages) (Servicewomen)',
        xlabel='Repetitions',
        ylabel='Score',
        legend_loc='lower right'
    )

def create_women_multi_situp_plot():
    return create_multi_line_plot(
        dataframe=WOMEN_SITUPS,
        title='Sit-up Scores (All Ages) (Servicewomen)',
        xlabel='Repetitions',
        ylabel='Score',
        legend_loc='lower right'
    )

def create_women_multi_run_plot():
    return create_multi_line_plot(
        dataframe=WOMEN_RUNS,
        title='2.4km Scores (All Ages) (Servicewomen)',
        xlabel='Time (in secs)',
        ylabel='Score',
        legend_loc='lower left'
    )

# Save Plots

def get_age_label(age):
    if age == '<22': # in case '<' is not allowed for filenames
        return '0-22'
    return age

def plot_and_save_svgs():
    os.makedirs(PLOT_OUTPUT_FOLDER, exist_ok=True)

    create_multi_line_plots = [
        (create_men_multi_pushup_plot, 'men_pushup_scores_all'),
        (create_men_multi_situp_plot, 'men_situp_scores_all'),
        (create_men_multi_run_plot, 'men_run_scores_all'),
        (create_women_multi_pushup_plot, 'women_pushup_scores_all'),
        (create_women_multi_situp_plot, 'women_situp_scores_all'),
        (create_women_multi_run_plot, 'women_run_scores_all')
    ]

    create_single_line_plots = chain.from_iterable((lambda age, age_label: (
        (partial(create_men_pushup_plot, age), f'men_pushup_scores_{age_label}'),
        (partial(create_men_situp_plot, age), f'men_situp_scores_{age_label}'),
        (partial(create_men_run_plot, age), f'men_run_scores_{age_label}'),
        (partial(create_women_pushup_plot, age), f'women_pushup_scores_{age_label}'),
        (partial(create_women_situp_plot, age), f'women_situp_scores_{age_label}'),
        (partial(create_women_run_plot, age), f'women_run_scores_{age_label}'),
    ))(age, get_age_label(age)) for age in AGES)

    create_plots = chain(create_multi_line_plots, create_single_line_plots)

    for create_plot, filename in create_plots:
        fig = create_plot()
        filepath = os.path.join(PLOT_OUTPUT_FOLDER, f'{filename}.svg')
        fig.savefig(filepath, bbox_inches='tight')
        plt.close(fig)

if __name__ == '__main__':
    plot_and_save_svgs()

