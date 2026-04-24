"""PyQt5 GUI for sorting algorithm visualizer"""

import sys
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QSpinBox, QSlider, QLabel, QFrame,
    QSplitter, QGridLayout, QGroupBox
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPalette

from bubble_sort_tracker import BubbleSortTracker
from quick_sort_tracker import QuickSortTracker
from merge_sort_tracker import MergeSortTracker
from insertion_sort_tracker import InsertionSortTracker
from selection_sort_tracker import SelectionSortTracker
from visualizer import SortVisualizer

class MplCanvas(FigureCanvas):
    """Matplotlib canvas for embedding in PyQt5"""
    
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
    
    def plot_array(self, arr, comparing=None, sorted_indices=None, title="Array Visualization"):
        """Plot an array with optional highlighting"""
        self.axes.clear()
        
        if not arr:
            return
        
        max_val = max(arr) if arr else 1
        colors = ['#3498db'] * len(arr)
        
        if sorted_indices:
            for idx in sorted_indices:
                if idx < len(colors):
                    colors[idx] = '#2ecc71'
        
        if comparing:
            for idx in comparing:
                if idx < len(colors):
                    colors[idx] = '#e74c3c'
        
        bars = self.axes.bar(range(len(arr)), arr, color=colors, edgecolor='black', linewidth=0.7)
        
        self.axes.set_ylim(0, max_val * 1.2)
        self.axes.set_xlim(-0.5, len(arr) - 0.5)
        self.axes.set_ylabel('Value', fontweight='bold')
        self.axes.set_xlabel('Index', fontweight='bold')
        self.axes.set_title(title, fontweight='bold', fontsize=12)
        self.axes.set_xticks(range(len(arr)))
        
        self.fig.tight_layout()
        self.draw()

