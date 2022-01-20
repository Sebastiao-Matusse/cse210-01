import random 
score = 0
rolling_dice = None
prompt = "Roll dice?"
atempts = []

def main(): 
    numbers = [1,2,3,4,5]
    data = random.sample(numbers, k=len(numbers))
    atempts.append(data)
    print(atempts)

    for i in data:
        print(i, end=" ")

def compute_score(score, rolling_dice):
    if rolling_dice == 5:
        score += 50
        print(f"Your score is {score}")
    elif rolling_dice == 10:
        score += 100
        print(f"Your socre is {score}")

    pass

while prompt.lower() == "y":
    if rolling_dice == 5:
        score += 50
        print(f"Your score is {score}")
    elif rolling_dice == 10:
        score += 100
        print(f"Your socre is {score}")

    pass


main()