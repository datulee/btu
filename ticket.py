class Ticket:
    def __init__(self, name, price, number, lang="Geo"):
        self.name = name
        self.price = price
        self.number = number
        self.lang = lang


    def __str__(self):
        return f'ფილმის დასახელება: {self.name}, ფასი - {self.price}, რაოდენობა - {self.number}, ენა - {self.lang} '

    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.number > other.number
        else:
            return self.number > other


class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def __str__(self):
        return f'User -  {self.username}, ბალანსი - {self.balance} ლარი'

    def buy(self, ticket_obj, number):
        if ticket_obj.price*number<=self.balance and ticket_obj.number>=number:
            self.balance -=  ticket_obj.price*number
            ticket_obj.number -= number
            print(f"თქვენ წარმატებით იყიდეთ ბილეთი {ticket_obj.name}")
        elif ticket_obj.price*number>self.balance:
            print("თქვენ ბილეთს ვერ იყიდით. არ არის საკმარისი თანხა")
        else:
            print("თქვენ ბილეთს ვერ იყიდით. არ არის საკმარისი ადგილი")


    def deposit(self, amount):
        self.balance += amount
        print(f"თქვენ ანგარიშზე გაქვთ {self.balance} ლარი")


t1 = Ticket('ბეჭდების მბრძანებელი', 15, 10, 'Eng')
t2 = Ticket('Batman', 30, 15)
u1 = User('ალექსანდრე', 50)
print(t1)
print(u1)
u1.buy(t1, 5)
print(t1)
print(u1)
u1.deposit(100)
print(t1 > t2)
print(t1 > 10)
