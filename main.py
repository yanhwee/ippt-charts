import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Globals

PLOT_OUTPUT_FOLDER = os.path.join(os.get_cwd(), 'charts')

MEN_PUSHUPS = pd.read_csv('scores-pushup-men.csv', index_col=0)
MEN_SITUPS = pd.read_csv('scores-situp-men.csv', index_col=0)
MEN_RUNS = pd.read_csv('scores-run-men.csv', index_col=0)

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
        # color='#56B4E9',
        title=f'Pushup Scores (Age {age}) (for Servicemen)',
        xlabel='Repetition',
        ylabel='Score'
    )

def create_men_situp_plot(age):
    return create_line_plot(
        series=MEN_SITUPS[age],
        color='#FF7F0E',
        # color='#E69F00',
        title=f'Situp Scores (Age {age}) (for Servicemen)',
        xlabel='Repetition',
        ylabel='Score'
    )

def create_men_run_plot(age):
    return create_line_plot(
        series=MEN_RUNS[age],
        color='#2CA02C',
        # color='#009E73',
        title=f'Run Scores (Age {age}) (for Servicemen)',
        xlabel='Time (in secs)',
        ylabel='Score'
    )

# Multi Line Plot

def create_multi_line_plot(dataframe, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax = sns.lineplot(ax=ax, data=dataframe)
    ax.set_title(title, pad=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def create_men_multi_pushup_plot():
    return create_multi_line_plot(
        dataframe=MEN_PUSHUPS,
        title='Pushup Scores (All Ages) (for Servicemen)',
        xlabel='Repetition',
        ylabel='Score'
    )

def create_men_multi_situp_plot():
    return create_multi_line_plot(
        dataframe=MEN_SITUPS,
        title='Situp Scores (All Ages) (for Servicemen)',
        xlabel='Repetition',
        ylabel='Score'
    )

def create_men_multi_run_plot():
    return create_multi_line_plot(
        dataframe=MEN_RUNS,
        title='Run Scores (All Ages) (for Servicemen)',
        xlabel='Time (in secs)',
        ylabel='Score'
    )

# Save Plots

def create_plot_svgs():
    pass

if __name__ == '__main__':
    pass
