# Playing Cards

Basically I like numbers and statistics and not necessarily in that order.  Cards have numbers and a lot of statistics.  They can also be shuffled so I'd like to build a mix of determinate and non-determinate shuffling algorithms.  Then I'd like to play a game like blackjack.  I'd like to see what kind of odds I'm playing against in real time since I seem to always be on the losing end.

Features:
* Request a shuffle anytime
* Make a bet
* choice of a couple games
** high - low
** blackjack
* Show stats about the next card
** probability below 21
** probability of win
* Explains what the numbers mean

## High - Low
A wild (number) card is chosen at random.  The player and the dealer draw a card.  Player chooses either high or low and a wager.
Once the wager is locked, the player and dealer both reveal their card.  

To win:
The choice was high and the player's card value is higher than the dealer's card value.
The choice was low and the player's card value is lower than the dealer's card value.

Draw:
In the event of a draw where the player's card is of equivalent value to the dealers and the card is not wild or an Ace, player loses.
If the card is wild OR the draw is on an Ace, player wins on the draw.

Values:
All suits are equivalent value
From low to high
Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, Ace
Notice that Ace cards can be both the highest and lowest value

Phases:
* Shuffle phase
* Wildcard phase
* Draw phase
* Wager phase
* Show phase
* Win/Lose phase

Win/Lose Phase:
On a win, increase the players money by their wager
On a loss, decrease the player's money by their wager

