#!/usr/bin/env python
# coding: utf-8

# In[7]:


def simple_interest(principal, rate, time):
    """
    Function to calculate simple interest
    Formula: SI = (P * R * T) / 100
    """
    si = (principal * rate * time) / 100
    return si

def compound_interest(principal, rate, time, n=1):
    """
    Function to calculate compound interest
    Formula: CI = P * (1 + R / n)^(n * T) - P
    """
    amount = principal * (1 + rate / (n * 100))**(n * time)
    ci = amount - principal
    return ci

def main():
    print("Interest Calculator\n")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in %): "))
    time = float(input("Enter the time period (in years): "))

    # Corrected input string
    interest_type = input("Enter 'S' for Simple Interest or 'C' for Compound Interest: ").upper()

    if interest_type == 'S':
        si = simple_interest(principal, rate, time)
        print(f"Simple Interest = {si:.2f}")
    elif interest_type == 'C':
        n = int(input("Enter the number of times interest is compounded per year (default is 1): ") or 1)
        ci = compound_interest(principal, rate, time, n)
        print(f"Compound Interest = {ci:.2f}")
    else:
        print("Invalid input. Please enter 'S' or 'C'.")

if __name__ == "__main__":
    main()


# In[ ]:




