import random, os 
Chips = None
plays = 0
bankfile = open('bank.txt','r')
readbank = bankfile.read()
bank = float(readbank)
print(bank)
def ChipsStart():
    global Chips, currentbet
    try:
        Chips = int(input('How much chips do you want to start off with? '))
        if Chips < 0:
            Chips = None
            print('Chips Must Not Be Negtive!')
            return
    except:
        print('Please type an positve integer!')
        return
while Chips == None:
    ChipsStart()
coinflip = None
coinresult = None
currentbet = None
def banksystem():
    global bank
    file = open('bank.txt', 'w')
    file.write(str(bank))
def bettingsystem():
    global Chips, currentbet
    while True:
        try:
            currentbet = round(float(input('How much do you want to bet? ')),3)
        except ValueError:
            print('Something went wrong with the bet please try again!')
            continue
        if 0 < currentbet <= Chips:
            Chips -= currentbet
            print(f'Your bet of {currentbet} went through, your chips is now: {Chips}')
            break
        else:
            print('Invalid Bet, Your bet must be above zero and below or equal to your chips!')
def mainloop():
    global bank
    banksystem()
    print(f'Current Bank Balance: {bank}')
    print('1. Limbo')
    print('2. Coin Flip')
    print('3. Card Guessing')
    print('4. Dice')
    print('5. Slots (NO BACKING OUT!)')
    try:
        gamechoice = int(input('Which Game would you like to play: '))
    except :
        print('Something went wrong with what you input for your game choice please try again with a number!')
        return
    if gamechoice == 1:
        gamelimbo()
    elif gamechoice == 2:
        gamecoinflip()
    elif gamechoice == 3:
        gamecardguessing()
    elif gamechoice == 4:
        gamedice()
    elif gamechoice == 5:
        gameslot()

def gamelimbo():
    global Chips, currentbet, bank
    bettingsystem()
    multiplier = float(input('What multiper for limbo do you want? (this number will be checked with a random multiper!) '))
    instantcrashchance = random.randint(1,100)
    if instantcrashchance <= 33:
        randommultiper = round(0 + random.uniform(0.01,0.5),3)
    else:
        randomtest = random.expovariate(0.7)
        if randomtest < 1:
            randomtest += 1
        else:
            pass
        randommultiper = round(randomtest,3)        
    if randommultiper > multiplier:
        winnings = currentbet * multiplier
        Chips += round(winnings,3)
        print(f'You won! Your multiper was {multiplier}, and the random was {randommultiper}! You gained {winnings} and now have {Chips}!')
    else:
        print(f'You lost. You now have {Chips}')
        bank += currentbet

def gamecoinflip():
    global Chips, coinflip, coinresult, currentbet, bank
    bettingsystem()
    try:
        inputheadsortails = input('Do you want heads or tails? ')
    except:
        print('Something went wrong try again with')
        return
    coinfliping()
    if inputheadsortails.lower() == coinresult.lower():
        print('YOU WON!!!')
        againinput = input('Do you want to go again for a chance at more Chips?(y/n) ')
        if againinput == 'y' or againinput == 'yes':
            headsortailsinput = input('Do you want heads or tails? ')
            coinfliping()
            if headsortailsinput == coinresult:
                winnings = currentbet * 4.5
                Chips += round(winnings,3)
                print(f'You won twice! and got 4.5x your bet! winnings: {round(winnings,3)} for a balance of {Chips}')
            else:
                print(f'Sorry, You lost. Your balance is {Chips}')
                bank += currentbet
        else:
            winnings = currentbet * 2
            Chips += round(winnings,3)
            print(f'You won one time! and got 2x your bet and now have {Chips}')
    else:
        print(f'Sorry, You lost. New balance is {Chips}')
        bank += currentbet

def coinfliping():
    global coinflip, coinresult
    coinflip = random.randint(1,2)
    if coinflip == 1:
        coinresult = 'heads'
    else:
        coinresult = 'tails'

def gamecardguessing():
    global Chips,currentbet,bank
    bettingsystem()
    randomcard = random.choices(['Ace','2','3','4','5','6','7','8','9','10','Jack','King','Queen','Joker'],k=1)[0]
    usercard = input('What Card Do you want(Cards: Ace,2,3,4,5,6,7,8,9,10,Jack,King,Queen,Joker) ')
    if usercard.lower() == randomcard.lower():
        winnings = currentbet * 13
        Chips += round(winnings,3)
        print(f'YOU WON!!!, THE CARD WAS {randomcard}, and you had {usercard}')
    else:
        print(f'Sorry, you lost. The card was {randomcard}, while you had {usercard}! You now have {Chips}')
        bank += currentbet

def gamedice():
    global Chips, currentbet,bank
    bettingsystem()
    try:
        target = float(input('What number would you like your target to be? If the dice roll is OVER this number you win!(must between 1 and 100) '))
        multiper = round((99/(100-target)),10)
        print(f'Given Your Target, your multiper was {multiper}')
    except ValueError:
        print('An error has occured.')
        return
    if 1 < target <= 100:
        dicenumber = random.randint(1,100)
        if dicenumber >= target:
            print(F'You Win! The Random Roll was {dicenumber}')
            winnings = currentbet * multiper
            Chips += round(winnings,3)
            print(f'Your winnings: {round(winnings,3)}')
            print(f'You won and now have: {Chips}')
        else:
            print(f'You lost! The Random Roll was {dicenumber}, and you have {Chips}')
            bank += currentbet
    else:
        print('Your target must be below hundred and greater than one and not zero!')
        Chips += currentbet
        print(f'Your bet: {currentbet} has been returned, your new Chips balance is {Chips}')
        print('')

def gameslot():
    global Chips, currentbet, plays,bank
    print(f'With a current of Plays:{plays}, the current jackpot is {500+5*plays}.')
    currentbet = 30 + plays * 0.5 
    Chips -= currentbet
    slotnumber = random.randint(1,65536)
    if slotnumber <= 3000 + plays * 30:
        winnings = 500 + 5 * plays
        Chips += winnings
        print(f'You won! Jackpot:{winnings}, Current Chips:{Chips}')
        plays = 0 
    else:
        print('You lost')
        bank += currentbet
    plays += 1
while Chips > 0:
    mainloop()