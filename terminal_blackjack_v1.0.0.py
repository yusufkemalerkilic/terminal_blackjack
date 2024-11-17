# EN:

# Name: terminal_blackjack

# Version: v1.0.0

# Author: Yusuf Kemal Erkılıç

# Date: 17.11.2024 (dd.mm.yyyy)

# Purpose:
# This Python script allows playing Blackjack on the terminal.
# At the beginning of the game, the player is given a virtual budget of $100. The player can place bets from this budget.
# The money in this game is virtual and not real.

# Description:
# A deck of 52 cards is defined.
# The budget is defined as $100.
# Word animations and budget animations are created.
# The player encounters 3 options in the main menu: PLAY, HELP, EXIT.
# If the player chooses PLAY, the player is directed to the bet screen.
# The player places a bet and the cards are dealt.
# The player and the dealer receive two cards each.
# The values of the cards are determined by the numbers and symbols on the cards.
# Cards with a number on them have that number value.
# Jack (J), Queen (Q), and King (K) cards have a value of 10.
# The Ace (A) card has a value of 1 or 11 depending on the player's hand.
# The card values are calculated and the player is offered the options to draw a card (HIT) or stand (STAND).
# The player is offered the options to draw a card and stand.
# If the player chooses to draw a card, a card is drawn and added to the player's hand.
# If the player chooses to stand, the card drawing process ends and the turn passes to the dealer.
# The dealer draws cards until reaching a hand value of 17 or higher.
# After the player and the dealer draw cards, the values of the hands are compared.
# The player and the dealer try to have a hand value closest to 21.
# If the player and the dealer exceed 21, the hand is lost.
# If the player has a hand value closest to 21, the hand is won.
# If the player has a hand value closest to 21 and uses only 2 cards to reach 21, the player has Blackjack.
# Blackjack pays 1.5 times the bet amount to the player.
# If the player and the dealer have 21 at the same time, the player who has Blackjack wins.
# If no one has Blackjack and the player and the dealer have the same hand value, the hand is tied and the player's bet is refunded.
# If both sides have Blackjack, the hand is tied and the player's bet is refunded.
# The player ends the game and returns to the main menu.
# If the player chooses HELP, the player receives information about the game.
# If the player chooses EXIT, the game ends.



# TR:

# İsim: terminal_blackjack

# Sürüm: v1.0.0

# Yazar: Yusuf Kemal Erkılıç

# Tarih: 17.11.2024 (gg.aa.yyyy)

# Amaç:
# Bu Python betiği, terminal üzerinden Blackjack oynanmasını sağlar.
# Oyun başında oyuncuya 100$ sanal bütçe verilir. Oyuncu, bu bütçe üzerinden bahis yatırabilir.
# Bu oyundaki paralar sanaldır ve gerçek değildir.

# Açıklama:
# 52 kartlık bir deste tanımlanır.
# Bütçe 100$ olarak tanımlanır.
# Kelime animasyonları ve bütçe animasyonları oluşturulur.
# Oyuncu ana menüde 3 seçenekle karşılaşır: OYNA (PLAY), YARDIM (HELP) ÇIKIŞ (EXIT).
# Oyuncu, OYNA seçeneğini seçerse, bahis yapma ekranına yönlendirilir.
# Oyuncu, bahis yapar ve kartlar dağıtılır.
# Oyuncu ve dağıtıcı (dealer) ikişer kart alır.
# Kart değerleri kartın üzerindeki sayı ve sembollerle belirlenir.
# Üzerinde bir sayı olan kartlar, o sayı değerine sahiptir.
# Vale (J), Kız (Q) ve Papaz (K) kartları 10 değerine sahiptir.
# As (A) kartı, oyuncunun eline göre 1 veya 11 değerine sahiptir.
# Kart değerleri hesaplanır ve oyuncuya kart çekme (HIT) ve pas (STAND) seçenekleri sunulur.
# Oyuncuya, kart çekme ve pas verme seçenekleri sunulur.
# Oyuncu, kart çekme seçeneğini seçerse, bir kart çeker ve kart eline eklenir.
# Oyuncu, pas verme seçeneğini seçerse, kart çekme işlemi sona erer ve sıra dağıtıcıya (dealer) geçer.
# Dağıtıcı, 17 veya daha yüksek bir el değerine ulaşana kadar kart çeker.
# Oyuncu ve dağıtıcı, kart çekme işlemi sona erdikten sonra ellerin değerleri karşılaştırılır.
# Oyuncu ve dağıtıcı, 21'e en yakın el değerine sahip olmaya çalışır.
# Oyuncu ve dağıtıcı, 21'i aşarsa, eli kaybeder.
# Oyuncu, 21'e en yakın el değerine sahipse, eli kazanır.
# Oyuncu, 21'e en yakın el değerine sahipse ve 21'e ulaşmak için sadece 2 kart kullanmışsa, Blackjack yapmış olur.
# Blackjack, oyuncuya bahis miktarının 1.5 katı ödeme yapar.
# Oyuncu ve dağıtıcı, aynı anda 21 el değerine sahip olursa, Blackjack yapmış olan kazanır.
# Eğer Blackjack yapan yoksa ve oyuncu ile dağıtıcı, aynı el değerine sahipse, el berabere biter ve oyuncunun bahsi geri ödenir.
# Eğer iki tarafta Blackjack yaparsa, el berabere biter ve oyuncunun bahsi geri ödenir.
# Oyuncu, oyunu bitirir ve ana menüye döner.
# Oyuncu, YARDIM seçeneğini seçerse, oyun hakkında bilgi alır.
# Oyuncu, ÇIKIŞ seçeneğini seçerse, oyunu sonlandırır.



import random   # EN: Required libraries are imported.
import os       # TR: Gerekli kütüphanelerin içe aktarılır.
import random   
import time

budget=100  # EN: The budget is defined as $100.
            # TR: Bütçe $100 olarak tanımlanır.

deck=[  "[♠ A ♠]","[♥ A ♥]","[♦ A ♦]","[♣ A ♣]",   # EN: A deck of 52 cards is defined.
        "[♠ 2 ♠]","[♥ 2 ♥]","[♦ 2 ♦]","[♣ 2 ♣]",   # TR: 52 kartlık bir deste tanımlanır.
        "[♠ 3 ♠]","[♥ 3 ♥]","[♦ 3 ♦]","[♣ 3 ♣]",
        "[♠ 4 ♠]","[♥ 4 ♥]","[♦ 4 ♦]","[♣ 4 ♣]",
        "[♠ 5 ♠]","[♥ 5 ♥]","[♦ 5 ♦]","[♣ 5 ♣]",
        "[♠ 6 ♠]","[♥ 6 ♥]","[♦ 6 ♦]","[♣ 6 ♣]",
        "[♠ 7 ♠]","[♥ 7 ♥]","[♦ 7 ♦]","[♣ 7 ♣]",
        "[♠ 8 ♠]","[♥ 8 ♥]","[♦ 8 ♦]","[♣ 8 ♣]",
        "[♠ 9 ♠]","[♥ 9 ♥]","[♦ 9 ♦]","[♣ 9 ♣]",
        "[♠ 10 ♠]","[♥ 10 ♥]","[♦ 10 ♦]","[♣ 10 ♣]",
        "[♠ J ♠]","[♥ J ♥]","[♦ J ♦]","[♣ J ♣]",
        "[♠ Q ♠]","[♥ Q ♥]","[♦ Q ♦]","[♣ Q ♣]",
        "[♠ K ♠]","[♥ K ♥]","[♦ K ♦]","[♣ K ♣]"
        ]

def wordAnimation(word,interval,endOfText): # EN: The function for word animations is defined.
                                            # TR: Kelime animasyonları için fonksiyon tanımlanır.

    for letter in word:
        print(letter,end="",flush=True)
        time.sleep(interval)
    print(str(endOfText),end="")

def budgetAnimation():              # EN: The function for budget animations is defined.
                                    # TR: Bütçe animasyonları için fonksiyon tanımlanır.

    for i in range(int(budget)):

        if len(range(int(budget)))-i<3:
            print("Budget: $"+str(i),end="",flush=True)
            time.sleep(0.3)

        elif len(range(int(budget)))-i<10:
            print("Budget: $"+str(i),end="",flush=True)
            time.sleep(0.1)

        else:
            print("Budget: $"+str(i),end="",flush=True)

        os.system("cls")

    print("Budget: $"+str(budget),flush=True)

