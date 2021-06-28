import random

def gamblingGame(numBets):
    possibleResults = ["win", "lose"]
    token = 50
    betsMade = 0
    totalWins =0
    totalLoses = 0
    betResult_STR = " "
    if numBets <= 300:
        for i in range(numBets):
            betResult = random.choices(possibleResults, [0.4, 0.6])
            betResult_STR = betResult_STR.join(betResult)
            if token > 0:
                if betResult_STR == "win":
                    token += 1
                    totalWins += 1
                else:
                    token -= 1
                    totalLoses +=1

                betsMade += 1
                print(f"{betResult_STR}\n")
            else:
                print("run out of tokens")
                break

        print(f"\nYou made {betsMade} bets\n")
        print(f"wins: {totalWins}")
        print(f"loses: {totalLoses}\n")

        if token > 0:
            print(f"You have {token} token's left")

if __name__ == "__main__":

    gamblingGame(20)
