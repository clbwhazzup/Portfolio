import math
import random
from random import choice
currentBet = 0
draw = ""
class Deck():    
    currentDeck = {}
    currentDeck = { 
            "AC": "Ace of Clubs",
            "2C": "Two of Clubs",
            "3C": "Three of Clubs",
            "4C": "Four of Clubs",
            "5C": "Five of Clubs",
            "6C": "Six of Clubs",
            "7C": "Seven of Clubs",
            "8C": "Eight of Clubs",
            "9C": "Nine of Clubs",
            "10C": "Ten of Clubs",
            "JC": "Jack of Clubs",
            "QC": "Queen of Clubs",
            "KC": "King of Clubs",
            "AD": "Ace of Diamonds",
            "2D": "Two of Diamonds",
            "3D": "Three of Diamonds",
            "4D": "Four of Diamonds",
            "5D": "Five of Diamonds",
            "6D": "Six of Diamonds",
            "7D": "Seven of Diamonds",
            "8D": "Eight of Diamonds",
            "9D": "Nine of Diamonds",
            "10D": "Ten of Diamonds",
            "JD": "Jack of Diamonds",
            "QD": "Queen of Diamonds",
            "KD": "King of Diamonds",
            "AH": "Ace of Hearts",
            "2H": "Two of Hearts",
            "3H": "Three of Hearts",
            "4H": "Four of Hearts",
            "5H": "Five of Hearts",
            "6H": "Six of Hearts",
            "7H": "Seven of Hearts",
            "8H": "Eight of Hearts",
            "9H": "Nine of Hearts",
            "10H": "Ten of Hearts",
            "JH": "Jack of Hearts",
            "QH": "Queen of Hearts",
            "KH": "King of Hearts",
            "AS": "Ace of Spades",
            "2S": "Two of Spades",
            "3S": "Three of Spades",
            "4S": "Four of Spades",
            "5S": "Five of Spades",
            "6S": "Six of Spades",
            "7S": "Seven of Spades",
            "8S": "Eight of Spades",
            "9S": "Nine of Spades",
            "10S": "Ten of Spades",
            "JS": "Jack of Spades",
            "QS": "Queen of Spades",
            "KS": "King of Spades"
    }
    def getDeck() :
        return Deck.currentDeck
    
    def drawCard() :
        draw = choice(list(Deck.currentDeck.keys()))
        Deck.currentDeck.pop(draw)
        return draw
class betting() :
    bet = 0.0
    money = 100.0
    def doBet(currentBet) :
        betting.bet += currentBet
        betting.money -= currentBet
    def getBet() :
        return betting.bet
    def getMoney() :
        return betting.money
    def payPush() :
        betting.money += betting.bet
        betting.bet = 0
    def payWin() :
        betting.money += betting.bet * 1.5
        betting.bet = 0
    def resetBet() :
        betting.bet = 0
		
class dealersHand() :
    hand = []
    handValue = 0
    def resetDealersHand() :
        dealersHand.hand = []
        dealersHand.handValue = 0
    def getHand(index) :
        return dealersHand.hand[index]
    def getHandValue() :
        return dealersHand.handValue
    def addCard(draw) :
        dealersHand.hand.append(draw)
        if draw == "AC" or draw == "AH" or draw == "AS" or draw == "AD" :
            dealersHand.handValue += 11
            if dealersHand.handValue > 21 :
                dealersHand.handValue -= 10
            else :
                pass
        elif draw == "2C" or draw == "2H" or draw == "2S" or draw == "2D" :
            dealersHand.handValue += 2
        elif draw == "3C" or draw == "3H" or draw == "3S" or draw == "3D" :
            dealersHand.handValue += 3
        elif draw == "4C" or draw == "4H" or draw == "4S" or draw == "4D" :
            dealersHand.handValue += 4
        elif draw == "5C" or draw == "5H" or draw == "5S" or draw == "5D" :
            dealersHand.handValue += 5
        elif draw == "6C" or draw == "6H" or draw == "6S" or draw == "6D" :
            dealersHand.handValue += 6
        elif draw == "7C" or draw == "7H" or draw == "7S" or draw == "7D" :
            dealersHand.handValue += 7
        elif draw == "8C" or draw == "8H" or draw == "8S" or draw == "8D" :
            dealersHand.handValue += 8
        elif draw == "9C" or draw == "9H" or draw == "9S" or draw == "9D" :
            dealersHand.handValue += 9
        elif draw == "10C" or draw == "10H" or draw == "10S" or draw == "10D" :
            dealersHand.handValue += 10
        elif draw == "JC" or draw == "JH" or draw == "JS" or draw == "JD" :
            dealersHand.handValue += 10
        elif draw == "QC" or draw == "QH" or draw == "QS" or draw == "QD" :
            dealersHand.handValue += 10
        elif draw == "KC" or draw == "KH" or draw == "KS" or draw == "KD" :
            dealersHand.handValue += 10
        else :
            pass
class playersHand() :
    hand = []
    handValue = 0
    def resetPlayersHand() :
        playersHand.hand = []
        playersHand.handValue = 0
    def getHand():
        return playersHand.hand
    def getHandValue() :
        return playersHand.handValue
    def addCard(draw) :
        playersHand.hand.append(draw)
        if draw == "AC" or draw == "AH" or draw == "AS" or draw == "AD" :
            playersHand.handValue += 11
            if playersHand.handValue > 21 :
                playersHand.handValue -= 10
            else :
                pass
        elif draw == "2C" or draw == "2H" or draw == "2S" or draw == "2D" :
            playersHand.handValue += 2
        elif draw == "3C" or draw == "3H" or draw == "3S" or draw == "3D" :
            playersHand.handValue += 3
        elif draw == "4C" or draw == "4H" or draw == "4S" or draw == "4D" :
            playersHand.handValue += 4
        elif draw == "5C" or draw == "5H" or draw == "5S" or draw == "5D" :
            playersHand.handValue += 5
        elif draw == "6C" or draw == "6H" or draw == "6S" or draw == "6D" :
            playersHand.handValue += 6
        elif draw == "7C" or draw == "7H" or draw == "7S" or draw == "7D" :
            playersHand.handValue += 7
        elif draw == "8C" or draw == "8H" or draw == "8S" or draw == "8D" :
            playersHand.handValue += 8
        elif draw == "9C" or draw == "9H" or draw == "9S" or draw == "9D" :
            playersHand.handValue += 9
        elif draw == "10C" or draw == "10H" or draw == "10S" or draw == "10D" :
            playersHand.handValue += 10
        elif draw == "JC" or draw == "JH" or draw == "JS" or draw == "JD" :
            playersHand.handValue += 10
        elif draw == "QC" or draw == "QH" or draw == "QS" or draw == "QD" :
            playersHand.handValue += 10
        elif draw == "KC" or draw == "KH" or draw == "KS" or draw == "KD" :
            playersHand.handValue += 10
        else :
            pass

