"""Demo script showing all sorting algorithms in action"""

from bubble_sort_tracker import BubbleSortTracker
from quick_sort_tracker import QuickSortTracker
from merge_sort_tracker import MergeSortTracker
from insertion_sort_tracker import InsertionSortTracker
from selection_sort_tracker import SelectionSortTracker

def print_separator(title=""):
    """Print a formatted separator"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}")
    else:
        print(f"{'='*60}")

def demo_algorithm(algorithm_class, algorithm_name, array):
    """Run a sorting algorithm and display results"""
    print(f"\n📊 {algorithm_name}")
    print(f"-" * 40)
    
    tracker = algorithm_class(array.copy())
    sorted_array, steps = tracker.sort()
    stats = tracker.get_stats()
    
    print(f"Original:  {array}")
    print(f"Sorted:    {sorted_array}")
    print(f"Steps:     {stats['steps']}")
    print(f"Comparisons: {stats['comparisons']}")
    print(f"Swaps:     {stats['swaps']}")
    
    return stats

def main():
    """Run demo of all sorting algorithms"""
    
    print_separator("SORTING ALGORITHM VISUALIZER - DEMO")
    
    # Test arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [3, 3, 1, 2, 3],
    ]
    
    results = {}
    
    for arr_idx, test_array in enumerate(test_arrays, 1):
        print_separator(f"Test Array {arr_idx}: {test_array}")
        
        algorithms = [
            (BubbleSortTracker, "Bubble Sort"),
            (SelectionSortTracker, "Selection Sort"),
            (InsertionSortTracker, "Insertion Sort"),
            (MergeSortTracker, "Merge Sort"),
            (QuickSortTracker, "Quick Sort"),
        ]
        
        results[f"Array_{arr_idx}"] = {}
        
        for algo_class, algo_name in algorithms:
            try:
                stats = demo_algorithm(algo_class, algo_name, test_array)
                results[f"Array_{arr_idx}"][algo_name] = stats
            except Exception as e:
                print(f"❌ Error in {algo_name}: {e}")
    
    # Print comparison summary
    print_separator("PERFORMANCE COMPARISON SUMMARY")
    
    for arr_name, arr_results in results.items():
        print(f"\n📈 {arr_name}:")
        print("-" * 40)
        
        # Find minimums for comparison
        min_steps = min((v['steps'] for v in arr_results.values()), default=float('inf'))
        min_comparisons = min((v['comparisons'] for v in arr_results.values()), default=float('inf'))
        min_swaps = min((v['swaps'] for v in arr_results.values()), default=float('inf'))
        
        for algo_name, stats in arr_results.items():
            steps_indicator = "✓" if stats['steps'] == min_steps else " "
            comp_indicator = "✓" if stats['comparisons'] == min_comparisons else " "
            swap_indicator = "✓" if stats['swaps'] == min_swaps else " "
            
            print(f"\n  {algo_name}:")
            print(f"    Steps:       {stats['steps']:3d} {steps_indicator} (lowest = ✓)")
            print(f"    Comparisons: {stats['comparisons']:3d} {comp_indicator}")
            print(f"    Swaps:       {stats['swaps']:3d} {swap_indicator}")
    
    print_separator()
    
    # Educational notes
    print("\n📚 ALGORITHM NOTES:\n")
    print("Bubble Sort:")
    print("  - Time: O(n²) | Space: O(1)")
    print("  - Simple but slow for large datasets")
    print("  - Good for learning")
    
    print("\nSelection Sort:")
    print("  - Time: O(n²) | Space: O(1)")
    print("  - Minimizes writes (useful for slow memory)")
    print("  - Consistent performance")
    
    print("\nInsertion Sort:")
    print("  - Time: O(n²) avg, O(n) best | Space: O(1)")
    print("  - Efficient for small/nearly sorted data")
    print("  - Used in hybrid algorithms")
    
    print("\nMerge Sort:")
    print("  - Time: O(n log n) guaranteed | Space: O(n)")
    print("  - Stable and predictable")
    print("  - Requires extra memory")
    
    print("\nQuick Sort:")
    print("  - Time: O(n log n) avg, O(n²) worst | Space: O(log n)")
    print("  - Fast in practice")
    print("  - Widely used in production")
    
    print("\n" + "="*60)
    print("\n✅ Demo completed! To see animated visualizations, run:")
    print("   python sort_visualizer_gui.py")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
