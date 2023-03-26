import unittest

from src.topologies import RingTopology


class RingTopologyTest(unittest.TestCase):

    def test_general_case(self):
        self.assertEqual(
            RingTopology(4).create(),
            {
                0: [1, 3],
                1: [0, 2],
                2: [1, 3],
                3: [0, 2]
            }
        )

    def test_small_case(self):
        self.assertEqual(
            RingTopology(2).create(),
            {
                0: [1],
                1: [0]
            }
        )



if __name__ == '__main__':
    unittest.main()