def handValue(person,ace):  # EN: The function for calculating the hand value is defined.
                            # TR: El değerini hesaplamak için fonksiyon tanımlanır.

    hand=0                  
    if "[♠ A ♠]" in person:

        if person==dealer and dealer[0]=="[♠ A ♠]":
            hand+=11

        else:
            hand+=1

    if "[♥ A ♥]" in person:

        if person==dealer and dealer[0]=="[♥ A ♥]":
            hand+=11

        else:
            hand+=1

    if "[♦ A ♦]" in person:

        if person==dealer and dealer[0]=="[♦ A ♦]":
            hand+=11

        else:
            hand+=1

    if "[♣ A ♣]" in person:

        if person==dealer and dealer[0]=="[♣ A ♣]":
            hand+=11

        else:
            hand+=1

    if "[♠ 2 ♠]" in person:
        hand+=2

    if "[♥ 2 ♥]" in person:
        hand+=2

    if "[♦ 2 ♦]" in person:
        hand+=2

    if "[♣ 2 ♣]" in person:
        hand+=2

    if "[♠ 3 ♠]" in person:
        hand+=3

    if "[♥ 3 ♥]" in person:
        hand+=3

    if "[♦ 3 ♦]" in person:
        hand+=3

    if "[♣ 3 ♣]" in person:
        hand+=3

    if "[♠ 4 ♠]" in person:
        hand+=4

    if "[♥ 4 ♥]" in person:
        hand+=4

    if "[♦ 4 ♦]" in person:
        hand+=4

    if "[♣ 4 ♣]" in person:
        hand+=4

    if "[♠ 5 ♠]" in person:
        hand+=5

    if "[♥ 5 ♥]" in person:
        hand+=5

    if "[♦ 5 ♦]" in person:
        hand+=5

    if "[♣ 5 ♣]" in person:
        hand+=5

    if "[♠ 6 ♠]" in person:
        hand+=6

    if "[♥ 6 ♥]" in person:
        hand+=6

    if "[♦ 6 ♦]" in person:
        hand+=6

    if "[♣ 6 ♣]" in person:
        hand+=6

    if "[♠ 7 ♠]" in person:
        hand+=7

    if "[♥ 7 ♥]" in person:
        hand+=7

    if "[♦ 7 ♦]" in person:
        hand+=7

    if "[♣ 7 ♣]" in person:
        hand+=7

    if "[♠ 8 ♠]" in person:
        hand+=8

    if "[♥ 8 ♥]" in person:
        hand+=8

    if "[♦ 8 ♦]" in person:
        hand+=8

    if "[♣ 8 ♣]" in person:
        hand+=8

    if "[♠ 9 ♠]" in person:
        hand+=9

    if "[♥ 9 ♥]" in person:
        hand+=9

    if "[♦ 9 ♦]" in person:
        hand+=9

    if "[♣ 9 ♣]" in person:
        hand+=9

    if "[♠ 10 ♠]" in person:
        hand+=10

    if "[♥ 10 ♥]" in person:
        hand+=10

    if "[♦ 10 ♦]" in person:
        hand+=10

    if "[♣ 10 ♣]" in person:
        hand+=10

    if "[♠ J ♠]" in person:
        hand+=10

    if "[♥ J ♥]" in person:
        hand+=10

    if "[♦ J ♦]" in person:
        hand+=10

    if "[♣ J ♣]" in person:
        hand+=10

    if "[♠ Q ♠]" in person:
        hand+=10

    if "[♥ Q ♥]" in person:
        hand+=10

    if "[♦ Q ♦]" in person:
        hand+=10

    if "[♣ Q ♣]" in person:
        hand+=10

    if "[♠ K ♠]" in person:
        hand+=10

    if "[♥ K ♥]" in person:
        hand+=10

    if "[♦ K ♦]" in person:
        hand+=10

    if "[♣ K ♣]" in person:
        hand+=10

    while person==dealer and ace>0 and hand>21:
        hand-=10
        ace-=1

    if person==player and ace>0 and hand<=11:
        hand+=10

    return hand

def playerShowHand():   # EN: The function for showing the player's hand is defined.
                        # TR: Oyuncunun elini göstermek için fonksiyon tanımlanır.

    hand=""
    for i in range(len(player)):
        hand+=player[i]+" "
    return hand

def holeCard():    # EN: The function for determining the value of the dealer's hole card is defined.
                   # TR: Dağıtıcının kapalı kartının değerini belirlemek için fonksiyon tanımlanır.

    holeCardValue=0

    if dealer[0]=="[♠ A ♠]" or dealer[0]=="[♥ A ♥]" or dealer[0]=="[♦ A ♦]" or dealer[0]=="[♣ A ♣]":    
        holeCardValue=11

    elif dealer[0]=="[♠ 2 ♠]" or dealer[0]=="[♥ 2 ♥]" or dealer[0]=="[♦ 2 ♦]" or dealer[0]=="[♣ 2 ♣]":
        holeCardValue=2

    elif dealer[0]=="[♠ 3 ♠]" or dealer[0]=="[♥ 3 ♥]" or dealer[0]=="[♦ 3 ♦]" or dealer[0]=="[♣ 3 ♣]":
        holeCardValue=3

    elif dealer[0]=="[♠ 4 ♠]" or dealer[0]=="[♥ 4 ♥]" or dealer[0]=="[♦ 4 ♦]" or dealer[0]=="[♣ 4 ♣]":
        holeCardValue=4

    elif dealer[0]=="[♠ 5 ♠]" or dealer[0]=="[♥ 5 ♥]" or dealer[0]=="[♦ 5 ♦]" or dealer[0]=="[♣ 5 ♣]":
        holeCardValue=5

    elif dealer[0]=="[♠ 6 ♠]" or dealer[0]=="[♥ 6 ♥]" or dealer[0]=="[♦ 6 ♦]" or dealer[0]=="[♣ 6 ♣]":
        holeCardValue=6

    elif dealer[0]=="[♠ 7 ♠]" or dealer[0]=="[♥ 7 ♥]" or dealer[0]=="[♦ 7 ♦]" or dealer[0]=="[♣ 7 ♣]":
        holeCardValue=7

    elif dealer[0]=="[♠ 8 ♠]" or dealer[0]=="[♥ 8 ♥]" or dealer[0]=="[♦ 8 ♦]" or dealer[0]=="[♣ 8 ♣]":
        holeCardValue=8

    elif dealer[0]=="[♠ 9 ♠]" or dealer[0]=="[♥ 9 ♥]" or dealer[0]=="[♦ 9 ♦]" or dealer[0]=="[♣ 9 ♣]":
        holeCardValue=9

    elif dealer[0]=="[♠ 10 ♠]" or dealer[0]=="[♥ 10 ♥]" or dealer[0]=="[♦ 10 ♦]" or dealer[0]=="[♣ 10 ♣]":
        holeCardValue=10

    elif dealer[0]=="[♠ J ♠]" or dealer[0]=="[♥ J ♥]" or dealer[0]=="[♦ J ♦]" or dealer[0]=="[♣ J ♣]":
        holeCardValue=10

    elif dealer[0]=="[♠ Q ♠]" or dealer[0]=="[♥ Q ♥]" or dealer[0]=="[♦ Q ♦]" or dealer[0]=="[♣ Q ♣]":
        holeCardValue=10

    elif dealer[0]=="[♠ K ♠]" or dealer[0]=="[♥ K ♥]" or dealer[0]=="[♦ K ♦]" or dealer[0]=="[♣ K ♣]":
        holeCardValue=10

    return holeCardValue

def dealerShowHand():   # EN: The function for showing the dealer's hand except the hole card is defined.
                        # TR: Dağıtıcının kapalı kart hariç elini göstermek için fonksiyon tanımlanır.

    hand=""

    for i in range(len(dealer)):

        if i==0:
            hand+="[  ?  ] "

        else:
            hand+=dealer[i]+" "

    return hand

def dealerShowHandOpen():   # EN: The function for showing the dealer's hand including the hole card is defined.
    hand=""                 # TR: Dağıtıcının elini kapalı kart ile birlikte göstermesi için fonksiyon tanımlanır.

    for i in range(len(dealer)):
        hand+=dealer[i]+" "

    return hand

def result():   # EN: The function for determining the result of the game is defined.
                # TR: Oyunun sonucunu belirlemek için fonksiyon tanımlanır.

            if handValue(player,aceCount(player))==21 and handValue(dealer,aceCount(dealer))!=21:

                if len(player)==2:
                    globals()['budget']+=bet*1.5
                    return f'''Blackjack! You win!
You won ${bet*1.5}'''

                else:
                    globals()['budget']+=bet
                    return f'''You win!
You won ${bet}'''

            elif handValue(player,aceCount(player))==21 and handValue(dealer,aceCount(dealer))==21:

                if len(player)==2 and len(dealer)==2:
                    return "Both have Blackjack! It's a tie!"

                elif len(player)==2 and len(dealer)>2:
                    globals()['budget']+=bet*1.5
                    return f'''Blackjack! You win!
You won ${bet*1.5}'''

                elif len(player)>2 and len(dealer)==2:
                    globals()['budget']-=bet
                    return f'''Dealer has Blackjack! You lose!
You lost ${bet}'''

            elif handValue(player,aceCount(player))!=21 and handValue(dealer,aceCount(dealer))==21:

                if len(dealer)==2:
                    globals()['budget']-=bet
                    return f'''Dealer has Blackjack! You lose!
You lost ${bet}'''

                else:
                    globals()['budget']-=bet
                    return f'''You lose!
You lost ${bet}'''

            elif handValue(player,aceCount(player))>21 and handValue(dealer,aceCount(dealer))>21:
                return "Both busted! It's a tie!"

            elif handValue(player,aceCount(player))>21 and handValue(dealer,aceCount(dealer))<=21:
                globals()['budget']-=bet
                return f'''You busted! Dealer wins!
You lost ${bet}'''

            elif handValue(player,aceCount(player))<=21 and handValue(dealer,aceCount(dealer))>21:
                globals()['budget']+=bet
                return f'''Dealer busted! You win!
You won ${bet}'''

            elif handValue(player,aceCount(player))<handValue(dealer,aceCount(dealer)) and handValue(dealer,aceCount(dealer))<=21:
                globals()['budget']-=bet
                return f'''You lose!
You lost ${bet}'''

            elif handValue(player,aceCount(player))>handValue(dealer,aceCount(dealer)) and handValue(player,aceCount(player))<=21:
                globals()['budget']+=bet
                return f'''You win!
You won ${bet}'''

            elif handValue(player,aceCount(player))==handValue(dealer,aceCount(dealer)) and handValue(player,aceCount(player))<=21:
                return "Push! It's a tie!"

def aceCount(person):   # EN: The function for counting the number of Aces in the hand is defined.
                        # TR: Eldeki As kartlarının sayısını saymak için fonksiyon tan

    number=0

    if "[♠ A ♠]" in person:
        number+=1

    if "[♥ A ♥]" in person:
        number+=1

    if "[♦ A ♦]" in person:
        number+=1

    if "[♣ A ♣]" in person:
        number+=1

    return number

def dealerDrawCard():   # EN: The function for the dealer to draw a card is defined.
                        # TR: Dağıtıcının kart çekmesi için fonksiyon tanımlanır.

    dealer.append(deck.pop())
    wordAnimation("Dealer drew "+str(dealer[-1]),0.05,"\n")
    time.sleep(1.5)

