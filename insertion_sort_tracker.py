"""Insertion Sort with step-by-step tracking for visualization"""

class InsertionSortTracker:
    def __init__(self, arr):
        self.original_list = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self):
        """Perform insertion sort and track all steps"""
        arr = self.original_list.copy()
        n = len(arr)
        sorted_indices = [0]
        
        self.steps.append({
            'array': arr.copy(),
            'comparing': [],
            'action': 'start',
            'sorted_indices': sorted_indices.copy()
        })
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                self.comparisons += 1
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [j, i],
                    'action': 'comparing',
                    'sorted_indices': sorted_indices.copy()
                })
                
                arr[j + 1] = arr[j]
                self.swaps += 1
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [j, j + 1],
                    'action': 'shift',
                    'sorted_indices': sorted_indices.copy()
                })
                j -= 1
            
            arr[j + 1] = key
            sorted_indices.append(i)
            self.steps.append({
                'array': arr.copy(),
                'comparing': [],
                'action': 'place',
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
