

from banking_system import BankingServices


class FrontEndRunner:
    def __init__(self):
        pass

    def run(self):
        bank = BankingServices()

        print('\n-------------Create User----------------\n')
        bank.create_user('dre','1234','manchester')
        bank.create_user('dre','1234','manchester')

        print('\n-------------Login User----------------\n')
        user = bank.login_user('dre', '12349')
        user = bank.login_user('dre','1234')

        if user:
            print('\n-------------Savings Account ----------------\n')
            user.savingAccount.deposit(1000)
            user.savingAccount.withdraw(200)
            user.savingAccount.future_value_principal(100, 5)
            user.savingAccount.savings_interest_earned(100, 5)
            user.savingAccount.get_history()

            
            print('\n-------------Fixed Deposit Account ----------------\n')
            user.fixedAccount.deposit(2000)
            user.fixedAccount.check_interest_earn()
            user.fixedAccount.withdraw(1000)
            user.fixedAccount.check_interest_earn(3)
            user.fixedAccount.withdraw(500, 3)
            user.fixedAccount.check_interest_earn(10)
            user.fixedAccount.withdraw(1000, 10)
            user.fixedAccount.withdraw(2000.43,0)
            user.fixedAccount.check_interest_earn(0)
            user.fixedAccount.get_history()

            print('\n-------------Checking Account ----------------\n')
            user.checkingAccount.deposit(2000)
            user.checkingAccount.over_draft_limit()
            user.checkingAccount.withdraw(500)
            user.checkingAccount.withdraw(1500)
            user.checkingAccount.withdraw(100)
            user.checkingAccount.withdraw(300)
            user.checkingAccount.withdraw(50)
            user.checkingAccount.repay_overDraft(600)
            user.checkingAccount.repay_overDraft(147.77)
            user.checkingAccount.withdraw(100)
            user.checkingAccount.deposit(400)
            user.checkingAccount.withdraw(200)
            user.checkingAccount.repay_overDraft(180)
            user.checkingAccount.repay_overDraft(500)
            user.checkingAccount.withdraw(90)
            user.checkingAccount.get_history() 



     
    
   


    



        
        

        


    
