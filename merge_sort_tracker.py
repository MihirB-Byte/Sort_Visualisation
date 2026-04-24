"""Merge Sort with step-by-step tracking for visualization"""

class MergeSortTracker:
    def __init__(self, arr):
        self.original_list = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self):
        """Perform merge sort and track all steps"""
        arr = self.original_list.copy()
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'start',
            'sorted_indices': []
        })
        self._merge_sort(arr, 0, len(arr) - 1)
        
        # Final sorted state
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'complete',
            'sorted_indices': list(range(len(arr)))
        })
        
        return arr, self.steps
    
    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)
    
    def _merge(self, arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            self.comparisons += 1
            self.steps.append({
                'array': arr.copy(),
                'comparing': [left + i, mid + 1 + j],
                'action': 'comparing',
                'sorted_indices': []
            })
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            self.swaps += 1
            self.steps.append({
                'array': arr.copy(),
                'comparing': [],
                'action': 'place',
                'sorted_indices': []
            })
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            self.swaps += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            self.swaps += 1
    
    def get_stats(self):
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'steps': len(self.steps)
        }
