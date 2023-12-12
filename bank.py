from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):


    def basic_info(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self):
        pass


# Class Swiss
class Swiss(Bank):

    def __init__(self, bal):
        self.bal = 1000

    def basic_info(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    def withdraw(self, amount):
        self.amount  = amount


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basic_info())
    s.withdraw(30)
    s.withdraw(1000)


if __name__ == "__main__":
    main()
