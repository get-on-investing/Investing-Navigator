#!/usr/bin/env python3
"""
Investing Navigator
An intelligent investing assistant that helps users explore investment
opportunities, understand financial concepts, and navigate the markets
with greater confidence.
https://getoninvesting.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "portfolio_readiness": "Portfolio Readiness",
        "market_knowledge": "Market Knowledge",
        "risk_assessment": "Risk Assessment",
        "wealth_building": "Wealth Building",
        "investment_education": "Investment Education",
        "market_navigation": "Market Navigation",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_investment_focus(overall: int, education: int) -> dict:
    return {
        "Stocks & Equities": min(100, round(overall * 1.0)),
        "Bonds & Fixed Income": min(100, round(overall * 0.96)),
        "ETFs & Index Funds": min(100, round(education * 0.94)),
        "Real Estate (REITs)": min(100, round(overall * 0.91)),
    }


def navigate(
    investor: str,
    experience_level: str = "beginner",
    portfolio_readiness: int = 75,
    market_knowledge: int = 68,
    risk_assessment: int = 80,
    wealth_building: int = 72,
    investment_education: int = 85,
    market_navigation: int = 70,
) -> dict:
    """
    Navigate and score investor profile signals.

    Args:
        investor: Investor name or profile identifier
        experience_level: beginner, intermediate, advanced, or expert
        portfolio_readiness: Portfolio readiness score (0-100)
        market_knowledge: Market knowledge score (0-100)
        risk_assessment: Risk assessment score (0-100)
        wealth_building: Wealth building score (0-100)
        investment_education: Investment education score (0-100)
        market_navigation: Market navigation score (0-100)

    Returns:
        dict with individual signal scores, overall navigator score,
        and investment focus areas
    """
    scores = {
        "portfolio_readiness": portfolio_readiness,
        "market_knowledge": market_knowledge,
        "risk_assessment": risk_assessment,
        "wealth_building": wealth_building,
        "investment_education": investment_education,
        "market_navigation": market_navigation,
    }
    overall_navigator_score = round(sum(scores.values()) / 6)

    return {
        "investor": investor,
        "experience_level": experience_level.capitalize(),
        "portfolio_readiness_score": portfolio_readiness,
        "market_knowledge_score": market_knowledge,
        "risk_assessment_score": risk_assessment,
        "wealth_building_score": wealth_building,
        "investment_education_score": investment_education,
        "market_navigation_score": market_navigation,
        "overall_navigator_score": overall_navigator_score,
        "priority_action": get_priority_action(scores),
        "investment_focus": get_investment_focus(overall_navigator_score, investment_education),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    investor = args[0] if len(args) > 0 else "investor-profile"
    experience_level = args[1] if len(args) > 1 else "beginner"
    portfolio_readiness = int(args[2]) if len(args) > 2 else 75
    market_knowledge = int(args[3]) if len(args) > 3 else 68
    risk_assessment = int(args[4]) if len(args) > 4 else 80
    wealth_building = int(args[5]) if len(args) > 5 else 72
    investment_education = int(args[6]) if len(args) > 6 else 85
    market_navigation = int(args[7]) if len(args) > 7 else 70

    result = navigate(
        investor, experience_level, portfolio_readiness, market_knowledge,
        risk_assessment, wealth_building, investment_education, market_navigation
    )

    print(f"Investor: {result['investor']}")
    print(f"Experience Level: {result['experience_level']}")
    print("=" * 45)
    print(f"Portfolio Readiness Score:     {result['portfolio_readiness_score']}/100  [{get_status(result['portfolio_readiness_score'])}]")
    print(f"Market Knowledge Score:        {result['market_knowledge_score']}/100  [{get_status(result['market_knowledge_score'])}]")
    print(f"Risk Assessment Score:         {result['risk_assessment_score']}/100  [{get_status(result['risk_assessment_score'])}]")
    print(f"Wealth Building Score:         {result['wealth_building_score']}/100  [{get_status(result['wealth_building_score'])}]")
    print(f"Investment Education Score:    {result['investment_education_score']}/100  [{get_status(result['investment_education_score'])}]")
    print(f"Market Navigation Score:       {result['market_navigation_score']}/100  [{get_status(result['market_navigation_score'])}]")
    print("=" * 45)
    print(f"Overall Navigator Score:       {result['overall_navigator_score']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nInvestment Focus Areas:")
    for area, score in result['investment_focus'].items():
        print(f"  {area:<26} {score}/100")


if __name__ == "__main__":
    main()
