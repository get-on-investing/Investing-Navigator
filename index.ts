#!/usr/bin/env node

interface NavigatorInput {
  investor: string;
  experienceLevel: string;
  portfolioReadiness: number;
  marketKnowledge: number;
  riskAssessment: number;
  wealthBuilding: number;
  investmentEducation: number;
  marketNavigation: number;
}

interface NavigatorOutput {
  investor: string;
  experienceLevel: string;
  portfolioReadinessScore: number;
  marketKnowledgeScore: number;
  riskAssessmentScore: number;
  wealthBuildingScore: number;
  investmentEducationScore: number;
  marketNavigationScore: number;
  overallNavigatorScore: number;
  priorityAction: string;
  investmentFocus: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    portfolioReadiness: "Portfolio Readiness",
    marketKnowledge: "Market Knowledge",
    riskAssessment: "Risk Assessment",
    wealthBuilding: "Wealth Building",
    investmentEducation: "Investment Education",
    marketNavigation: "Market Navigation",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getInvestmentFocus(overall: number, education: number): Record<string, number> {
  return {
    "Stocks & Equities": Math.min(100, Math.round(overall * 1.0)),
    "Bonds & Fixed Income": Math.min(100, Math.round(overall * 0.96)),
    "ETFs & Index Funds": Math.min(100, Math.round(education * 0.94)),
    "Real Estate (REITs)": Math.min(100, Math.round(overall * 0.91)),
  };
}

export function navigate(input: NavigatorInput): NavigatorOutput {
  const scores = {
    portfolioReadiness: input.portfolioReadiness,
    marketKnowledge: input.marketKnowledge,
    riskAssessment: input.riskAssessment,
    wealthBuilding: input.wealthBuilding,
    investmentEducation: input.investmentEducation,
    marketNavigation: input.marketNavigation,
  };
  const overallNavigatorScore = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    investor: input.investor,
    experienceLevel: input.experienceLevel.charAt(0).toUpperCase() + input.experienceLevel.slice(1),
    portfolioReadinessScore: input.portfolioReadiness,
    marketKnowledgeScore: input.marketKnowledge,
    riskAssessmentScore: input.riskAssessment,
    wealthBuildingScore: input.wealthBuilding,
    investmentEducationScore: input.investmentEducation,
    marketNavigationScore: input.marketNavigation,
    overallNavigatorScore,
    priorityAction: getPriorityAction(scores),
    investmentFocus: getInvestmentFocus(overallNavigatorScore, input.investmentEducation),
  };
}

const args = process.argv.slice(2);
const investor = args[0] || "investor-profile";
const experienceLevel = args[1] || "beginner";
const portfolioReadiness = parseInt(args[2]) || 75;
const marketKnowledge = parseInt(args[3]) || 68;
const riskAssessment = parseInt(args[4]) || 80;
const wealthBuilding = parseInt(args[5]) || 72;
const investmentEducation = parseInt(args[6]) || 85;
const marketNavigation = parseInt(args[7]) || 70;

const result = navigate({
  investor, experienceLevel, portfolioReadiness, marketKnowledge,
  riskAssessment, wealthBuilding, investmentEducation, marketNavigation,
});

console.log(`Investor: ${result.investor}`);
console.log(`Experience Level: ${result.experienceLevel}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Portfolio Readiness Score:     ${result.portfolioReadinessScore}/100  [${getStatus(result.portfolioReadinessScore)}]`);
console.log(`Market Knowledge Score:        ${result.marketKnowledgeScore}/100  [${getStatus(result.marketKnowledgeScore)}]`);
console.log(`Risk Assessment Score:         ${result.riskAssessmentScore}/100  [${getStatus(result.riskAssessmentScore)}]`);
console.log(`Wealth Building Score:         ${result.wealthBuildingScore}/100  [${getStatus(result.wealthBuildingScore)}]`);
console.log(`Investment Education Score:    ${result.investmentEducationScore}/100  [${getStatus(result.investmentEducationScore)}]`);
console.log(`Market Navigation Score:       ${result.marketNavigationScore}/100  [${getStatus(result.marketNavigationScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Navigator Score:       ${result.overallNavigatorScore}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nInvestment Focus Areas:");
Object.entries(result.investmentFocus).forEach(([area, score]) => {
  console.log(`  ${area.padEnd(24)} ${score}/100`);
});
