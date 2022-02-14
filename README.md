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
