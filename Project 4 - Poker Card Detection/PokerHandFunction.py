def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []
    for card in hand:
        if len(card)>2:
            rank = card[0:2]
            suit = card[2]
        else:
            rank = card[0]
            suit = card[1]
        if rank == 'A':
            rank = 14
        elif rank == 'K':
            rank = 13
        elif rank == 'Q':
            rank = 12
        elif rank == 'J':
            rank = 11
        ranks.append(int(rank))
        suits.append(suit)


    sortedRanks = sorted(ranks)
    # print(ranks, suits)
    # print(sortedRanks)
    # print(hand)

    # Royal Flush and Straight Flush and Flush
    if suits.count(suits[0]) == len(suits):
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks \
            and 10 in sortedRanks: # Royal Flush
            possibleRanks.append(10)
        elif all(sortedRanks[i] == sortedRanks[i-1] +1 for i in range(1, len(sortedRanks))): # Straight
            possibleRanks.append(9)
        else: # Flush
            possibleRanks.append(6)

    # Straight
    if all(sortedRanks[i] == sortedRanks[i-1] +1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)

    # Four of a kind and Full House
    handUniqueValues = list(set(sortedRanks))
    # print(handUniqueValues)
    if len(handUniqueValues) == 2:
        for val in handUniqueValues:
            if sortedRanks.count(val) == 4: # Four of a kind
                possibleRanks.append(8)
            if sortedRanks.count(val) == 3: # Full House
                possibleRanks.append(7)

    # Three of a kind and two pair
    if len(handUniqueValues) == 3:
        for val in handUniqueValues:
            if sortedRanks.count(val) == 3: # three of a kind
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2: # Two pair
                possibleRanks.append(3)

    # pair
    if len(handUniqueValues) == 4:
        possibleRanks.append(2)


    if not possibleRanks:
        possibleRanks.append(1)
    pokerHandRanks = {10:"Royal Flush", 9: "Straight Flush", 8: "Four of a Kind",
                      7: "Full House", 6: "Flush", 5:"Straight", 4: 'Three of a kind',
                      3:"Two pair", 2:"pair", 1:"High Card"}
    output = pokerHandRanks[max(possibleRanks)]
    print(hand, output)
    return output

if __name__ == "__main__":
    findPokerHand(['AH', 'KH', 'QH', 'JH', '10H']) # Royal Flush
    findPokerHand(['QC', 'JC', '10C', '9C', '8C']) # Straight Flush
    findPokerHand(['5C', '5S', '5H', '5D', 'QH']) # 4 of a kind
    findPokerHand(['2H', '2D', '2S', '10H', '10C']) # Full House
    findPokerHand(['2D', 'KD', '7D', '6D', '5D']) # Flush
    findPokerHand(['JC', '10H', '9C', '8C', '7D']) # Straight
    findPokerHand(['10H', '10C', '10D', '2D', '5S']) # Three of a kind
    findPokerHand(['KD', 'KH', '5C', '5S', '6D']) # Two pair
    findPokerHand(['2D', '2S', '9C', 'KD', '10C']) # Pair
    findPokerHand(['KD', '5H', '2D', '10C', 'JH']) # High card