class Program() :
    #Test Program
    
    #currentDeck = Deck.getDeck()
    #print("Hello World!")
    #print(currentDeck)
    #draw = Deck.drawCard()
    #print(Deck.currentDeck[draw])
    #Deck.currentDeck.pop(draw)
    #print(currentDeck)
    
    #Blackjack Program
    print("             Welcome to Blackjack"
          "              ------------------"
          "   Get as close to 21 as you can without going over!"
          "   You can either stand or hit on your turn. If you"
          "   hit, you will be dealt another card. If you stand"
          " that will be the end of your one turn. The Dealer will"
          "   hit until they reach 17 or higher. If you and the"
          "    dealer both stand, whoever has the highest total"
          "            at 21 and under will win"
          "Number cards are worth their face value, face cards"
          "are worth 10, and an Ace can be worth either 1 or 11."
          )
    play = "y"
    hit = True
    busted = False
    while play == "y" :
        currentDeck = Deck.getDeck()
        input("Press ENTER to start")
        playersHand.resetPlayersHand()
        dealersHand.resetDealersHand()
        hit = True
        busted = False

        while True :
            print("How much would you like to bet? You currently have", betting.getMoney(), "\n")
            currentBet = float(input())
            if currentBet > betting.getMoney() :
                print("You don't have enough money")
                continue
            elif currentBet < 0 :
                print("You can't bet a negative number")
                continue
            else :
                break
        
        betting.doBet(currentBet)
        draw = Deck.drawCard()
        dealersHand.addCard(draw)
        draw = Deck.drawCard()
        dealersHand.addCard(draw)
        print("The dealer has a", dealersHand.getHand(1), " and an unknow card")
        
        draw = Deck.drawCard()
        playersHand.addCard(draw)
        draw = Deck.drawCard()
        playersHand.addCard(draw)
        print("You have", playersHand.getHandValue(), ", with ", playersHand.getHand())
        
        while hit == True :
            if playersHand.getHandValue() > 21 :
                print("You went over 21 and busted!")
                hit = False
                busted = True
                betting.resetBet()
                print("You now have $", betting.getMoney())
                input("Would you like to play again? y/n")
            elif playersHand.getHandValue() == 21 :
                print("Blackjack! Let's see what the dealer has.")
                hit = False
            else :
                print("You have", playersHand.getHandValue(), ", with ", playersHand.getHand(), ". Type 'h' to hit, or 's' to stand\n")
                hitOrStand = input()
                if hitOrStand == "h" :
                    draw = Deck.drawCard()
                    playersHand.addCard(draw)
                    print(playersHand.getHand(), " worth ", playersHand.getHandValue())
                    if playersHand.getHandValue() > 21 :
                        print("You went over 21 and busted!")
                        hit = False
                        busted = True
                        betting.resetBet()
                        print("You now have $", betting.getMoney())
                        play = input("Would you like to play again? y/n")
                    elif playersHand.getHandValue() == 21 :
                        print("Blackjack! Let's see what the dealer has.")
                        hit = False
                elif hitOrStand == "s" :
                    print("Dealer's turn")
                    hit = False
                else :
                    print("Invalid input")
                    hit = True
        if busted == False :
            print("The dealer's hand is currently worth ", dealersHand.getHandValue())
            if dealersHand.getHandValue() >=17 and dealersHand.getHandValue() <= 21 :
                if playersHand.getHandValue() == dealersHand.getHandValue() :
                    print("The dealer and you tie. It's a push, so you win your money back: ", betting.getBet())
                    betting.payPush()
                    print("You now have ", betting.getMoney())
                elif playersHand.getHandValue() > dealersHand.getHandValue() :
                    print("You win, so you get your money back plus half, ", betting.getBet() * 1.5)
                    betting.payWin()
                    print("You now have ", betting.getMoney())
                elif playersHand.getHandValue() < dealersHand.getHandValue() :
                    print("The dealer wins.")
                    betting.resetBet()
                    print("You now have ", betting.getMoney())
            elif dealersHand.getHandValue() < 21 :
                while dealersHand.getHandValue() < 17 :
                    draw = Deck.drawCard()
                    dealersHand.addCard(draw)
                    print("The dealer got ", draw, " and they now have ", dealersHand.getHandValue())
                    if dealersHand.getHandValue() > 21 :
                        print("Dealer went over 21 and busted! You win, so you get your money back plus half, ", betting.getBet() * 1.5)
                        betting.payWin()
                        print("You now have ", betting.getMoney())
                    elif dealersHand.getHandValue() == 21 :
                        print("The dealer has blackjack!")
                        if playersHand.getHandValue() == 21 :
                            print("A push. You and the dealer tie, so you get your money back: ", betting.getBet())
                            betting.payPush()
                            print("You now have ", betting.getMoney())
                        else :
                            print("The dealer wins.")
                            betting.resetBet()
                            print("You now have ", betting.getMoney())
                    elif dealersHand.getHandValue() >= 17 and dealersHand.getHandValue() <= 21 :
                        if playersHand.getHandValue() == dealersHand.getHandValue() :
                            print("You and the dealer tie. It's a push, so you win your money back: ", betting.getBet())
                            betting.payPush()
                            print("You now have ", betting.getMoney())
                        elif playersHand.getHandValue() > dealersHand.getHandValue() :
                            print("You win, so you get your money back plus half, ", betting.getBet() * 1.5)
                            betting.payWin()
                            print("You now have ", betting.getMoney())
                        elif playersHand.getHandValue() < dealersHand.getHandValue() :
                            print("The dealer wins.")
                            betting.resetBet()
                            print("You now have ", betting.getMoney())
                    else :
                        pass
            elif dealersHand.getHandValue() == 21 :
                print("The dealer has blackjack!")
                if playersHand.getHandValue() == 21 :
                    print("A push. You and the dealer tie, so you get your money back: ", betting.getBet())
                    betting.payPush()
                    print("You now have ", betting.getMoney())
                else :
                    print("The dealer wins!")
                    betting.resetBet()
                    print("You now have ", betting.getMoney())
            play = input("Would you like to play again? (y/n)")
        else :
            pass