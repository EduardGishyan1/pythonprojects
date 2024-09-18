from Checking_account import *
from customer import *
from Joint_account import *
from Savings_account import *
from Transcation import *
from Transcation_manager import ConcreteTranscationManager
    
def main():
    try:
     saving_account = SavingAccounts(100,2500.0,"Hello world",10.0)
     checking_account = CheckingAccount(90,4000.0,"checking account",2000.0)
     joint_account = JointAccount(103,2500.0,"Normal",[saving_account,checking_account])

     customer = Customer("Jane","374.......",[joint_account,saving_account])

     saving_account.transfer(checking_account,100.0)
     checking_account.transfer(joint_account,100.0)
     print(joint_account.show_balance())
     print(checking_account.show_balance())
     print(saving_account.show_balance())


     customer.add_account(saving_account)
     customer.view_accounts()
     customer.view_transcation_history()
     transcation = Transcation(CheckingAccount,JointAccount,150.0,'without type',datetime.datetime.now())

     transcation.log()

     manage_transcation = ConcreteTranscationManager()
     manage_transcation.log_transcation("none",100.0)
     manage_transcation.show_transcation_history()

    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()