def help(): # EN: The function for the help screen is defined.
            # TR: Yardım ekranı için fonksiyon tanımlanır.


    os.system("cls")

    wordAnimation("Welcome to the game of Terminal Blackjack!",0.025,"\n\n")
    wordAnimation("Developed by Yusuf Kemal Erkılıç",0.025,"\n\n")
    wordAnimation("#################### HOW TO PLAY ####################",0.025,"\n\n")
    wordAnimation("The game is played with a standard deck of 52 cards.",0.025,"\n")
    wordAnimation("The deck consists of four suits: Spades (♠), Hearts (♥), Diamonds (♦), and Clubs (♣).",0.025,"\n")
    wordAnimation("Each suit has 13 cards: Ace (A), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack (J), Queen (Q), and King (K).",0.025,"\n")
    wordAnimation("The game is played between the player and the dealer.",0.025,"\n")
    wordAnimation("The player is asked for entering the amount of bet before the game.",0.025,"\n")
    wordAnimation("If the player does not want to or can not bet, the amount of bet can be entered as 0.",0.025,"\n")
    wordAnimation("In Terminal Blackjack, the goal is to get your cards as close as possible to a total value of 21 without going over.",0.025,"\n")
    wordAnimation("At the start, both the player and the dealer receive two cards. The dealer shows one card face-up and the other face-down (hole card).",0.025,"\n")
    wordAnimation("The player can choose to either HIT (draw a card) or STAND (keep the current hand).",0.025,"\n")
    wordAnimation("An Ace can be worth either 1 or 11, depending on which value benefits the player more.",0.025,"\n")
    wordAnimation("Blackjack is achieved by having an Ace and a 10-value card (10, Jack, Queen, or King) as the first two cards, totaling 21.",0.025,"\n")
    wordAnimation("The dealer must draw cards until their hand value is at least 17.",0.025,"\n")
    wordAnimation("If a player's hand exceeds 21, they go bust and automatically lose the round.",0.025,"\n")
    wordAnimation("If the dealer's hand exceeds 21, the player wins.",0.025,"\n")
    wordAnimation("If the player gets a Blackjack (a hand value of 21 with two cards), the player wins the game.",0.025,"\n")
    wordAnimation("If both the player and the dealer have the same total without BlackJack, the round results in a push, and the player’s bet is returned.",0.025,"\n")
    wordAnimation("The Blackjack holder beats a non-Blackjack 21 value holder.",0.025,"\n")
    wordAnimation("The player starts with a budget of $100. The player can bet any amount of money from the budget.",0.025,"\n")
    wordAnimation("If the player’s hand is closer to 21 than the dealer’s, the player wins the round.",0.025,"\n")
    wordAnimation("If the dealer’s hand is closer to 21 than the player’s, the dealer wins the round.",0.025,"\n")
    wordAnimation("In the case where both the player and the dealer have the same total (e.g., both have 20), the round results in a push, and the bet is returned.",0.025,"\n")
    wordAnimation("If the player wins, the player receives the bet amount. If the player loses, the player loses the bet amount.",0.025,"\n")
    wordAnimation("If the player gets a Blackjack, the player receives 1.5 times the bet amount.",0.025,"\n")
    wordAnimation("Good luck and have fun playing Terminal Blackjack!",0.025,"\n\n")
    wordAnimation("Press ENTER to continue...",0.025,"")

    input()



os.system("cls")    # EN: The screen is cleared.
                    # TR: Ekran temizlenir.

wordAnimation("Welcome to the game of Terminal Blackjack!",0.05,"\n")   # EN: The welcome message is displayed.
                                                                        # TR: Hoşgeldiniz mesajı gösterilir.

time.sleep(0.5) # EN: The program waits for 0.5 seconds.
                # TR: Program 0.5 saniye bekler.

wordAnimation("Press ENTER to continue",0.05,"")    # EN: The message for continuing the game is displayed.
                                                    # TR: Oyunun devam etmesi için mesaj gösterilir.

for i in range(3):  # EN: The dot animation is created.
                    # TR: Nokta animasyonu oluşturulur.

    time.sleep(0.5)
    print(".",end="",flush=True)
input()

