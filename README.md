# Blind_quartets
Blink Quartets card game

## Rules
[Rules in Dutch](https://pyth.eu/blind-kwartetten)

### turns
Each turn is split into two/three sub-stages.
- Optional: quartets. Player A states he/she has acumulated a quartet (names the group) and puts it aside.
- Q: First the players A who's turn it is asks an other player B for a specific card (of a group he/she owns). 
- A: Secondly that player B decides if he/she has the card.
  - If so, pass the card and A continues
  - If not, B gets the turn

Note that after each turn and sub-stage the state must be valid. 

Player A looses if declaring a imposible quartet.  
Player A looses if after player A's Question there is no valid state.  
Player B looses if after players B's Answer there is no valid state.  

### out of cards
When a player A who has the turn has run out of cards:
- The just quetioned player B gets the turn (if that one has cards left)
- Then
  - **house rule x** From the players with at least one card the first (clockwise from A) player get the turn.
  - **house rule y** From the players with the least (but at least one) cards the first (clockwise from A) player get the turn.
  - **house rule z** From the players with the most cards the first (clockwise from A) player get the turn.

### End of game
The game end when all but one player lost due to an invalid move (outcome I) or all quartets are won (outcome II).  
I: The player who didn't lose, automatically wins.  
II: The player who has the most quartets (and aquired the final one first) Wins.

## Implementation

### State
All players are represented as a list of **cards**. For all these cards their potential (or lack there of) is administered in their card representation.

#### State Update
Quartets: Four of the players cards (that have the correct potential) are collapsed into the four cards of the group.
Question:
- If the player allready has a card that is (partially) collapsed to the group, no state change is needed.
- Otherwise collapse one card (that has the correct potential) to be only of that group.
Answer:
- Yes, collapse the card (that has the correct, and least potential) and hand it over to the questioner. This automatically excludes this option from all other cards in play.
- No, exclude the specified card from all cards in the players hand.

### State check
After each player's desicion the state is updated and a check is run to verify the state is still valid after that choice.

#### Brute force method
To check a state the following brute force method can be used.  
Clone the state (keeping the origional for reference) and depth-first collapse the cards potentials while updating the concequences on the other cards, keeping track of all decisions made.  
If the this results in a imposible state, backtrack one step an try again. If all options for a card are tried backtrack an aditional position.  
If all cards are collapsed it is proven the stae is still valid, if back-tracking is reverted to the first (collapsable) card and all it's options are depleted it is proven the state is invalid.

#### Optimized brute force
Like the normal brute force method with one addition. In stead of running the brute force algoritm on the cards in order they are in play, the cards are sorted from most specified to least specified before the check algoritm starts. This way cards will probably be more restricted when selected for callapsing.

#### Early DeadEnd detection
The folowing method can be used to quickly check if the rest of the cards (rightside) does not have a chance of having a valid permutation.  
L_R = length(R)  
O_R = all R or-ed together  
chance_valid = Hamming(O_R) >= L_R  
if (!change_valid) there is no need to progress this lead further.
