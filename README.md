# EN:

**Name:** terminal_blackjack

**Version:** *v1.0.0*

**Author:** Yusuf Kemal Erkılıç

**Date:** 17.11.2024 (dd.mm.yyyy)

**Purpose:**
This Python script allows playing Blackjack on the terminal.
At the beginning of the game, the player is given a virtual budget of $100. The player can place bets from this budget.
The money in this game is virtual and not real.

**Description:**
A deck of 52 cards is defined.
The budget is defined as $100.
Word animations and budget animations are created.
The player encounters 3 options in the main menu: PLAY, HELP, EXIT.
If the player chooses PLAY, the player is directed to the bet screen.
The player places a bet and the cards are dealt.
The player and the dealer receive two cards each.
The values of the cards are determined by the numbers and symbols on the cards.
Cards with a number on them have that number value.
Jack (J), Queen (Q), and King (K) cards have a value of 10.
The Ace (A) card has a value of 1 or 11 depending on the player's hand.
The card values are calculated and the player is offered the options to draw a card (HIT) or stand (STAND).
The player is offered the options to draw a card and stand.
If the player chooses to draw a card, a card is drawn and added to the player's hand.
If the player chooses to stand, the card drawing process ends and the turn passes to the dealer.
The dealer draws cards until reaching a hand value of 17 or higher.
After the player and the dealer draw cards, the values of the hands are compared.
The player and the dealer try to have a hand value closest to 21.
If the player and the dealer exceed 21, the hand is lost.
If the player has a hand value closest to 21, the hand is won.
If the player has a hand value closest to 21 and uses only 2 cards to reach 21, the player has Blackjack.
Blackjack pays 1.5 times the bet amount to the player.
If the player and the dealer have 21 at the same time, the player who has Blackjack wins.
If no one has Blackjack and the player and the dealer have the same hand value, the hand is tied and the player's bet is refunded.
If both sides have Blackjack, the hand is tied and the player's bet is refunded.
The player ends the game and returns to the main menu.
If the player chooses HELP, the player receives information about the game.
If the player chooses EXIT, the game ends.



# TR:

**İsim:** terminal_blackjack

**Sürüm:** *v1.0.0*

**Yazar:** Yusuf Kemal Erkılıç

**Tarih:** 17.11.2024 (gg.aa.yyyy)

**Amaç:**
Bu Python betiği, terminal üzerinden Blackjack oynanmasını sağlar.
Oyun başında oyuncuya 100$ sanal bütçe verilir. Oyuncu, bu bütçe üzerinden bahis yatırabilir.
Bu oyundaki paralar sanaldır ve gerçek değildir.

**Açıklama:**
52 kartlık bir deste tanımlanır.
Bütçe 100$ olarak tanımlanır.
Kelime animasyonları ve bütçe animasyonları oluşturulur.
Oyuncu ana menüde 3 seçenekle karşılaşır: OYNA (PLAY), YARDIM (HELP) ÇIKIŞ (EXIT).
Oyuncu, OYNA seçeneğini seçerse, bahis yapma ekranına yönlendirilir.
Oyuncu, bahis yapar ve kartlar dağıtılır.
Oyuncu ve dağıtıcı (dealer) ikişer kart alır.
Kart değerleri kartın üzerindeki sayı ve sembollerle belirlenir.
Üzerinde bir sayı olan kartlar, o sayı değerine sahiptir.
Vale (J), Kız (Q) ve Papaz (K) kartları 10 değerine sahiptir.
As (A) kartı, oyuncunun eline göre 1 veya 11 değerine sahiptir.
Kart değerleri hesaplanır ve oyuncuya kart çekme (HIT) ve pas (STAND) seçenekleri sunulur.
Oyuncuya, kart çekme ve pas verme seçenekleri sunulur.
Oyuncu, kart çekme seçeneğini seçerse, bir kart çeker ve kart eline eklenir.
Oyuncu, pas verme seçeneğini seçerse, kart çekme işlemi sona erer ve sıra dağıtıcıya (dealer) geçer.
Dağıtıcı, 17 veya daha yüksek bir el değerine ulaşana kadar kart çeker.
Oyuncu ve dağıtıcı, kart çekme işlemi sona erdikten sonra ellerin değerleri karşılaştırılır.
Oyuncu ve dağıtıcı, 21'e en yakın el değerine sahip olmaya çalışır.
Oyuncu ve dağıtıcı, 21'i aşarsa, eli kaybeder.
Oyuncu, 21'e en yakın el değerine sahipse, eli kazanır.
Oyuncu, 21'e en yakın el değerine sahipse ve 21'e ulaşmak için sadece 2 kart kullanmışsa, Blackjack yapmış olur.
Blackjack, oyuncuya bahis miktarının 1.5 katı ödeme yapar.
Oyuncu ve dağıtıcı, aynı anda 21 el değerine sahip olursa, Blackjack yapmış olan kazanır.
Eğer Blackjack yapan yoksa ve oyuncu ile dağıtıcı, aynı el değerine sahipse, el berabere biter ve oyuncunun bahsi geri ödenir.
Eğer iki tarafta Blackjack yaparsa, el berabere biter ve oyuncunun bahsi geri ödenir.
Oyuncu, oyunu bitirir ve ana menüye döner.
Oyuncu, YARDIM seçeneğini seçerse, oyun hakkında bilgi alır.
Oyuncu, ÇIKIŞ seçeneğini seçerse, oyunu sonlandırır.
