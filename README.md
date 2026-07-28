# Investing Navigator 📈🧭

[![npm](https://img.shields.io/npm/v/@get-on-investing/investing-navigator)](https://npmjs.com/package/@get-on-investing/investing-navigator)
[![PyPI](https://img.shields.io/pypi/v/investing-navigator)](https://pypi.org/project/investing-navigator)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Investing Navigator is an intelligent investing assistant from Get On Investing that helps users explore investment opportunities, understand financial concepts, and navigate the markets with greater confidence. Built by [GetOnInvesting.com](https://getoninvesting.com).

## Features

- Portfolio Readiness Score — evaluates investment portfolio structure and diversification
- Market Knowledge Score — measures understanding of financial markets and instruments
- Risk Assessment Score — evaluates risk tolerance and portfolio risk alignment
- Wealth Building Score — tracks progress toward long-term wealth building goals
- Investment Education Score — measures financial literacy and investing knowledge
- Market Navigation Score — evaluates ability to navigate market conditions confidently
- CLI support in Node.js and Python
- Benchmark dataset included (20 investor profile cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @get-on-investing/investing-navigator
npx investing-navigator "investor-profile" beginner 75 68 80 72 85 70
```

### Python

```bash
pip install investing-navigator
python -m navigator "investor-profile" beginner 75 68 80 72 85 70
```

## Output

```
Investor: investor-profile
Experience Level: Beginner
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Portfolio Readiness Score:     75 / 100  [Healthy]
Market Knowledge Score:        68 / 100  [Healthy]
Risk Assessment Score:         80 / 100  [Healthy]
Wealth Building Score:         72 / 100  [Healthy]
Investment Education Score:    85 / 100  [Excellent]
Market Navigation Score:       70 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Navigator Score:       75 / 100
Priority Action:               Market Knowledge (lowest — act first)

Investment Focus Areas:
  Stocks & Equities:      75 / 100
  Bonds & Fixed Income:   72 / 100
  ETFs & Index Funds:     80 / 100
  Real Estate (REITs):    68 / 100
```

## Investor Experience Levels

| Level | Description |
|-------|-------------|
| beginner | New to investing — learning fundamentals |
| intermediate | Some experience — building portfolio |
| advanced | Experienced — optimising strategies |
| expert | Professional — managing complex portfolios |

## Project Structure

```
Investing-Navigator/
├── index.ts              # TypeScript navigator
├── navigator.py          # Python navigator
├── setup.py              # PyPI setup config
├── pyproject.toml        # PyPI build config
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── investing_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Investment Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Portfolio Readiness | Portfolio structure and diversification | 0–100 |
| Market Knowledge | Understanding of financial markets | 0–100 |
| Risk Assessment | Risk tolerance and portfolio alignment | 0–100 |
| Wealth Building | Progress toward long-term wealth goals | 0–100 |
| Investment Education | Financial literacy and investing knowledge | 0–100 |
| Market Navigation | Ability to navigate market conditions | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate learning intervention required |
| 31–60 | At Risk | Active education and guidance needed |
| 61–80 | Healthy | On track — continue building knowledge |
| 81–100 | Excellent | Strong investor — ready for advanced strategies |

## Keywords

Investing Navigator · Investment Assistant · Portfolio Planning · Financial Education · Market Navigation · Wealth Building · Investment Learning · Get On Investing

## Links

| Platform | URL |
|----------|-----|
| Website | https://getoninvesting.com |
| GitHub | https://github.com/get-on-investing/Investing-Navigator |
| GitHub Pages | https://get-on-investing.github.io/Investing-Navigator/ |
| NPM | https://npmjs.com/package/@get-on-investing/investing-navigator |
| PyPI | https://pypi.org/project/investing-navigator |
| Hugging Face | https://huggingface.co/datasets/get-on-investing/investing-navigator-benchmarks |
| Kaggle | https://kaggle.com/datasets/getoninvesting/investing-navigator-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://investing-navigator.readthedocs.io |

## About GetOnInvesting.com

GetOnInvesting.com is an intelligent investing platform helping users explore investment opportunities, understand financial concepts, and navigate the markets with greater confidence through organised investing knowledge, portfolio insights, and practical guidance.

## License

MIT — [GetOnInvesting.com](https://getoninvesting.com)
