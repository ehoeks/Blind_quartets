# Blind_quartets
Blink Quartets card game

## Rules
[Rules in Dutch](https://pyth.eu/blind-kwartetten)

###
Each turn is split into two sub-stages.
- Q: First the players A who's turn it is asks an other player B for a specific card (of a group he/she owns). 
- A: Secondly that player B decides if he/she has the card.
  - If so, pass the card and A continues
  - If not, B gets the turn

## Implementation

### State
All players are represented as a list of **cards**. For all these cards their potential (or lack there of) is administered in their card representation.


### State check
After each player's desicion the state check is run to verify the state is still valid after that choice.
