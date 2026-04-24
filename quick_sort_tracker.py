"""Quick Sort with step-by-step tracking for visualization"""

class QuickSortTracker:
    def __init__(self, arr):
        self.original_list = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self):
        """Perform quick sort and track all steps"""
        arr = self.original_list.copy()
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'start',
            'sorted_indices': []
        })
        self._quicksort(arr, 0, len(arr) - 1, [])
        
        # Final sorted state
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'complete',
            'sorted_indices': list(range(len(arr)))
        })
        
        return arr, self.steps
    
    def _quicksort(self, arr, low, high, sorted_indices):
        if low < high:
            pi = self._partition(arr, low, high, sorted_indices)
            self._quicksort(arr, low, pi - 1, sorted_indices)
            self._quicksort(arr, pi + 1, high, sorted_indices)
    
    def _partition(self, arr, low, high, sorted_indices):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.comparisons += 1
            self.steps.append({
                'array': arr.copy(),
                'comparing': [j, high],
                'action': 'comparing',
                'sorted_indices': sorted_indices.copy()
            })
            
            if arr[j] < pivot:
                i += 1
                self.swaps += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [i, j],
                    'action': 'swap',
                    'sorted_indices': sorted_indices.copy()
                })
        
        self.swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.steps.append({
            'array': arr.copy(),
            'comparing': [i + 1, high],
            'action': 'swap',
            'sorted_indices': sorted_indices.copy()
        })
        
        return i + 1
    
    def get_stats(self):
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'steps': len(self.steps)
        }
