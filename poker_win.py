import re
import time

opportunities = ["2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "b", "d", "k", "a"]
color = ["H", "P", "r", "a"]

mein = ["P_10", "P_b", "P_d"]
mo = ["P_9", "P_9", "P_k", "P_a"]

one_pair = False
two_pair = False
drillinge = False
vierlinge = False
high_card = ""
straight = False
flush = False
full_house = False
straight_flush = False
royal_flush = False
number = 0
hi_ca = {}


def Pair(st):

    global one_pair
    global two_pair
    global drillinge
    global vierlinge
    global number
    p = 0
    number_one_pair = 0
    number_two_pair = 0
    number_drillinge = 0
    number_vierlinge = 0

    for i in opportunities:
        x = re.findall(i, st)

        if x and len(x) >= 2:
            if i == "a":
                number = 12
            elif i == "k":
                number = 11
            elif i == "d":
                number = 10
            elif i == "b":
                number = 10
            elif i in str((2, 3, 4, 5, 6, 7, 8, 9, 10)):
                number = int(i) - 2
            le = len(x)

            if le == 2 and one_pair == False:
                one_pair = True
                p = 1
                number_one_pair = number

            elif le == 2 and one_pair == True and p == 1:
                two_pair = True
                one_pair = False

                if number > number_one_pair:
                    number_two_pair = number
                else:
                    number_two_pair = number_one_pair

            elif le == 3:
                drillinge = True
                number_drillinge = number

            elif le == 4:
                vierlinge = True
                number_vierlinge = number

    if vierlinge:
        return number_vierlinge
    elif drillinge:
        return number_drillinge
    elif two_pair:
        return number_two_pair
    elif one_pair:
        return number_one_pair


def Flush(st):
    global flush

    for j in color:
        e = re.findall(j, st)
        w = e
        if len(e) >= 5:
            w = e[0]
            flush = True
            for q in reversed(opportunities):
                x = re.search(q, st)
                if x:
                    zh = x.start()-2
                    if st[zh] in w:
                        val = x.group()
                        if val == "a":
                            return 12
                        elif val == "k":
                            return 11
                        elif val == "d":
                            return 10
                        elif val == "b":
                            return 9
                        elif val in str((2, 3, 4, 5, 6, 7, 8, 9, 10)):
                            return int(val)-2


def Straight(st):
    global straight

    last_state = False
    last = 0
    again = 0
    number_list = []

    for i in opportunities:
        f = re.search(i, st)
        if f:
            number_list.append(True)
        else:
            number_list.append(False)

    for j in range(12, -1, -1):
        if again == 5:
            straight = True
            return last
        if number_list[j] == True:
            if last_state == False:
                last = j
            again += 1
            last_state = True
        else:
            again = 0
            last_state = False


def Full_House(st):
    global full_house
    global drillinge
    global one_pair

    if drillinge == True:
        if one_pair == True:
            num = Pair(st)
            one_pair = False
            drillinge = False
            full_house = True
            return num


def Straight_Flush(st):
    global straight_flush
    global royal_flush

    last_state = False
    last = 0
    again = 0
    number_list = []
    number_span = []
    last_color = ""

    for i in opportunities:
        f = re.search(i, st)
        if f:
            number_list.append(True)
            co = f.start() - 2
            number_span.append(int(co))
        else:
            number_list.append(False)
            number_span.append(0)

    for j in range(12, -1, -1):

        if again == 5:
            if last == 12:
                royal_flush = True
                return 12
            else:
                straight_flush = True
                return last

        if number_list[j] == True:
            if last_color == st[number_span[j]] or not last_color:
                again += 1

                if last_state == False:
                    last = j
                last_state = True
            else:
                again = 1

            last_color = st[number_span[j]]

        else:
            again = 0
            last_state = False


def High_Card(st):
    global high_card

    if not one_pair or not two_pair or not drillinge or not vierlinge or not straight or not flush or not full_house or not straight_flush or not royal_flush:
        for i in reversed(opportunities):
            if i in st:
                high_card = i
                return high_card


def win_reset():
    global one_pair
    global two_pair
    global drillinge
    global vierlinge
    global high_card
    global straight
    global flush
    global full_house
    global straight_flush
    global royal_flush
    global number

    one_pair = False
    two_pair = False
    drillinge = False
    vierlinge = False
    high_card = ""
    straight = False
    flush = False
    full_house = False
    straight_flush = False
    royal_flush = False
    number = 0


def Highest(your_cards, comm_cards):
    global hi_ca

    k = your_cards + comm_cards
    st = " ".join(k)

    val_straight = Straight(st)
    val_pair = Pair(st)
    val_straight_flush = Straight_Flush(st)
    val_flush = Flush(st)
    val_full_house = Full_House(st)
    high_ca = High_Card(st)

    if royal_flush:
        return val_straight_flush, 10
    elif straight_flush:
        return val_straight_flush, 9
    elif vierlinge:
        return val_pair, 8
    elif full_house:
        return val_full_house, 7
    elif flush:
        return val_flush, 6
    elif straight:
        return val_straight, 5
    elif drillinge:
        return val_pair, 4
    elif two_pair:
        return val_pair, 3
    elif one_pair:
        return val_pair, 2
    else:
        return high_ca
