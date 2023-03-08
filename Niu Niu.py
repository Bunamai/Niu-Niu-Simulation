import warnings
warnings.filterwarnings("ignore")

import itertools
import numpy as np
import matplotlib.pyplot as plt


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

def compare_score_and_card(score1, score2, card1, card2):
    if score1 > score2:
        if score1 >= 0 & score1 <= 6:
            return [100, -100]
        elif score1 >= 7 & score1 <= 9:
            return [200, -200]
        elif score1 == 10:
            return [300, -300]
    elif score2 > score1:
        if score2 >= 0 & score2 <= 6:
            return [-100, 100]
        elif score2 >= 7 & score2 <= 9:
            return [-200, 200]
        elif score2 == 10:
            return [-300, 300]
    elif score1 == score2:
        if card1[1] > card2[1]:
            if score1 >= 0 & score1 <= 6:
                return [100, -100]
            elif score1 >= 7 & score1 <= 9:
                return [200, -200]
            elif score1 == 10:
                return [300, -300]
        elif card2[1] > card1[1]:
            if score2 >= 0 & score2 <= 6:
                return [-100, 100]
            elif score2 >= 7 & score2 <= 9:
                return [-200, 200]
            elif score2 == 10:
                return [-300, 300]
        elif card2[1] == card1[1]:
            if card1[0] > card2[0]:
                if score1 >= 0 & score1 <= 6:
                    return [100, -100]
                elif score1 >= 7 & score1 <= 9:
                    return [200, -200]
                elif score1 == 10:
                    return [300, -300]
            elif card2[0] > card1[0]:
                if score2 >= 0 & score2 <= 6:
                    return [-100, 100]
                elif score2 >= 7 & score2 <= 9:
                    return [-200, 200]
                elif score2 == 10:
                    return [-300, 300]

