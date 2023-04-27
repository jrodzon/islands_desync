import unittest

from islands_desync.topologies.CompleteTopology import CompleteTopology


class MyTestCase(unittest.TestCase):
    def test_general(self):
        self.assertEqual(
            {
                0: [1, 2, 3],
                1: [0, 2, 3],
                2: [0, 1, 3],
                3: [0, 1, 2],
            },
            CompleteTopology(4).create(),
        )

    def test_small_case(self):
        self.assertEqual({0: []}, CompleteTopology(1).create())


if __name__ == "__main__":
    unittest.main()
