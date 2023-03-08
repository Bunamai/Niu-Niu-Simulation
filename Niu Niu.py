import warnings
warnings.filterwarnings("ignore")

import itertools
import numpy as np


def remove_element(list1, list2):
    for item2 in list2:
        for item1 in list1:
            if item1 == item2:
                list1.remove(item2)
    return list1


class player:
    def __init__(self):
        self.money = 0
        self.card = []

# Draw a card from the stack and store it
    def get_card(self, card_list):
        self.card = []
        for card in card_list:
            if card >= 1 & card <= 13:
                if card >= 10:
                    self.card.append(10)
                else:
                    self.card.append(card)
            elif card >= 14 & card <= 26:
                card = card - 13
                if card >= 10:
                    self.card.append(10)
                else:
                    self.card.append(card)
            elif card >= 27 & card <= 39:
                card = card - 26
                if card >= 10:
                    self.card.append(10)
                else:
                    self.card.append(card)
            elif card >= 40 & card <= 52:
                card = card - 39
                if card >= 10:
                    self.card.append(10)
                else:
                    self.card.append(card)

    def get_score(self):
        for combination in itertools.combinations(self.card, 3):
            if np.sum(combination) % 10 == 0:
                score = np.sum(self.card) - np.sum(combination)
                if score > 10:
                    return score - 10
                else:
                    return score
        return 0

    def get_largest_card(self, card_list):
        num_n_col = []
        for card in card_list:
            if card >= 1 & card <= 13:
                num_n_col.append([1, card])
            elif card >= 14 & card <= 26:
                card = card - 13
                num_n_col.append([2, card])
            elif card >= 27 & card <= 39:
                card = card - 26
                num_n_col.append([3, card])
            elif card >= 40 & card <= 52:
                card = card - 39
                num_n_col.append([4, card])
        max_card = [1, 1]
        for card in num_n_col:
            if card[1] > max_card[1]:
                max_card = card
            elif card[1] == max_card[1]:
                if card[0] > max_card[0]:
                    max_card = card
        return max_card

    def update_money(self, money):
        self.money = self.money + money

    def get_money(self):
        return self.money

def compute_bet_win(score, bet):
    if score >= 0 & score <= 6:
        return [bet, -1 * bet]
    elif score >= 7 & score <= 9:
        return [2 * bet, -2 * bet]
    elif score == 10:
        return [3 * bet, -3 * bet]

def compute_bet_lose(score, bet):
    if score >= 0 & score <= 6:
        return [-bet, bet]
    elif score >= 7 & score <= 9:
        return [-2 * bet, 2 * bet]
    elif score == 10:
        return [-3 * bet, 3 * bet]

def compare_score_and_card(score1, score2, card1, card2, current_money):
    bet = np.random.choice([500, np.max([int(current_money / 5), 750]), np.max([int(current_money / 3), 1000])], 1)[0]
    if score1 > score2:
        return compute_bet_win(score1, bet)
    elif score2 > score1:
        return compute_bet_lose(score2, bet)
    elif score1 == score2:
        if card1[1] > card2[1]:
            return compute_bet_win(score1, bet)
        elif card2[1] > card1[1]:
            return compute_bet_lose(score2, bet)
        elif card2[1] == card1[1]:
            if card1[0] > card2[0]:
                return compute_bet_win(score1, bet)
            elif card2[0] > card1[0]:
                return compute_bet_lose(score2, bet)

def Niu_Niu_round(A, B, C, D, E):
    card_list = list(range(1, 53))
    card_A = np.random.choice(card_list, 5, replace=False)
    A.get_card(card_A)
    card_list = remove_element(card_list, card_A)
    card_B = np.random.choice(card_list, 5, replace=False)
    B.get_card(card_B)
    card_list = remove_element(card_list, card_B)
    card_C = np.random.choice(card_list, 5, replace=False)
    C.get_card(card_C)
    card_list = remove_element(card_list, card_C)
    card_D = np.random.choice(card_list, 5, replace=False)
    D.get_card(card_D)
    card_list = remove_element(card_list, card_D)
    card_E = np.random.choice(card_list, 5, replace=False)
    E.get_card(card_E)
    Compare_AB = compare_score_and_card(A.get_score(), B.get_score(), A.get_largest_card(card_A),
                                          B.get_largest_card(card_B), B.get_money())
    A.update_money(Compare_AB[0])
    B.update_money(Compare_AB[1])
    Compare_AC = compare_score_and_card(A.get_score(), C.get_score(), A.get_largest_card(card_A),
                                          C.get_largest_card(card_C), C.get_money())
    A.update_money(Compare_AC[0])
    C.update_money(Compare_AC[1])
    Compare_AD = compare_score_and_card(A.get_score(), D.get_score(), A.get_largest_card(card_A),
                                          D.get_largest_card(card_D), D.get_money())
    A.update_money(Compare_AD[0])
    D.update_money(Compare_AD[1])
    Compare_AE = compare_score_and_card(A.get_score(), E.get_score(), A.get_largest_card(card_A),
                                          E.get_largest_card(card_E), E.get_money())
    A.update_money(Compare_AE[0])
    E.update_money(Compare_AE[1])


trials = 100
A = player()
B = player()
C = player()
D = player()
E = player()
for n in range(trials):
    current_player = np.random.choice(["A", "B", "C", "D", "E"], 1)
    if current_player == "A":
        Niu_Niu_round(A, B, C, D, E)
    elif current_player == "B":
        Niu_Niu_round(B, C, D, E, A)
    elif current_player == "C":
        Niu_Niu_round(C, D, E, A, B)
    elif current_player == "D":
        Niu_Niu_round(D, E, A, B, C)
    elif current_player == "E":
        Niu_Niu_round(E, A, B, C, D)

print(A.get_money(), B.get_money(), C.get_money(), D.get_money(), E.get_money())



