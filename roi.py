class House:

    def __init__(self, monthly_income = 0, total_expenses = 0, total_investment = 0, monthly_cash_flow = 0, down_payment = 0, closing_costs = 0):
        self.monthly_income = monthly_income
        self.total_expenses = total_expenses
        self.total_investment = total_investment
        self.monthly_cash_flow = monthly_cash_flow
        self.down_payment = down_payment
        self.closing_costs = closing_costs

    def income(self):
        units = int(input("\nHow many rental units are on the property? "))

        rent = int(input("\nHow much are you charging in rent per unit? "))

        otherincome = input("\nAre you receiving any additional income from the property? (ie. laundry, storage, etc.) ").lower()
        if otherincome == "no":
            self.monthly_income = units * rent
        else:
            miscincome = int(input("\nHow much additional income do you receive each month from the property? (not including the rents received) "))
            self.monthly_income = units * rent + miscincome

        print(f"\nTotal monthly income: ${self.monthly_income}")


    def expenses(self):
        self.total_expenses = 0
        mortgage = input("\nWill/do you have a mortgage on the property? ").lower()
        if mortgage == "yes":
            piti = input("\nAre your taxes and insurance escrowed into the payment?").lower()
            if piti == "yes":
                full_piti = int(input("\nWhat is the full PITI (Principle Interest Taxes and Insurance) payment? "))
                print(f"\nThe full PITI payment is ${full_piti}")
                self.down_payment = int(input("\nHow much did you put down? "))
                self.closing_costs = int(input("\nHow much were the closing costs? (appraisal, realtor fees, etc.) "))
            else:
                taxes = int(input("\nWhat are the monthly property taxes? (Annual amount divided by 12) "))
                insurance = int(input("\nWhat is the monthly home insurance payment? "))
                mortgage_payment = int(input("\nWhat is the monthly mortgage payment? (Including both principle and interest) "))
                full_piti = taxes + insurance + mortgage_payment
                print(f"\nThe full PITI payment is ${full_piti}")
        else:
            taxes = int(input("\nWhat are the monthly property taxes? (Annual amount divided by 12) "))
            insurance = int(input("\nWhat is the monthly home insurance payment? "))
            mortgage_payment = 0
            full_piti = taxes + insurance + mortgage_payment
            print(f"\nThe full PITI payment is ${full_piti}")
            self.down_payment = int(input("\nHow much did you put down? "))
            self.closing_costs = int(input("\nHow much were the closing costs? (appraisal, realtor fees, etc.) "))
        self.total_expenses += full_piti
        utilities = input("\nAre you having the tenant pay utilities? (yes/no) ").lower()
        if utilities == "yes":
            print("\nOne thing less to worry about!")
            utility_payment = 0
        else:
            utility_payment = int(input("\nWhat is the approximate estimated total utilities? (Electric/Water/Sewer/Trash) "))
        self.total_expenses += utility_payment
        hoa = input("\nDoes the property have a HOA that oversees the community? ").lower()
        if hoa == "yes":
            condo = input("\nIs the home a condo? (This can impact maintenance expenses as some will cover most things) ").lower()
            if condo == "yes":
                hoa_dues = int(input("\nHow much are the monthly dues? (Annual divided by 12 or quarterly divided by 3) "))
                capex = int(input("\nHow much are you setting aside for major repairs/renovations per month? "))
                maintenance = 0
            else:
                hoa_dues = int(input("\nHow much are the monthly dues? (Annual divided by 12 or quarterly divided by 3) "))
                maintenance = int(input("\nHow much are the monthly maintenance costs? (minor repairs and/or lawncare/snow removal) "))
                capex = int(input("\nHow much are you setting aside for major repairs/renovations per month? "))
        else:
            hoa_dues = 0
            maintenance = int(input("\nHow much are the monthly maintenance costs? (minor repairs and/or lawncare/snow removal) "))
            capex = int(input("\nHow much are you setting aside for major repairs/renovations per month? "))
        self.total_expenses += hoa_dues + capex + maintenance
        vacancy_factor  = int(input(f"\nHow much of the monthly income (${self.monthly_income}) are you putting aside for vacancy? (Please enter a percent, 0 - 100) " ))
        vacancy_saved = (vacancy_factor / 100) * self.monthly_income
        self.total_expenses += vacancy_saved
        prop_manager = input("\nAre you using a property management company? ").lower()
        if prop_manager == "yes":
            prop_manage_cost = int(input("\nHow much do they charge per month? "))
        else:
            prop_manage_cost = 0
        self.total_expenses += prop_manage_cost
        miscexpenses = int(input("\nHow much in additional misc. expenses per month? "))
        self.total_expenses += miscexpenses
        print(f"\nTotal expenses: ${self.total_expenses}")

    def cashflow(self):
        print("\nTime to look at how the income and expenses impact your monthly cash flow. ")
        self.monthly_cash_flow = self.monthly_income - self.total_expenses
        if self.monthly_cash_flow <= 0:
            print(f"\nThe expenses of ${self.total_expenses} outweigh the income of ${self.monthly_income}. ")
        else:
            print(f"\nYour monthly income of ${self.monthly_income} minus the monthly expenses of ${self.total_expenses} leaves you with ${self.monthly_cash_flow} per month in profit. ")
            print("\nLet's take a look at the total investment and see what your annual return is. ")
            invest_dp_cc = input(f"So far we have covered the down payment of ${self.down_payment} and closing costs of ${self.closing_costs}. Are these numbers correct? (yes/no) ").lower()
            if invest_dp_cc == "yes":
                pass
            else:
                change_dp_cc = int(input("\nWhich number is incorrect? (1 for down payment or 2 for closing costs) "))
                if change_dp_cc == 1:
                    self.down_payment = int(input("\nPlease enter the correct down payment "))
                else:
                    self.closing_costs = int(input("\nPlease enter the correct closing costs "))
            misc_invest = int(input("\nDo you have any additional money invested in the transaction? (rehab/revnovations etc.) Please enter the amount here. "))
            self.total_investment = self.down_payment + self.closing_costs + misc_invest
            print(f"\nThe total investment calculated is ${self.total_investment}. ")
    def roi(self):
        annual_cash_flow = self.monthly_cash_flow * 12
        print(f"\nYour annual cashflow is ${annual_cash_flow}. ")
        annual_roi = (annual_cash_flow / self.total_investment) * 100
        if annual_roi <= 6:
            print(f"\nYour annual cash on cash retrun is {annual_roi}%, which is less than the annual gain on the S&P 500 of 6%. There may be room for improvement by assessing expenses. ")
        else:
            print(f"\nYour annual cash on cash retrun is {annual_roi}%, which is more than the annual gain on the S&P 500 of 6%. This looks like a solid investment. ")

    

def calc():
    rental_home = House()

    while True:
        response = input("\nWhat would you like to enter, your income or expenses? enter 'clear' to exit (income/expenses/clear) ").lower()

        if response == "clear":
            startagain = input("\nWould you like to start over? (yes/no) ").lower()

            if startagain == 'yes':
                response = input("\nWhat would you like to enter, your income or expenses? enter 'clear' to exit (income/expenses/clear) ").lower()
            else:
                break

        elif response == "income":
            rental_home.income()

        elif response == "expenses":
            rental_home.expenses()
            break
    rental_home.cashflow()
    
    rental_home.roi()

calc()