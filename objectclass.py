
class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
    

    def deposit(self, amount, description=""):
        """
        A deposit should accept an amount and description. If 
        no description is give, it should default to an empty string.
        """

        self.ledger.append({"amount": amount , "description": description})
    

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method, but the amount
        paid in should be stored in the ledger as a negative number
        """

        if(self.check_funds(amount)):
            self.ledger.append({"amount": amount , "description": description})
            return True
        return False


    def get_balance(self):
        """
        A get_balance method that returns the current balance of the budget category
        based on deposits and withdrawals.
        """
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        
        return total_cash

    
    def transfer(self, amount, category):
        """
        This method should return True if transfer took place, and False otherwise.
        """
        if (self.check_funds(amount)):
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        return False