while True: # EN: The main menu is created.
            # TR: Ana menü oluşturulur.

    os.system("cls")    # EN: The screen is cleared.
                        # TR: Ekran temizlenir.

    budgetAnimation()   # EN: The budget animation is displayed.
                        # TR: Bütçe animasyonu gösterilir.

    wordAnimation("1. PLAY",0.05,"\n")
    wordAnimation("2. HELP",0.05,"\n")
    wordAnimation("3. EXIT",0.05,"\n")
    wordAnimation("Enter your choice: ",0.05,"")

    choice=input()  # EN: The player's choice is taken.

    if choice=="1" or choice.upper()=="PLAY" or choice.upper()=="P":    # EN: If the player chooses PLAY, the game starts.
                                                                        # TR: Oyuncu OYNA seçeneğini seçerse, oyun başlar.

        os.system("cls")    # EN: The screen is cleared.
                            # TR: Ekran temizlenir.

        wordAnimation(str("Budget: $"+str(budget)),0.05,"\n")   # EN: The budget is displayed.
                                                                # TR: Bütçe gösterilir.

        wordAnimation("Enter your bet: ",0.05,"")
        bet=input() # EN: The player is asked to enter the bet.
                    # TR: Oyuncudan bahis girmesi istenir.

        while not bet.isdigit() or int(bet)>budget or int(bet)<=0:  # EN: If the player enters an invalid bet, the player is asked to enter a valid bet.
                                                                    # TR: Eğer oyuncu geçersiz bir bahis girerse, oyuncudan geçerli bir bahis girmesi istenir.

            os.system("cls")

            if not bet.isdigit():
                wordAnimation("Invalid input!",0.05,"\n")

            elif int(bet)<0:
                wordAnimation("Invalid input!",0.05,"\n")

            else:
                wordAnimation("Insufficient funds!",0.05,"\n")
                wordAnimation("Budget: $"+str(budget),0.05,"\n")

            wordAnimation("Enter your bet: ",0.05,"")

            bet=input()

            os.system("cls")

        bet=int(bet)

        os.system("cls")    # EN: The screen is cleared.
                            # TR: Ekran temizlenir.

        wordAnimation("Dealing cards",0.05,"")  # EN: The animation for dealing cards is displayed.
                                                # TR: Kartların dağıtılıyor olduğunu belirten bir animasyon devreye girer.

        for dot in range(3):

            if dot==2:
                for i in range(2):
                    time.sleep(0.5)
                    print(".",end="",flush=True)

            else:
                for i in range(3):
                    time.sleep(0.5)
                    print(".",end="",flush=True)
                time.sleep(0.5)
                os.system("cls")
                print("Dealing cards",end="",flush=True)

        player=[]   # EN: The player's hand is defined.
                    # TR: Oyuncunun eli tanımlanır.

        dealer=[]   # EN: The dealer's hand is defined.
                    # TR: Dağıtıcının eli tanımlanır.

        random.shuffle(deck)    # EN: The deck is shuffled.
                                # TR: Destenin karılması sağlanır.

        player.append(deck.pop())   # EN: The player draws the first card.
                                    # TR: Oyuncu ilk kartını çeker.

        dealer.append(deck.pop())   # EN: The dealer draws the first card.
                                    # TR: Dağıtıcı ilk kartını kart çeker.

        player.append(deck.pop())   # EN: The player draws the second card.
                                    # TR: Oyuncu ikinci kartını çeker.

        dealer.append(deck.pop())   # EN: The dealer draws the second card.
                                    # TR: Dağıtıcı ikinci kartını çeker.

        while True:
            
            os.system("cls")    # EN: The screen is cleared.
                                # TR: Ekran temizlenir.

            # EN: All possible results are checked and messages are displayed according to the result.
            # TR: Bütün olası sonuçlar kontrol edilir ve sonuca göre mesajlar gösterilir.

            if handValue(player,aceCount(player))==21 and handValue(dealer,aceCount(dealer))!=21 and len(player)==2:
                os.system("cls")
                wordAnimation("Dealer's hand: "+str(dealerShowHandOpen()),0.05,"\n")
                wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))),0.05,"\n\n")
                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")
                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")
                budget+=float(bet)*1.5
                wordAnimation(f'''Blackjack! You win!
You won ${float(bet)*1.5}''',0.05,"\n")
                wordAnimation("Press ENTER to continue...",0.05,"")
                input()
                break

            if handValue(player,aceCount(player))==21 and handValue(dealer,aceCount(dealer))!=21 and len(player)>2:
                os.system("cls")
                wordAnimation("Dealer's hand: "+str(dealerShowHandOpen()),0.05,"\n")
                wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))),0.05,"\n\n")
                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")
                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")
                budget+=bet
                wordAnimation(f'''You win!
You won ${bet}''',0.05,"\n")
                wordAnimation("Press ENTER to continue...",0.05,"")
                input()
                break

            if handValue(player,aceCount(player))>21 and handValue(dealer,aceCount(dealer))<=21:
                os.system("cls")
                wordAnimation("Dealer's hand: "+str(dealerShowHandOpen()),0.05,"\n")
                wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))),0.05,"\n\n")
                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")
                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")
                budget-=bet
                wordAnimation(f'''Busted! Dealer wins!
You lost ${bet}''',0.05,"\n")
                wordAnimation("Press ENTER to continue...",0.05,"")
                input()
                break

            if handValue(player,aceCount(player))>21 and handValue(dealer,aceCount(dealer))>21:
                os.system("cls")
                wordAnimation("Dealer's hand: "+str(dealerShowHandOpen()),0.05,"\n")
                wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))),0.05,"\n\n")
                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")
                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")
                wordAnimation("Both busted! It's a tie!",0.05,"\n")
                wordAnimation("Press ENTER to continue...",0.05,"")
                input()
                break

            else:
                os.system("cls")

                wordAnimation("Dealer's hand: "+str(dealerShowHand()),0.05,"\n")

                if aceCount(dealer)==0:
                    wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))-holeCard())+" + ?",0.05,"\n\n")
                if aceCount(dealer)>0 and handValue(dealer,aceCount(dealer))-holeCard()<=11:
                    wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))-holeCard())+" + ? | "+str(handValue(dealer,aceCount(dealer))-holeCard()+10)+" + ?",0.05,"\n\n")

                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")

                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")

            # EN: The player is asked to enter the move.
            # TR: Oyuncudan hamle girmesi istenir.

            wordAnimation("1. HIT",0.05,"\n")
            wordAnimation("2. STAND",0.05,"\n\n")

            wordAnimation("Enter your move: ",0.05,"")
            move=input()

            if move=="1" or move.upper()=="HIT" or move.upper()=="H":   # EN: If the player chooses HIT, the player draws a card.
                                                                        # TR: Eğer oyuncu HIT (kart çekme) seçeneğini seçerse, oyuncu bir kart çeker.

                os.system("cls")
                player.append(deck.pop())
                wordAnimation("You drew "+str(player[-1]),0.05,"\n")
                time.sleep(1.5)
                if handValue(dealer,aceCount(dealer))<17:
                    dealerDrawCard()
                else:
                    wordAnimation("Dealer stands.",0.05,"\n")
                    time.sleep(1.5)
                continue

            elif move=="2" or move.upper()=="STAND" or move.upper()=="S":   # EN: If the player chooses STAND, the player's turn ends and the dealer's turn starts.
                                                                            # TR: Eğer oyuncu STAND (pas) seçeneğini seçerse, oyuncunun sırası biter ve dağıtıcının sırası başlar.

                os.system("cls")

                while handValue(dealer,aceCount(dealer))<17:    # EN: The dealer draws cards until the hand value is at least 17.
                                                                # TR: Dağıtıcı el değeri en az 17 olana kadar kart çeker.

                    dealerDrawCard()

                os.system("cls")    # EN: The screen is cleared.
                                    # TR: Ekran temizlenir.

                # EN: The result of the game is displayed.
                # TR: Oyunun sonucu gösterilir.

                wordAnimation("Dealer's hand: "+str(dealerShowHandOpen()),0.05,"\n")
                wordAnimation("Dealer's hand value: "+str(handValue(dealer,aceCount(dealer))),0.05,"\n\n")

                wordAnimation("Your hand: "+str(playerShowHand()),0.05,"\n")
                wordAnimation("Your hand value: "+str(handValue(player,aceCount(player))),0.05,"\n\n")

                wordAnimation(result(),0.05,"\n")
                wordAnimation("Press ENTER to continue...",0.05,"")
                input()
                break



    if choice=="2" or choice.upper()=="HELP" or choice.upper()=="H":    # EN: If the player chooses HELP, the help screen is displayed.
                                                                        # TR: Oyuncu YARDIM seçeneğini seçerse, yardım ekranı gösterilir.
        help()

    if choice=="3" or choice.upper()=="EXIT" or choice.upper()=="E":    # EN: If the player chooses EXIT, the game ends.
                                                                        # TR: Oyuncu ÇIKIŞ (EXIT) seçeneğini seçerse, oyun sonlanır.
        os.system("cls")
        wordAnimation("Thank you for playing Terminal Blackjack!",0.05,"\n")
        time.sleep(1.5)
        os.system("cls")
        break