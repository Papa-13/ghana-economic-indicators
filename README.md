# 🇬🇭 Ghana Rising: An Economic Data Story
### Tracking Development, Digital Growth & Financial Inclusion (2000–2024)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![World Bank](https://img.shields.io/badge/Data-World%20Bank%20Open%20Data-brightgreen)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Personal Note

This project is personal. I grew up between Ghana and the UK — and I've seen firsthand what economic progress looks like at ground level in the Ashanti Region, and what it looks like in the data. I've also led digital literacy outreach reaching 950+ secondary school students across Ghana, and my MSc dissertation measured energy poverty in UK smart meter data.

This analysis bridges those worlds — using public data to tell an honest story about where Ghana has come from, where it is, and what the numbers say about what comes next.

---

## 📌 Project Overview

Ghana is one of Africa's most studied development success stories — and one of its most complicated. It reached lower-middle-income status in 2011, survived a debt crisis in 2022, and has built one of West Africa's most active mobile money ecosystems, all while managing significant inequality between regions.

This project uses **World Bank Open Data** to explore four interconnected themes across 25 years of economic history.

---

## 🎯 Key Questions Explored

| # | Question |
|---|----------|
| 1 | How has Ghana's GDP growth trajectory compared to Sub-Saharan Africa averages? |
| 2 | Has economic growth translated into poverty reduction — and for whom? |
| 3 | How fast is Ghana digitising, and what does financial inclusion look like on the ground? |
| 4 | What does energy access data reveal about development inequality across Ghana? |

---

## 📂 Project Structure

```
ghana-economic-indicators/
│
├── 📓 notebooks/
│   ├── 01_gdp_growth_trends.ipynb          # GDP, growth rate, sectoral shifts
│   ├── 02_poverty_and_inequality.ipynb     # Poverty headcount, Gini, HDI
│   ├── 03_digital_financial_inclusion.ipynb # Mobile money, internet, banking
│   └── 04_energy_access_development.ipynb  # Electricity access, energy poverty
│
├── 📊 data/
│   ├── raw/                                # Downloaded from World Bank API
│   └── processed/                         # Cleaned, analysis-ready CSVs
│
├── 📁 outputs/
│   └── figures/                            # All exported charts
│
├── 🛠️ src/
│   ├── wb_loader.py                        # World Bank API wrapper
│   └── plot_utils.py                       # Consistent chart styling (Ghana palette)
│
├── requirements.txt
└── README.md
```

---

## 📦 Data Sources

All data is **freely available** — no account required.

| Source | Dataset | Access |
|--------|---------|--------|
| **World Bank Open Data** | GDP, poverty, Gini, health, education | [data.worldbank.org](https://data.worldbank.org) |
| **World Bank API** | Programmatic access via `wbdata` Python library | `pip install wbdata` |
| **Ghana Statistical Service** | National census & household survey data | [statsghana.gov.gh](https://statsghana.gov.gh) |
| **GSMA Intelligence** | Mobile money & connectivity statistics | [gsma.com/solutions](https://www.gsma.com) |
| **Our World in Data** | Long-run poverty & energy access series | [ourworldindata.org](https://ourworldindata.org) |

---

## 🔍 Analysis Highlights

### 1. GDP & Growth Trajectory
- Ghana's GDP grew 14× between 2000 and 2022 in nominal terms — but growth has been volatile
- The 2011 oil boom created a one-off spike; post-oil growth has been more structurally driven
- Ghana's per capita growth has outpaced Sub-Saharan Africa average in 18 of the last 24 years

### 2. Poverty & Inequality
- National poverty headcount fell from ~52% (2000) to ~23% (2017) — a significant achievement
- The North-South inequality gap has narrowed but remains stark
- Gini coefficient has held stubbornly above 0.40 — growth has not been fully inclusive

### 3. Digital Financial Inclusion
- Ghana's mobile money transaction volume grew over 1,000% between 2012 and 2022
- Internet penetration reached ~60% by 2023 — but urban-rural divide remains wide
- Formal bank account ownership doubled in a decade yet 40%+ of adults remain unbanked

### 4. Energy Access & Development
- National electrification rate crossed 80% in the late 2010s — ahead of most West African peers
- Rural electrification still lags urban by 30+ percentage points
- Energy access improvements correlate strongly with school enrolment and health outcomes

---

## 📈 Sample Visualisations

- 📉 Ghana GDP per capita vs SSA average (2000–2023) — dual-line chart
- 🌍 Poverty headcount trend with key policy milestones annotated
- 📱 Mobile money growth trajectory vs bank account ownership
- ⚡ Urban vs rural electricity access gap over time
- 🔥 Correlation matrix: energy access, education, health outcomes

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Papa-13/ghana-economic-indicators.git
cd ghana-economic-indicators
```

### 2. Set up environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Fetch data (automated)
```bash
python src/wb_loader.py
```
This pulls all World Bank indicators directly via API and saves to `data/raw/`.

### 4. Run notebooks in order
```bash
jupyter lab
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| `wbdata` | World Bank API client |
| `pandas` | Data wrangling |
| `numpy` | Numerical operations |
| `matplotlib` / `seaborn` | Static visualisations |
| `plotly` | Interactive charts |
| `scipy` | Correlation analysis |
| `jupyter` | Notebook environment |

---

## 💡 Key Takeaways

1. **Growth ≠ inclusion** — Ghana's headline GDP numbers mask significant regional and urban-rural inequality
2. **Mobile money is the real financial inclusion story** — not bank accounts
3. **Energy access is a development multiplier** — improvements in electrification track closely with education and health gains
4. **The debt crisis of 2022 reversed years of fiscal progress** — the data tells a cautionary tale about commodity dependence

---

## 🔗 Related Projects

- [`uk-consumer-credit-eda`](https://github.com/Papa-13/uk-consumer-credit-eda) — UK lending patterns & credit exclusion analysis
- [`energy-poverty-detection-ml`](https://github.com/Papa-13/energy-poverty-detection-ml) — XGBoost on 167M UK smart meter observations

---

## 👤 Author

**Papa Kwadwo Bona Owusu**  
Data Scientist | ML Engineer  
Co-Founder & CEO, DigiTech Edge Solutions  
MSc Applied AI & Data Science | MSc Business Analytics  


---

## 📄 License

MIT License — free to use, adapt, and build on with attribution.
