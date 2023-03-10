import unittest
from main import *


class TestMainFunctions(unittest.TestCase):
    def test_roll_dice(self):
        dice_roll = roll_dice()
        self.assertTrue(dice_roll in range(1, 7))

    def test_roll_attacker_and_defender(self):
        attacker, defender = roll_attacker_and_defender(4, 3)
        self.assertEqual(3, len(attacker))
        self.assertEqual(2, len(defender))

    def test_find_loser(self):
        attacker_loss, defender_loss = find_loser(3, 2)
        self.assertEqual(2, attacker_loss + defender_loss)

    def test_battle(self):
        winner = battle(3, 2)
        self.assertTrue(winner in ['attacker', 'defender'])

    def test_battle_simulator(self):
        attacker_wins, defender_wins, percent_attacker_wins, percent_defender_wins = battle_simulator(3, 2, 100)
        self.assertEqual(100, attacker_wins + defender_wins)
        self.assertEqual(100, percent_attacker_wins + percent_defender_wins)

if __name__ == '__main__':
    unittest.main()
