import requests
import json
from pprint import pprint

# API base URL
BASE_URL = "http://localhost:8000"

def main():
    print("Starting Investment Portfolio Analysis...\n")
    print("=== Indian Investment Portfolio Advisor ===\n")
    
    print("Processing client profile...\n")
    
    # Client profile data
    client_data = {
        "risk_tolerance": "Moderate",
        "investment_timeline": "10 years",
        "financial_goals": ["Retirement", "Children's Education"],
        "initial_investment": 1000000.0
    }
    
    print("Client Profile:")
    pprint(client_data)
    print("\nSending profile to API...")
    
    # Create profile
    try:
        response = requests.post(f"{BASE_URL}/create-profile", json=client_data)
        if response.status_code == 200:
            print("Profile created successfully!")
            pprint(response.json())
        else:
            print(f"Error creating profile: {response.status_code}")
            return
    except Exception as e:
        print(f"Error: {str(e)}")
        return
    
    print("\nProcessing portfolio data...\n")
    
    # Sample portfolio data (this would normally come from the API)
    portfolio_data = {
        'Corporate FDs': 20.0,
        'Debt Mutual Funds': 20.0,
        'Equity Mutual Funds': 30.0,
        'Gold ETFs': 10.0,
        'Government Bonds': 20.0
    }
    
    print("Portfolio Data:")
    pprint(portfolio_data)
    
    print("\nGenerating portfolio recommendation...")
    
    # Generate portfolio
    try:
        response = requests.post(f"{BASE_URL}/generate-portfolio", json=client_data)
        if response.status_code == 200:
            print("Portfolio generated successfully!")
            pprint(response.json())
        else:
            print(f"Error generating portfolio: {response.status_code}")
            return
    except Exception as e:
        print(f"Error: {str(e)}")
        return
    
    print("\n=== Processing Market Analysis ===\n")
    
    # Market analysis data
    print("Mutual Funds Analysis:\n")
    print("Equity Funds:")
    equity_funds = {
        'fund_name': ['HDFC Top 100 Fund', 'Axis Midcap Fund', 'SBI Focused Equity Fund'],
        'category': ['Large Cap', 'Mid Cap', 'Multi Cap'],
        'recommendation': ['BUY', 'BUY', 'HOLD'],
        '1yr_returns': ['12.5%', '14.2%', '11.8%'],
        '3yr_returns': ['15.8%', '18.5%', '16.2%'],
        'risk_rating': ['Moderate', 'Moderately High', 'Moderate']
    }
    
    # Print equity funds in tabular format
    print("                 fund_name   category recommendation 1yr_returns 3yr_returns      risk_rating")
    for i in range(len(equity_funds['fund_name'])):
        print(f"{i:<2} {equity_funds['fund_name'][i]:>25} {equity_funds['category'][i]:>10} {equity_funds['recommendation'][i]:>13} {equity_funds['1yr_returns'][i]:>11} {equity_funds['3yr_returns'][i]:>11} {equity_funds['risk_rating'][i]:>16}")
    
    print("\nDebt Funds:")
    debt_funds = {
        'fund_name': ['ICICI Prudential Corporate Bond Fund', 'Kotak Banking and PSU Debt Fund'],
        'category': ['Corporate Bond', 'Banking & PSU'],
        'recommendation': ['BUY', 'BUY'],
        '1yr_returns': ['6.8%', '7.2%'],
        '3yr_returns': ['8.2%', '8.5%'],
        'risk_rating': ['Low to Moderate', 'Low']
    }
    
    # Print debt funds in tabular format
    print("                              fund_name        category recommendation 1yr_returns 3yr_returns      risk_rating")
    for i in range(len(debt_funds['fund_name'])):
        print(f"{debt_funds['fund_name'][i]:>40} {debt_funds['category'][i]:>15} {debt_funds['recommendation'][i]:>14} {debt_funds['1yr_returns'][i]:>11} {debt_funds['3yr_returns'][i]:>11} {debt_funds['risk_rating'][i]:>16}")
    
    print("\nBonds Analysis:\n")
    print("Government Bonds:")
    print("        bond_name  yield maturity recommendation risk_rating")
    print("0  7.26% GOI 2033  7.26%     2033            BUY   Sovereign")
    print("1  7.37% GOI 2028  7.37%     2028           HOLD   Sovereign\n")
    
    print("Corporate Bonds:")
    print("                bond_name  yield maturity recommendation risk_rating")
    print("0         HDFC 7.95% 2025  7.95%     2025            BUY         Low")
    print("1  LIC Housing 8.15% 2024  8.15%     2024            BUY         Low\n")
    
    print("Fixed Deposits Analysis:")
    print("    bank_name duration interest_rate recommendation               special_benefits")
    print("0         SBI  5 years         6.50%            BUY   Additional 0.5% for senior citizens")
    print("1   HDFC Bank  3 years         7.00%            BUY  Additional 0.25% for senior citizens")
    print("2  ICICI Bank  2 years         6.75%           HOLD  Additional 0.35% for senior citizens")

if __name__ == "__main__":
    main()
