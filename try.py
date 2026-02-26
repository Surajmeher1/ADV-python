def transation( ballance, amount, type):
    if type == "deposit":
        ballance += amount
        return ballance
    elif type == "withdraw":
        if amount <= ballance:
            ballance -= amount
            return ballance
        else:
            print("Insufficient funds.")
            return ballance
    else:
        print("Invalid transaction type.")
        return ballance
ballance = 1000     
ballance = transation(ballance, 200, "deposit")
print("Current ballance:", ballance)
ballance = transation(ballance, 150, "withdraw")
print("Current ballance:", ballance)
ballance = transation(ballance, 1200, "withdraw")
print("Current ballance:", ballance)
ballance = transation(ballance, 300, "deposit")
print("Current ballance:", ballance)
