"""
src/plot_utils.py
─────────────────
Reusable chart styling helpers — Ghana national colour palette.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── Ghana flag palette + accents ───────────────────────────────────────────────
GHANA_RED    = '#CE1126'
GHANA_GOLD   = '#FCD116'
GHANA_GREEN  = '#006B3F'
GHANA_BLACK  = '#000000'
ACCENT_BLUE  = '#2563EB'
GREY_MID     = '#9CA3AF'

PALETTE = [GHANA_GREEN, GHANA_RED, GHANA_GOLD, ACCENT_BLUE, GHANA_BLACK]

# Key policy/event annotations for Ghana
GHANA_EVENTS = {
    '2007': 'Oil discovery',
    '2011': 'Oil production\nbegins',
    '2017': 'Banking sector\ncrisis',
    '2020': 'COVID-19',
    '2022': 'IMF debt\nrestructuring',
}


def apply_style():
    """Apply consistent chart style across all notebooks."""
    plt.rcParams.update({
        'figure.figsize':    (12, 5),
        'font.family':       'DejaVu Sans',
        'axes.spines.top':   False,
        'axes.spines.right': False,
        'axes.grid':         True,
        'grid.alpha':        0.25,
        'grid.linestyle':    '--',
    })
    sns.set_palette(PALETTE)


def annotate_events(ax, events: dict, y_pos: float, color: str = GREY_MID):
    """Add vertical event lines with labels to a time-series chart."""
    for year_str, label in events.items():
        ax.axvline(int(year_str), color=color, linestyle=':', linewidth=1, alpha=0.7)
        ax.text(int(year_str) + 0.1, y_pos, label, fontsize=7.5,
                color=color, va='top', rotation=90)


def save_fig(fig, filename: str, dpi: int = 150):
    """Save figure to outputs/figures/ folder."""
    path = f'../outputs/figures/{filename}'
    fig.savefig(path, dpi=dpi, bbox_inches='tight')
    print(f'Saved → {path}')


def format_pct(ax, axis='y'):
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}%')) \
        if axis == 'y' else \
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}%'))


def format_usd(ax, axis='y', unit='bn'):
    divisor = 1e9 if unit == 'bn' else 1e6
    label = f'${{}:.1f}{unit}'
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: label.format(x / divisor)))
