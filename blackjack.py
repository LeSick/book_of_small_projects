import random
import sys
from typing import List


HEARTS: str = chr(9829)
DIAMONDS: str = chr(9830)
SPADES: str = chr(9824)
CLUBS: str = chr(9827)
BACKSIDE: str = 'backside'


def main():
    print(
        '''Rules:
Try to get as close to 21 without going over.
Kings, Queens and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet.
In case of a tie, the bet is returned to the player.
The dealer stops hitting on 17.
'''
    )

    money: str = 5_000
    # Main game loop
    while True:
        if money <= 0:
            print('You\'re broke!')
            print('Good thing you weren\'t playing with real money!')
            print('Thanks for playing!')
            sys.exit()

        # Let the player enter their bet for this round
        print('Money: ', money)
        bet = get_bet(money)

        # Give the dealer and player two cards from the deck each
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet: ', bet)
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust
            if get_hand_value(player_hand) > 21:
                break

            # Get the player's move, either H, S, or D
            move = get_move(player_hand, money - bet)

            # Handle the player action
            if move == 'D':
                # Player is doubling down, they can increase their bet
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # The player has busted
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn
                break

        # Handle the dealer's actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # The dealer hits
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # Handle whether the player won, lost or tied
        if dealer_value > 21:
            print(f'Dealer busts! You won ${bet}')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}!')
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


def get_bet(max_bet: int) -> int:
    '''Ask player how much he wants to bet for this rouhnd'''
    while True:
        print(f'How much do you bet? (1 - {max_bet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck() -> List:
    '''Return a list of (rank, suit) tuples for all 52 cards.'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(
        player_hand: List[str],
        dealer_hand: List[str],
        show_dealer_hand: bool
):
    '''Show player's and dealer's cards.
    Hide the deler's first card if show_dealer_hand is False.
    '''
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show player's cards
    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards: List[str]) -> int:
    '''Returns the value of the cards.'''
    value: int = 0
    number_of_aces: int = 0

    # Add value for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    # Add value for aces
    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards: List[str]) -> str:
    '''Display all the cards in the cards list.'''
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += f'| {suit} |'
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def get_move(player_hand: List[str], money: int) -> str:
    '''Ask the player for his move.'''
    while True:
        # Determine what moves the player can make
        moves = ['(H)it', '(S)tand']

        # The player can double down on his first move,
        # which we can tell because he has exactly two cards
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get player's move
        move_promt = ', '.join(moves) + '> '
        move = input(move_promt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


if __name__ == '__main__':
    main()
