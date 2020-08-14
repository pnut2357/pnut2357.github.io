---
title: Calculating the Balance in Your Retirement Account (GUI)
description: Wealth calculation at retirement
categories:
  - python
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Wealth calculation at retirement / GUI
# header:
#   image: /assets/images/logos/logo-text-8c3ba8a6.svg
---
# Problem
What age do you plan to retire? Whatever your age when you decide to retire, you have to consider  
- how much you contribute to your retirement account,
- how much you would set your retirement spending.


I created Wealth calculator at retirement, using GUI.
> If you are interested in creating your own GUI, please check this [tutorial](https://realpython.com/python-gui-tkinter/).

The program calculates and outputs the average balance in your retirement bank account out of 10 repeats at the time when you would retire, showing 10 plots of the balances as functions of number of years. A User can clicks the calculation button multiple times. Then, the plots vary depending on a measure of annual volatility of the investment (Std Dev).

## Inputs

1. Mean Return (%): estimate the average annual return of the investment above inflation. (Personal estimation: 5)
2. Std Dev Return (%): estimate the measure of the annual volatility of the investment (Personal estimation: 10)
3. Yearly Contribution ($): estimate how much you want to save your money annually (Personal estimation: $10000)
4. No. of Years of Contribution: estimate how many years you would save (Personal estimation: 40 yrs)
5. No. of Years to Retirement: estimate how many years later you would set your retirement year (Personal estimation: 40 yrs)
6. Annual Spend in Retirement ($): estimate your retirement spending (Personal estimation: $100000)

# Result
![tw_webpage](/assets/images/Retirement/result.png){:height="800px" width="600px"}  
| Fig1. Result of my Retirement Plan |

If I set up my retirement year for 40 years later, I will be broke around 10 years since my retirement year. I need to either increase my contribution or limit my retirement spending. :(

If you are interested in playing with this, or even what formulae I used and how I implemented python GUI, please check my [github](https://github.com/pnut2357/Retirement_Plan_Caulator_GUI)
