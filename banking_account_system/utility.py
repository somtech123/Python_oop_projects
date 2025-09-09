"""
To calculate compound interest with a monthly deposit, you need to consider two components:

Compound interest on the initial principal

Future value of a series of monthly contributions

FV=P×(1+nr​)nt+PMT×[nr​(1+nr​)nt−1​]

Where:

FV = Future Value (total amount after time period)

P = Initial principal (starting amount)

r = Annual interest rate (decimal, so 5% = 0.05)

n = Number of times interest is compounded per year (monthly = 12)

t = Time in years

PMT = Monthly deposit amount

"""

class CompoundInterestCalculator:
    def __init__(self):
        pass

    @staticmethod
    def futureValue(principal_deposit: float, monthly_deposite_amount: float, interest_rate: float, time: int, compounded_per_year = 12) -> float:
      
        percent_interest = interest_rate / 100
         # Compound factor
        compound_factor = (1 + percent_interest / compounded_per_year) ** (compounded_per_year * time)

        #Future value principle

        FV_principle = principal_deposit * compound_factor

        FV_deposit = monthly_deposite_amount * ((compound_factor - 1) / (percent_interest / compounded_per_year))

        Fv_total = FV_principle + FV_deposit

        return round(Fv_total, 2)
    



    @staticmethod
    def interest_earned(principal_deposit: float, monthly_deposite_amount: float, interest_rate: float, time: int) -> float:

        total_contribution = principal_deposit + (monthly_deposite_amount * 12 * time)
        fv = CompoundInterestCalculator.futureValue(principal_deposit, monthly_deposite_amount, interest_rate, time)
        interest_earned = fv - total_contribution

        return round(interest_earned)
    
    @staticmethod
    def compound_value(principal_deposit: float, annual_interest: float, time: int) :
        percent_interest = annual_interest / 100
        time = 1 if time == 0 else time
        #number of quater = year * 4

        compunding_period = time * 4
        coumpound_value_time = time * compunding_period
        coumpound_factor = (1 + percent_interest / compunding_period) ** coumpound_value_time
        coumpound_total = principal_deposit * coumpound_factor
        return round(coumpound_total, 2)
    
    @staticmethod
    def coumpound_interest_earned(principal_deposit: float, annual_interest: float, time: int):

        amount = CompoundInterestCalculator.compound_value(principal_deposit, annual_interest, time) 
        compunding_interest = amount - principal_deposit
        return round(compunding_interest, 2)
    

    








