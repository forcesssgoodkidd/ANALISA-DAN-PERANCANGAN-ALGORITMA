import sys
import os
import unittest

# supaya bisa import dari src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from algorithm import resource_allocation


class TestResourceAllocation(unittest.TestCase):

    def test_output_is_list(self):
        tasks = [10, 20, 30]
        cpu = 3
        gpu = 6
        result = resource_allocation(tasks, cpu, gpu)
        self.assertIsInstance(result, list)

    def test_output_length(self):
        tasks = [5, 15, 25, 35]
        cpu = 2
        gpu = 4
        result = resource_allocation(tasks, cpu, gpu)
        self.assertEqual(len(result), len(tasks))

    def test_energy_positive(self):
        tasks = [10, 20]
        cpu = 2
        gpu = 5
        result = resource_allocation(tasks, cpu, gpu)
        for item in result:
            self.assertGreaterEqual(item["energy"], 0)


if __name__ == "__main__":
    unittest.main()
