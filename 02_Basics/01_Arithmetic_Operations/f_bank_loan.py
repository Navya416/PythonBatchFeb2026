"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""

# Compound Interest

P = float(input("Enter Principal Amount: "))
r = float(input("Enter Annual Interest Rate (e.g., 0.08): "))
n = int(input("Enter Number of Compounds per Year: "))
t = int(input("Enter Time (years): "))

A = P * (1 + r / n) ** (n * t)

print("Final Amount:", round(A, 2))