# main game
A = player()
B = player()
C = player()
D = player()
E = player()
trials = 1000
A_mean = []
for i in range(1, trials + 1):
    current_player = np.random.choice(["A", "B", "C", "D", "E"], 1)
    if current_player == "A":
        card_list = list(range(1, 53))
        card_A = np.random.choice(card_list, 5, replace=False)
        A.get_card(card_A)
        card_list = remove_element(card_list, card_A)
        card_B = np.random.choice(card_list, 5,replace=False)
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
        A.update_money(compare_score_and_card(A.get_score(), B.get_score(), A.get_largest_card(card_A),
                                              B.get_largest_card(card_B))[0])
        B.update_money(compare_score_and_card(A.get_score(), B.get_score(), A.get_largest_card(card_A),
                                              B.get_largest_card(card_B))[1])
        A.update_money(compare_score_and_card(A.get_score(), C.get_score(), A.get_largest_card(card_A),
                                              C.get_largest_card(card_C))[0])
        C.update_money(compare_score_and_card(A.get_score(), C.get_score(), A.get_largest_card(card_A),
                                              C.get_largest_card(card_C))[1])
        A.update_money(compare_score_and_card(A.get_score(), D.get_score(), A.get_largest_card(card_A),
                                              D.get_largest_card(card_D))[0])
        D.update_money(compare_score_and_card(A.get_score(), D.get_score(), A.get_largest_card(card_A),
                                              D.get_largest_card(card_D))[1])
        A.update_money(compare_score_and_card(A.get_score(), E.get_score(), A.get_largest_card(card_A),
                                              E.get_largest_card(card_E))[0])
        E.update_money(compare_score_and_card(A.get_score(), E.get_score(), A.get_largest_card(card_A),
                                              E.get_largest_card(card_E))[1])
    elif current_player == "B":
        card_list = list(range(1, 53))
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
        card_list = remove_element(card_list, card_E)
        card_A = np.random.choice(card_list, 5, replace=False)
        A.get_card(card_A)
        B.update_money(compare_score_and_card(B.get_score(), C.get_score(), B.get_largest_card(card_B),
                                              C.get_largest_card(card_C))[0])
        C.update_money(compare_score_and_card(B.get_score(), C.get_score(), B.get_largest_card(card_B),
                                              C.get_largest_card(card_C))[1])
        B.update_money(compare_score_and_card(B.get_score(), D.get_score(), B.get_largest_card(card_B),
                                              D.get_largest_card(card_D))[0])
        D.update_money(compare_score_and_card(B.get_score(), D.get_score(), B.get_largest_card(card_B),
                                              D.get_largest_card(card_D))[1])
        B.update_money(compare_score_and_card(B.get_score(), E.get_score(), B.get_largest_card(card_B),
                                              E.get_largest_card(card_E))[0])
        E.update_money(compare_score_and_card(B.get_score(), E.get_score(), B.get_largest_card(card_B),
                                              E.get_largest_card(card_E))[1])
        B.update_money(compare_score_and_card(B.get_score(), A.get_score(), B.get_largest_card(card_B),
                                              A.get_largest_card(card_A))[0])
        A.update_money(compare_score_and_card(B.get_score(), A.get_score(), B.get_largest_card(card_B),
                                              A.get_largest_card(card_A))[1])
    elif current_player == "C":
        card_list = list(range(1, 53))
        card_C = np.random.choice(card_list, 5, replace=False)
        C.get_card(card_C)
        card_list = remove_element(card_list, card_C)
        card_D = np.random.choice(card_list, 5, replace=False)
        D.get_card(card_D)
        card_list = remove_element(card_list, card_D)
        card_E = np.random.choice(card_list, 5, replace=False)
        E.get_card(card_E)
        card_list = remove_element(card_list, card_E)
        card_A = np.random.choice(card_list, 5, replace=False)
        A.get_card(card_A)
        card_list = remove_element(card_list, card_A)
        card_B = np.random.choice(card_list, 5, replace=False)
        B.get_card(card_B)
        C.update_money(compare_score_and_card(C.get_score(), D.get_score(), C.get_largest_card(card_C),
                                              D.get_largest_card(card_D))[0])
        D.update_money(compare_score_and_card(C.get_score(), D.get_score(), C.get_largest_card(card_C),
                                              D.get_largest_card(card_D))[1])
        C.update_money(compare_score_and_card(C.get_score(), E.get_score(), C.get_largest_card(card_C),
                                              E.get_largest_card(card_E))[0])
        E.update_money(compare_score_and_card(C.get_score(), E.get_score(), C.get_largest_card(card_C),
                                              E.get_largest_card(card_E))[1])
        C.update_money(compare_score_and_card(C.get_score(), A.get_score(), C.get_largest_card(card_C),
                                              A.get_largest_card(card_A))[0])
        A.update_money(compare_score_and_card(C.get_score(), A.get_score(), C.get_largest_card(card_C),
                                              A.get_largest_card(card_A))[1])
        C.update_money(compare_score_and_card(C.get_score(), B.get_score(), C.get_largest_card(card_C),
                                              B.get_largest_card(card_B))[0])
        B.update_money(compare_score_and_card(C.get_score(), B.get_score(), C.get_largest_card(card_C),
                                              B.get_largest_card(card_B))[1])
    elif current_player == "D":
        card_list = list(range(1, 53))
        card_D = np.random.choice(card_list, 5, replace=False)
        D.get_card(card_D)
        card_list = remove_element(card_list, card_D)
        card_E = np.random.choice(card_list, 5, replace=False)
        E.get_card(card_E)
        card_list = remove_element(card_list, card_E)
        card_A = np.random.choice(card_list, 5, replace=False)
        A.get_card(card_A)
        card_list = remove_element(card_list, card_A)
        card_B = np.random.choice(card_list, 5, replace=False)
        B.get_card(card_B)
        card_list = remove_element(card_list, card_B)
        card_C = np.random.choice(card_list, 5, replace=False)
        C.get_card(card_C)
        D.update_money(compare_score_and_card(D.get_score(), E.get_score(), D.get_largest_card(card_D),
                                              E.get_largest_card(card_E))[0])
        E.update_money(compare_score_and_card(D.get_score(), E.get_score(), D.get_largest_card(card_D),
                                              E.get_largest_card(card_E))[1])
        D.update_money(compare_score_and_card(D.get_score(), A.get_score(), D.get_largest_card(card_D),
                                              A.get_largest_card(card_A))[0])
        A.update_money(compare_score_and_card(D.get_score(), A.get_score(), D.get_largest_card(card_D),
                                              A.get_largest_card(card_A))[1])
        D.update_money(compare_score_and_card(D.get_score(), B.get_score(), D.get_largest_card(card_D),
                                              B.get_largest_card(card_B))[0])
        B.update_money(compare_score_and_card(D.get_score(), B.get_score(), D.get_largest_card(card_D),
                                              B.get_largest_card(card_B))[1])
        D.update_money(compare_score_and_card(D.get_score(), C.get_score(), D.get_largest_card(card_D),
                                              C.get_largest_card(card_C))[0])
        C.update_money(compare_score_and_card(D.get_score(), C.get_score(), D.get_largest_card(card_D),
                                              C.get_largest_card(card_C))[1])
    elif current_player == "E":
        card_list = list(range(1, 53))
        card_E = np.random.choice(card_list, 5, replace=False)
        E.get_card(card_E)
        card_list = remove_element(card_list, card_E)
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
        E.update_money(compare_score_and_card(E.get_score(), A.get_score(), E.get_largest_card(card_E),
                                              A.get_largest_card(card_A))[0])
        A.update_money(compare_score_and_card(E.get_score(), A.get_score(), E.get_largest_card(card_E),
                                              A.get_largest_card(card_A))[1])
        E.update_money(compare_score_and_card(E.get_score(), B.get_score(), E.get_largest_card(card_E),
                                              B.get_largest_card(card_B))[0])
        B.update_money(compare_score_and_card(E.get_score(), B.get_score(), E.get_largest_card(card_E),
                                              B.get_largest_card(card_B))[1])
        E.update_money(compare_score_and_card(E.get_score(), C.get_score(), E.get_largest_card(card_E),
                                              C.get_largest_card(card_C))[0])
        C.update_money(compare_score_and_card(E.get_score(), C.get_score(), E.get_largest_card(card_E),
                                              C.get_largest_card(card_C))[1])
        E.update_money(compare_score_and_card(E.get_score(), D.get_score(), E.get_largest_card(card_E),
                                              D.get_largest_card(card_D))[0])
        D.update_money(compare_score_and_card(E.get_score(), D.get_score(), E.get_largest_card(card_E),
                                              D.get_largest_card(card_D))[1])


print(A.get_money(), B.get_money(), C.get_money(), D.get_money(), E.get_money())