class SortVisualizerApp(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sorting Algorithm Visualizer')
        self.setGeometry(100, 100, 1400, 900)
        self.setStyleSheet("background-color: #ecf0f1;")
        
        # Data
        self.current_array = []
        self.steps = []
        self.current_step = 0
        self.is_playing = False
        self.tracker = None
        self.stats = {}
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Left panel - Controls
        left_panel = self.create_control_panel()
        
        # Right panel - Visualization
        self.canvas = MplCanvas(self, width=10, height=6, dpi=100)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(self.canvas, 2)
        
        # Timer for animation
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate_step)
        
        # Initial plot
        self.update_visualization()
    
    def create_control_panel(self):
        """Create the left control panel"""
        panel = QFrame()
        panel.setStyleSheet("background-color: white; border-radius: 5px;")
        layout = QVBoxLayout(panel)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Title
        title_label = QLabel("Sorting Visualizer")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # Array Generation Group
        array_group = QGroupBox("Array Generation")
        array_layout = QGridLayout()
        
        array_layout.addWidget(QLabel("Array Size:"), 0, 0)
        self.size_spinbox = QSpinBox()
        self.size_spinbox.setRange(5, 100)
        self.size_spinbox.setValue(20)
        self.size_spinbox.setStyleSheet("background-color: #ecf0f1; border-radius: 3px; padding: 5px;")
        array_layout.addWidget(self.size_spinbox, 0, 1)
        
        generate_btn = QPushButton("Generate Array")
        generate_btn.setStyleSheet("background-color: #3498db; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        generate_btn.clicked.connect(self.generate_array)
        array_layout.addWidget(generate_btn, 1, 0, 1, 2)
        
        array_group.setLayout(array_layout)
        layout.addWidget(array_group)
        
        # Algorithm Selection Group
        algo_group = QGroupBox("Select Algorithm")
        algo_layout = QVBoxLayout()
        
        algo_layout.addWidget(QLabel("Algorithm:"))
        self.algo_combo = QComboBox()
        self.algo_combo.addItems([
            "Bubble Sort",
            "Quick Sort",
            "Merge Sort",
            "Insertion Sort",
            "Selection Sort"
        ])
        self.algo_combo.setStyleSheet("background-color: #ecf0f1; border-radius: 3px; padding: 5px;")
        algo_layout.addWidget(self.algo_combo)
        
        algo_group.setLayout(algo_layout)
        layout.addWidget(algo_group)
        
        # Animation Controls Group
        controls_group = QGroupBox("Animation Controls")
        controls_layout = QVBoxLayout()
        
        button_layout = QHBoxLayout()
        self.start_btn = QPushButton("▶ Start")
        self.start_btn.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        self.start_btn.clicked.connect(self.start_sorting)
        button_layout.addWidget(self.start_btn)
        
        self.pause_btn = QPushButton("⏸ Pause")
        self.pause_btn.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        self.pause_btn.clicked.connect(self.pause_sorting)
        self.pause_btn.setEnabled(False)
        button_layout.addWidget(self.pause_btn)
        
        controls_layout.addLayout(button_layout)
        
        # Step Navigation
        step_layout = QHBoxLayout()
        prev_btn = QPushButton("⬅ Previous")
        prev_btn.setStyleSheet("background-color: #95a5a6; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        prev_btn.clicked.connect(self.previous_step)
        step_layout.addWidget(prev_btn)
        
        next_btn = QPushButton("Next ➜")
        next_btn.setStyleSheet("background-color: #95a5a6; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        next_btn.clicked.connect(self.next_step)
        step_layout.addWidget(next_btn)
        controls_layout.addLayout(step_layout)
        
        # Speed Control
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Speed:"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(10, 500)
        self.speed_slider.setValue(100)
        self.speed_slider.setTickPosition(QSlider.TicksBelow)
        self.speed_slider.setTickInterval(50)
        self.speed_slider.setStyleSheet("background-color: #ecf0f1; border-radius: 3px;")
        speed_layout.addWidget(self.speed_slider)
        controls_layout.addLayout(speed_layout)
        
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Statistics Group
        stats_group = QGroupBox("Statistics")
        stats_layout = QGridLayout()
        
        self.step_label = QLabel("Step: 0/0")
        self.step_label.setStyleSheet("font-weight: bold;")
        stats_layout.addWidget(self.step_label, 0, 0)
        
        self.comparisons_label = QLabel("Comparisons: 0")
        stats_layout.addWidget(self.comparisons_label, 1, 0)
        
        self.swaps_label = QLabel("Swaps: 0")
        stats_layout.addWidget(self.swaps_label, 2, 0)
        
        self.time_label = QLabel("Time: 0ms")
        stats_layout.addWidget(self.time_label, 3, 0)
        
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        # Reset Button
        reset_btn = QPushButton("🔄 Reset")
        reset_btn.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold; padding: 10px; border-radius: 4px;")
        reset_btn.clicked.connect(self.reset_visualization)
        layout.addWidget(reset_btn)
        
        layout.addStretch()
        
        return panel
    
    def generate_array(self):
        """Generate a random array"""
        size = self.size_spinbox.value()
        self.current_array = [random.randint(10, 100) for _ in range(size)]
        self.reset_visualization()
        self.update_visualization()
    
    def start_sorting(self):
        """Start the sorting animation"""
        if not self.current_array:
            self.generate_array()
        
        if self.current_step == 0:
            self.run_sorting_algorithm()
        
        if self.steps:
            self.is_playing = True
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.algo_combo.setEnabled(False)
            self.size_spinbox.setEnabled(False)
            
            interval = self.speed_slider.value()
            self.animation_timer.start(interval)
    
    def pause_sorting(self):
        """Pause the sorting animation"""
        self.is_playing = False
        self.animation_timer.stop()
        self.start_btn.setText("▶ Resume")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
    
    def animate_step(self):
        """Animate one step of sorting"""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_visualization()
        else:
            self.animation_timer.stop()
            self.is_playing = False
            self.start_btn.setEnabled(True)
            self.pause_btn.setEnabled(False)
            self.pause_btn.setText("⏸ Pause")
            self.start_btn.setText("▶ Start")
    
    def next_step(self):
        """Move to next step manually"""
        if self.steps and self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_visualization()
    
    def previous_step(self):
        """Move to previous step manually"""
        if self.current_step > 0:
            self.current_step -= 1
            self.update_visualization()
    
    def run_sorting_algorithm(self):
        """Run the selected sorting algorithm"""
        algo_index = self.algo_combo.currentIndex()
        
        if algo_index == 0:
            self.tracker = BubbleSortTracker(self.current_array)
        elif algo_index == 1:
            self.tracker = QuickSortTracker(self.current_array)
        elif algo_index == 2:
            self.tracker = MergeSortTracker(self.current_array)
        elif algo_index == 3:
            self.tracker = InsertionSortTracker(self.current_array)
        elif algo_index == 4:
            self.tracker = SelectionSortTracker(self.current_array)
        
        sorted_array, self.steps = self.tracker.sort()
        self.stats = self.tracker.get_stats()
        self.current_step = 0
    
    def update_visualization(self):
        """Update the visualization based on current step"""
        if not self.steps:
            self.canvas.plot_array(
                self.current_array if self.current_array else [1, 2, 3],
                title="Click 'Start' to begin sorting"
            )
            self.step_label.setText("Step: 0/0")
            self.comparisons_label.setText("Comparisons: 0")
            self.swaps_label.setText("Swaps: 0")
            return
        
        step_data = self.steps[self.current_step]
        title = f"{self.algo_combo.currentText()} - Step {self.current_step}/{len(self.steps)-1}"
        
        self.canvas.plot_array(
            step_data['array'],
            comparing=step_data.get('comparing'),
            sorted_indices=step_data.get('sorted_indices'),
            title=title
        )
        
        self.step_label.setText(f"Step: {self.current_step}/{len(self.steps)-1}")
        self.comparisons_label.setText(f"Comparisons: {self.stats.get('comparisons', 0)}")
        self.swaps_label.setText(f"Swaps: {self.stats.get('swaps', 0)}")
    
    def reset_visualization(self):
        """Reset the visualization to initial state"""
        self.steps = []
        self.current_step = 0
        self.is_playing = False
        self.animation_timer.stop()
        self.start_btn.setText("▶ Start")
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.algo_combo.setEnabled(True)
        self.size_spinbox.setEnabled(True)
        self.step_label.setText("Step: 0/0")
        self.comparisons_label.setText("Comparisons: 0")
        self.swaps_label.setText("Swaps: 0")
        self.update_visualization()

def main():
    app = QApplication(sys.argv)
    window = SortVisualizerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
