"""Selection Sort with step-by-step tracking for visualization"""

class SelectionSortTracker:
    def __init__(self, arr):
        self.original_list = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self):
        """Perform selection sort and track all steps"""
        arr = self.original_list.copy()
        n = len(arr)
        sorted_indices = []
        
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'start',
            'sorted_indices': sorted_indices.copy()
        })
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                self.comparisons += 1
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [min_idx, j],
                    'action': 'comparing',
                    'sorted_indices': sorted_indices.copy()
                })
                
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                self.swaps += 1
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [i, min_idx],
                    'action': 'swap',
                    'sorted_indices': sorted_indices.copy()
                })
            
            sorted_indices.append(i)
            self.steps.append({
                'array': arr.copy(),
                'comparing': [],
                'action': 'sort',
                'sorted_indices': sorted_indices.copy()
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
