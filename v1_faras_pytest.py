import unittest
from faras import Card, Hand, mapping

# Helper to make a hand from rank list and same suit

def make_hand(ranks, suit='spade'):
    return Hand([Card((suit, rank)) for rank in ranks])

class TestFaras(unittest.TestCase):

    def test_trial(self):
        hand = make_hand(['K', 'K', 'K'])
        hand.check_all()
        self.assertTrue(hand.trial)
        self.assertEqual(hand.trial_card, 'K')
        self.assertEqual(hand.max_hand, 'trial')

    def test_color(self):
        hand = Hand([Card(('heart', '5')), Card(('heart', '9')), Card(('heart', 'K'))])
        hand.check_all()
        self.assertTrue(hand.color)
        self.assertEqual(hand.color_suit, 'heart')

    def test_pair(self):
        hand = make_hand(['5', '5', '9'])
        hand.check_all()
        self.assertTrue(hand.pair)
        self.assertEqual(hand.pair_card, '5')

    def test_run_standard(self):
        hand = make_hand(['9', '10', 'J'])
        hand.check_all()
        self.assertTrue(hand.run)
        self.assertEqual(hand.run_cards, ['9', '10', 'J'])

    def test_run_with_ace_wraparound(self):
        hand = make_hand(['2', '3', 'A'])
        hand.check_all()
        self.assertTrue(hand.run)
        self.assertEqual(hand.run_cards, ['2', '3', 'A'])

    def test_double_run(self):
        hand = Hand([Card(('diamond', '9')), Card(('diamond', '10')), Card(('diamond', 'J'))])
        hand.check_all()
        self.assertTrue(hand.double_run)
        self.assertEqual(hand.double_run_suit, 'diamond')

    def test_high_card(self):
        hand = Hand([Card(('club', '2')), Card(('heart', '5')), Card(('spade', 'K'))])
        hand.check_all()
        self.assertEqual(hand.max_hand, 'high_card')
        self.assertEqual(hand.high_card, 'K')

    def test_sorted_order(self):
        hand = make_hand(['K', '2', '9'])
        hand.check_all()
        self.assertEqual(hand.sorted_hand_ranks, ['2', '9', 'K'])

    def test_pair_vs_high_card(self):
        hand_pair = make_hand(['7', '7', '4'])
        hand_pair.check_all()
        self.assertEqual(hand_pair.max_hand_val, mapping['pair'])

        hand_high = make_hand(['A', '10', '2'])
        hand_high.check_all()
        self.assertEqual(hand_high.max_hand_val, mapping['high_card'])

        self.assertGreater(hand_pair.max_hand_val, hand_high.max_hand_val)

    def test_trial_vs_double_run(self):
        hand_trial = make_hand(['8', '8', '8'])
        hand_trial.check_all()
        self.assertEqual(hand_trial.max_hand_val, mapping['trial'])

        hand_double_run = Hand([Card(('heart', '10')), Card(('heart', 'J')), Card(('heart', 'Q'))])
        hand_double_run.check_all()
        self.assertEqual(hand_double_run.max_hand_val, mapping['double_run'])

        self.assertGreater(hand_trial.max_hand_val, hand_double_run.max_hand_val)

    def test_duplicate_cards_different_suits(self):
        hand = Hand([Card(('club', '9')), Card(('spade', '9')), Card(('diamond', 'K'))])
        hand.check_all()
        self.assertTrue(hand.pair)
        self.assertEqual(hand.pair_card, '9')

    def test_invalid_run_like_QKA(self):
        hand = make_hand(['Q', 'K', 'A'])
        hand.check_all()
        self.assertFalse(hand.run)
        self.assertEqual(hand.max_hand, 'high_card')

if __name__ == '__main__':
    unittest.main()
