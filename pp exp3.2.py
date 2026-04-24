def calculate_emi(principal, annual_rate, years):
    R = annual_rate / (12 * 100)   
    N = years * 12                 
    
    EMI = (principal * R * (1 + R)**N) / ((1 + R)**N - 1)
    return EMI

# Example
emi = calculate_emi(100000, 10, 2)
print("Monthly EMI:", round(emi, 2))

