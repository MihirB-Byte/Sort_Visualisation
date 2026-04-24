# Sort Visualization

An interactive Python application for visually understanding how different sorting algorithms work. Watch in real-time as arrays are sorted using various techniques!

## Features

✨ **5 Sorting Algorithms**
- Bubble Sort
- Quick Sort
- Merge Sort
- Insertion Sort
- Selection Sort

🎨 **Interactive Visualization**
- Real-time animated sorting process
- Color-coded visualization:
  - 🔵 Blue = Unsorted elements
  - 🔴 Red = Currently comparing/processing
  - 🟢 Green = Sorted elements
- Adjustable animation speed
- Manual step-by-step navigation

📊 **Performance Metrics**
- Real-time comparison counter
- Swap counter
- Total steps display
- Algorithm efficiency comparison

🎮 **Full Control**
- Customizable array sizes (5-100 elements)
- Play/Pause/Resume animation
- Step through manually
- Speed slider
- Random array generation

## Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository:
```bash
git clone https://github.com/MihirB-Byte/Sort_Visualisation.git
cd Sort_Visualisation
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Launch the GUI Application

```bash
python sort_visualizer_gui.py
```

This opens the interactive visualizer where you can:
1. Generate a random array (adjust size with the spinbox)
2. Select a sorting algorithm from the dropdown
3. Click "Start" to watch the animation
4. Use "Pause"/"Resume" to control playback
5. Use "Previous"/"Next" for manual step navigation
6. Adjust speed with the slider
7. View real-time statistics

### Run the Command-Line Demo

```bash
python demo.py
```

This demonstrates all sorting algorithms with sample arrays and prints statistics.

### Run Tests

```bash
python test_sorting.py
```

Runs comprehensive unit tests for all sorting algorithms.

## Sorting Algorithms Explained

### Bubble Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order
- **Best for:** Learning, small datasets
- **Worst for:** Large datasets

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** Divides the array into sorted and unsorted regions, repeatedly finds the minimum element from the unsorted region and moves it to the sorted region
- **Best for:** Minimal memory writes
- **Worst for:** Large datasets

### Insertion Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** Builds the sorted array one item at a time by inserting elements into their correct position
- **Best for:** Small datasets, nearly sorted data
- **Worst for:** Large unsorted datasets

### Merge Sort
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **How it works:** Divide-and-conquer approach: divides array into halves, recursively sorts them, then merges the sorted halves
- **Best for:** Large datasets, guaranteed O(n log n)
- **Worst for:** Requires extra space

### Quick Sort
- **Time Complexity:** O(n log n) average, O(n²) worst case
- **Space Complexity:** O(log n)
- **How it works:** Divide-and-conquer: partitions around a pivot, recursively sorts partitions
- **Best for:** General-purpose, efficient on average
- **Worst for:** Poor pivot selection on already sorted data

## Project Structure

```
Sort_Visualisation/
├── sort_visualizer_gui.py      # Main PyQt5 GUI application
├── visualizer.py               # Matplotlib visualization engine
├── bubble_sort_tracker.py      # Bubble Sort with step tracking
├── quick_sort_tracker.py       # Quick Sort with step tracking
├── merge_sort_tracker.py       # Merge Sort with step tracking
├── insertion_sort_tracker.py   # Insertion Sort with step tracking
├── selection_sort_tracker.py   # Selection Sort with step tracking
├── demo.py                     # Command-line demo
├── test_sorting.py             # Unit tests
├─��� requirements.txt            # Dependencies
└── README.md                   # This file
```

## How It Works

1. **Tracking**: Each sorting algorithm has a "Tracker" class that records every step of the sorting process, including:
   - Current state of the array
   - Which elements are being compared
   - Which elements are already sorted
   - Type of operation (comparison, swap, placement, etc.)

2. **Visualization**: The `visualizer.py` module uses matplotlib to create animations based on the tracked steps

3. **GUI**: PyQt5 provides an interactive interface where users can control the animation and select algorithms

## Example Usage

### In Python Code

```python
from bubble_sort_tracker import BubbleSortTracker
from visualizer import SortVisualizer

# Create array and tracker
arr = [64, 34, 25, 12, 22, 11, 90]
tracker = BubbleSortTracker(arr)

# Sort and get steps
sorted_arr, steps = tracker.sort()
stats = tracker.get_stats()

print(f"Comparisons: {stats['comparisons']}")
print(f"Swaps: {stats['swaps']}")

# Visualize
vis = SortVisualizer(steps, "Bubble Sort Visualization")
vis.show_animation(interval=200)  # 200ms between frames
```

## Performance Comparison

Use the visualizer to compare how different algorithms perform on the same array:
- Watch which algorithm completes fastest
- Compare number of comparisons and swaps
- Understand algorithm characteristics

## Troubleshooting

### "ModuleNotFoundError: No module named 'PyQt5'"
- Solution: Run `pip install -r requirements.txt`

### Application crashes when starting sorting
- Solution: Make sure you've generated an array first (click "Generate Array")

### Animation is too fast/slow
- Solution: Use the speed slider to adjust animation speed

### Array sizes above 100
- Current: Limited to 100 elements for performance
- To increase: Modify the spinbox range in `sort_visualizer_gui.py`

## Learning Resources

- [Sorting Algorithm Visualizations](https://visualgo.net/en/sorting)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Algorithm Complexity](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms)

## Future Enhancements

- [ ] Additional sorting algorithms (Heap Sort, Shell Sort, etc.)
- [ ] Sound effects for comparisons/swaps
- [ ] Algorithm comparison side-by-side
- [ ] Save/export visualizations
- [ ] Custom array input
- [ ] Data structure visualizations
- [ ] Mobile app version

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add more sorting algorithms
- Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Mihir Bachkaniwala** - [GitHub Profile](https://github.com/MihirB-Byte)

## Acknowledgments

- Inspired by popular sorting visualization websites
- Built with Python, PyQt5, and Matplotlib
- Thanks to the open-source community
