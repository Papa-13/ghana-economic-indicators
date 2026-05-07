"""
src/wb_loader.py
────────────────
Fetches all required World Bank indicators for Ghana via the wbdata API
and saves them as clean CSVs to data/raw/.

Run once before opening any notebook:
    python src/wb_loader.py
"""

import wbdata
import pandas as pd
from pathlib import Path
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────────────────
COUNTRY   = 'GHA'           # Ghana ISO code
SSA_CODE  = 'SSF'           # Sub-Saharan Africa aggregate
START     = datetime(2000, 1, 1)
END       = datetime(2023, 12, 31)
RAW_DIR   = Path(__file__).parent.parent / 'data' / 'raw'
RAW_DIR.mkdir(parents=True, exist_ok=True)

# ── Indicator sets ─────────────────────────────────────────────────────────────
INDICATORS = {

    # Notebook 1 — GDP & Growth
    'gdp': {
        'NY.GDP.MKTP.CD':    'gdp_current_usd',
        'NY.GDP.PCAP.CD':    'gdp_per_capita_usd',
        'NY.GDP.MKTP.KD.ZG': 'gdp_growth_pct',
        'NV.AGR.TOTL.ZS':    'agriculture_pct_gdp',
        'NV.IND.TOTL.ZS':    'industry_pct_gdp',
        'NV.SRV.TOTL.ZS':    'services_pct_gdp',
        'GC.DOD.TOTL.GD.ZS': 'debt_pct_gdp',
        'FP.CPI.TOTL.ZG':    'inflation_pct',
    },

    # Notebook 2 — Poverty & Inequality
    'poverty': {
        'SI.POV.DDAY':       'poverty_headcount_190',
        'SI.POV.LMIC':       'poverty_headcount_320',
        'SI.POV.GINI':       'gini_index',
        'HD.HCI.OVRL':       'human_capital_index',
        'SE.PRM.ENRR':       'primary_school_enrolment',
        'SE.SEC.ENRR':       'secondary_school_enrolment',
        'SP.DYN.IMRT.IN':    'infant_mortality_per_1000',
        'SH.XPD.CHEX.GD.ZS':'health_expenditure_pct_gdp',
    },

    # Notebook 3 — Digital & Financial Inclusion
    'digital': {
        'IT.NET.USER.ZS':    'internet_users_pct',
        'IT.CEL.SETS.P2':    'mobile_subscriptions_per_100',
        'FX.OWN.TOTL.ZS':   'bank_account_ownership_pct',
        'FX.OWN.TOTL.FE.ZS':'bank_account_female_pct',
        'FX.OWN.TOTL.MA.ZS':'bank_account_male_pct',
        'FB.ATM.TOTL.P5':   'atms_per_100k',
        'FB.CBK.BRCH.P5':   'bank_branches_per_100k',
    },

    # Notebook 4 — Energy & Development
    'energy': {
        'EG.ELC.ACCS.ZS':   'electricity_access_pct',
        'EG.ELC.ACCS.RU.ZS':'electricity_rural_pct',
        'EG.ELC.ACCS.UR.ZS':'electricity_urban_pct',
        'EG.USE.PCAP.KG.OE':'energy_use_per_capita_kgoe',
        'EG.ELC.RNEW.ZS':   'renewable_electricity_pct',
        'EN.ATM.CO2E.PC':   'co2_emissions_per_capita',
    },
}


def fetch_indicators(indicator_dict: dict, countries: list, label: str) -> pd.DataFrame:
    """Fetch a set of indicators for given countries and return as a tidy DataFrame."""
    print(f'Fetching: {label}...')
    try:
        df = wbdata.get_dataframe(
            indicator_dict,
            country=countries,
            date=(START, END),
        )
        df = df.reset_index()
        df.columns.name = None
        # Rename indicator columns
        df = df.rename(columns=indicator_dict)
        print(f'  ✅ {len(df)} rows fetched')
        return df
    except Exception as e:
        print(f'  ❌ Error fetching {label}: {e}')
        return pd.DataFrame()


def main():
    print('=' * 55)
    print('Ghana Economic Indicators — World Bank Data Fetch')
    print('=' * 55)

    countries = [COUNTRY, SSA_CODE]

    for name, indicators in INDICATORS.items():
        df = fetch_indicators(indicators, countries, name)
        if not df.empty:
            out_path = RAW_DIR / f'{name}_indicators.csv'
            df.to_csv(out_path, index=False)
            print(f'  💾 Saved → {out_path.name}')

    print('\nAll done! Data saved to data/raw/')
    print('You can now open the notebooks in order (01 → 04).')


if __name__ == '__main__':
    main()
