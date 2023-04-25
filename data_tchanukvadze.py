class Bus:
    def __init__(self,num,price,capacity,pass_info=[]):
        self.num = num
        self.price = price
        self.capacity = capacity
        self.pass_info = pass_info

    def __str__(self):
        print(f"Nomeri: {self.num}, Fasi: {self.price}, Tevadoba: {self.capacity}, Mgzavrta Info: {self.pass_info}")

class Card:
    def __init__(self,id,name,balance,history=[]):
        self.id = id
        self.name = name
        self.balance = balance
        self.history = history

    def __str__(self):
        print(f"Id: {self.id}, Saxeli: {self.name}, Balansi: {self.balance}, Istoria: {self.history}")

    def buy_ticket(self,bus_obj):
        if self.balance >= bus_obj.price and self.id not in bus_obj.pass_info:
            self.balance -= bus_obj.price
            self.history.append(bus_obj.num)
            bus_obj.pass_info.append(self.id)
            print(f"Sheidzina Bileti-{bus_obj.num}")

        elif self.id in bus_obj.pass_info :
            print("Mgzavrs Ukve Aqvs Bileti")

b1 = Bus(449,2,25)
pass1 = Card(100,"Davit",5)
pass2 = Card(101,"Giorgi",1)
pass1.buy_ticket(b1)
pass2.buy_ticket(b1)
print("Name:",pass1.name,"bal:",pass1.balance,"hist:",pass1.history)
print("Name:",pass2.name,"bal:",pass2.balance,"hist:",pass2.history)
print(b1.pass_info)
#tevadobaze ar iyo pirobashi dawerili amitom if logika agar davwere imedia magashi ar damakldeba

