"""Bubble Sort with step-by-step tracking for visualization"""

class BubbleSortTracker:
    def __init__(self, arr):
        self.original_list = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self):
        """Perform bubble sort and track all steps"""
        arr = self.original_list.copy()
        n = len(arr)
        
        for i in range(n - 1):
            for j in range(n - i - 1):
                self.comparisons += 1
                # Record the comparison
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [j, j + 1],
                    'action': 'comparing',
                    'sorted_indices': list(range(n - i, n))
                })
                
                if arr[j] > arr[j + 1]:
                    self.swaps += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    # Record the swap
                    self.steps.append({
                        'array': arr.copy(),
                        'comparing': [j, j + 1],
                        'action': 'swap',
                        'sorted_indices': list(range(n - i, n))
                    })
        
        # Final sorted state
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'complete',
            'sorted_indices': list(range(n))
        })
        
        return arr, self.steps

    def get_stats(self):
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'steps': len(self.steps)
        }
