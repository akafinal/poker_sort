import sys

def poker_sort():
    "Return how many hands each player wins"
    p1_win_count = 0 ; p2_win_count = 0
    for line in sys.stdin:
        cards = line.split()
        unique = len(set(cards)) == 10
        format = set([len(i) for i in cards]) == {2}
        suit = set([s for v,s in cards]).issubset({'C','S','H','D'})
        if unique and format and suit:
            hand1 = cards[:5]; hand2 = cards[5:]
            if max(hand1, hand2, key=card_rank) == hand1: p1_win_count +=1
            else: p2_win_count +=1
        else:
            print("Please check data file!")
            break
    print("Player 1: {0} \nPlayer 2: {1}".format(p1_win_count, p2_win_count))
    return None

def card_rank(hand):
    "Return a number showing the ranking of a hand"
    counts_and_values = collect(['--23456789TJQKA'.index(v) for v, s in hand])
    counts, values = unzip(counts_and_values)
    straight = len(set(values)) == 5 and max(values) - min(values) == 4
    flush = len(set([s for v,s in hand])) == 1

    if values == (14, 13, 12, 11, 10) and flush: return 10, values
    elif straight and flush: return 9, values
    elif counts == (4,1): return 8, values
    elif counts == (3,2): return 7, values
    elif straight: return 6, values
    elif flush: return 5, values
    elif counts == (3,1,1): return 4, values
    elif counts == (2,2,1): return 3, values
    elif counts == (2,1,1,1): return 2, values
    else: return 1, values

def collect(values):
    "Return a list of tuples. Each tuple contains (count, a card value),\
 sorted by highest count first, than highest card rank"
    counts_and_values = []
    for v in set(values):
        counts_and_values.append((values.count(v), v))
    return sorted(counts_and_values, reverse=True)

def unzip(counts_and_values):
    "Unzip - Return a list of 2 tuples, one for counts and one for card values"
    # unzip_list = [[i for i, j in groups],[j for i, j in groups]]
    return list(zip(*counts_and_values))

if __name__ == '__main__':
    poker_sort()

# def test():
#     rf = "TC JC QC KC AC".split() # royal flush
#     sf = "9C TC JC QC KC".split() # straight flush
#     fk = "3S 3D 3H 3C 4H".split()
#     fh = "8C 8D 8H 3S 3C".split()
#     tp = "7C 7H 5D 4D 4S".split()
#     fl = "2D 7D 8D 3D 5D".split() # flush
#     st = "2C 3C 4C 5S 6S".split() # straight
#     eh = "3C 4C 5S 7S 8D".split() # 8 high

    # assert card_rank(rf) == 10,
    # assert card_rank(sf) == 9
    # assert card_rank(fk) == 8
    # assert card_rank(fh) == 7
    # assert card_rank(st) == 6
    # assert card_rank(fl) == 5
    # assert card_rank(tp) == 3
    # assert card_rank(eh) == 1
    # assert poker() == "9C 9D 8D 7C 3C"
    # print ("tests pass")
