"""Unit tests for all sorting algorithms"""

import unittest
import random
from bubble_sort_tracker import BubbleSortTracker
from quick_sort_tracker import QuickSortTracker
from merge_sort_tracker import MergeSortTracker
from insertion_sort_tracker import InsertionSortTracker
from selection_sort_tracker import SelectionSortTracker

class TestBubbleSort(unittest.TestCase):
    """Test Bubble Sort implementation"""
    
    def test_empty_array(self):
        tracker = BubbleSortTracker([])
        result, _ = tracker.sort()
        self.assertEqual(result, [])
    
    def test_single_element(self):
        tracker = BubbleSortTracker([1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1])
    
    def test_sorted_array(self):
        tracker = BubbleSortTracker([1, 2, 3, 4, 5])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        tracker = BubbleSortTracker([5, 4, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        tracker = BubbleSortTracker([64, 34, 25, 12, 22, 11, 90])
        result, _ = tracker.sort()
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        tracker = BubbleSortTracker([3, 1, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        tracker = BubbleSortTracker([3, -1, 4, -5, 2])
        result, _ = tracker.sort()
        self.assertEqual(result, [-5, -1, 2, 3, 4])
    
    def test_steps_generated(self):
        tracker = BubbleSortTracker([3, 1, 2])
        _, steps = tracker.sort()
        self.assertGreater(len(steps), 0)
        self.assertEqual(steps[0]['action'], 'start')
        self.assertEqual(steps[-1]['action'], 'complete')

class TestQuickSort(unittest.TestCase):
    """Test Quick Sort implementation"""
    
    def test_empty_array(self):
        tracker = QuickSortTracker([])
        result, _ = tracker.sort()
        self.assertEqual(result, [])
    
    def test_single_element(self):
        tracker = QuickSortTracker([1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1])
    
    def test_sorted_array(self):
        tracker = QuickSortTracker([1, 2, 3, 4, 5])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        tracker = QuickSortTracker([5, 4, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        tracker = QuickSortTracker([64, 34, 25, 12, 22, 11, 90])
        result, _ = tracker.sort()
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        tracker = QuickSortTracker([3, 1, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        tracker = QuickSortTracker([3, -1, 4, -5, 2])
        result, _ = tracker.sort()
        self.assertEqual(result, [-5, -1, 2, 3, 4])

class TestMergeSort(unittest.TestCase):
    """Test Merge Sort implementation"""
    
    def test_empty_array(self):
        tracker = MergeSortTracker([])
        result, _ = tracker.sort()
        self.assertEqual(result, [])
    
    def test_single_element(self):
        tracker = MergeSortTracker([1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1])
    
    def test_sorted_array(self):
        tracker = MergeSortTracker([1, 2, 3, 4, 5])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        tracker = MergeSortTracker([5, 4, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        tracker = MergeSortTracker([64, 34, 25, 12, 22, 11, 90])
        result, _ = tracker.sort()
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        tracker = MergeSortTracker([3, 1, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        tracker = MergeSortTracker([3, -1, 4, -5, 2])
        result, _ = tracker.sort()
        self.assertEqual(result, [-5, -1, 2, 3, 4])

class TestInsertionSort(unittest.TestCase):
    """Test Insertion Sort implementation"""
    
    def test_empty_array(self):
        tracker = InsertionSortTracker([])
        result, _ = tracker.sort()
        self.assertEqual(result, [])
    
    def test_single_element(self):
        tracker = InsertionSortTracker([1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1])
    
    def test_sorted_array(self):
        tracker = InsertionSortTracker([1, 2, 3, 4, 5])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        tracker = InsertionSortTracker([5, 4, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        tracker = InsertionSortTracker([64, 34, 25, 12, 22, 11, 90])
        result, _ = tracker.sort()
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        tracker = InsertionSortTracker([3, 1, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        tracker = InsertionSortTracker([3, -1, 4, -5, 2])
        result, _ = tracker.sort()
        self.assertEqual(result, [-5, -1, 2, 3, 4])

class TestSelectionSort(unittest.TestCase):
    """Test Selection Sort implementation"""
    
    def test_empty_array(self):
        tracker = SelectionSortTracker([])
        result, _ = tracker.sort()
        self.assertEqual(result, [])
    
    def test_single_element(self):
        tracker = SelectionSortTracker([1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1])
    
    def test_sorted_array(self):
        tracker = SelectionSortTracker([1, 2, 3, 4, 5])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        tracker = SelectionSortTracker([5, 4, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        tracker = SelectionSortTracker([64, 34, 25, 12, 22, 11, 90])
        result, _ = tracker.sort()
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        tracker = SelectionSortTracker([3, 1, 3, 2, 1])
        result, _ = tracker.sort()
        self.assertEqual(result, [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        tracker = SelectionSortTracker([3, -1, 4, -5, 2])
        result, _ = tracker.sort()
        self.assertEqual(result, [-5, -1, 2, 3, 4])

class TestAlgorithmComparison(unittest.TestCase):
    """Compare all algorithms on the same inputs"""
    
    def test_all_algorithms_produce_same_result(self):
        test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [5, 2, 8, 1, 9],
            [3, 3, 1, 2, 3],
        ]
        
        for test_array in test_arrays:
            trackers = [
                BubbleSortTracker(test_array.copy()),
                QuickSortTracker(test_array.copy()),
                MergeSortTracker(test_array.copy()),
                InsertionSortTracker(test_array.copy()),
                SelectionSortTracker(test_array.copy()),
            ]
            
            results = []
            for tracker in trackers:
                result, _ = tracker.sort()
                results.append(result)
            
            # All results should be the same
            for i in range(1, len(results)):
                self.assertEqual(results[0], results[i])
    
    def test_random_arrays(self):
        """Test with random arrays"""
        for _ in range(10):
            test_array = [random.randint(1, 100) for _ in range(20)]
            
            trackers = [
                BubbleSortTracker(test_array.copy()),
                QuickSortTracker(test_array.copy()),
                MergeSortTracker(test_array.copy()),
                InsertionSortTracker(test_array.copy()),
                SelectionSortTracker(test_array.copy()),
            ]
            
            results = []
            for tracker in trackers:
                result, _ = tracker.sort()
                results.append(result)
            
            expected = sorted(test_array)
            for result in results:
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
