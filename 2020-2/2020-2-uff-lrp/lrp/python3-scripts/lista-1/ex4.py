entr = list(map(int, input().split()))
if len(entr) == 5:
    sorts_cards = [entr]*3

    asc = sorts_cards[0]
    desc = sorts_cards[1]
    asc.sort()
    desc.sort(reverse=True)
    print(sorts_cards)
    # for lists in sorts_cards:
    #     if lists==sorts_cards[2]:
    #         print('C')
    #         break
    #     elif lists==sorts_cards[2]:
    #         print('D') 
    #         break
    #     else:
    #         print('N') 
    #         break