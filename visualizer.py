"""Matplotlib-based visualization engine for sorting algorithms"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import numpy as np

class SortVisualizer:
    """Visualize sorting algorithms with animated bar charts"""
    
    def __init__(self, steps, title="Sorting Algorithm Visualization", figsize=(12, 6)):
        self.steps = steps
        self.title = title
        self.figsize = figsize
        self.current_step = 0
    
    def create_animation(self, interval=100, save_path=None):
        """
        Create an animated visualization of the sorting process
        
        Args:
            interval: Delay between frames in milliseconds
            save_path: Optional path to save the animation as a file
        
        Returns:
            fig, ani: Matplotlib figure and animation objects
        """
        fig, ax = plt.subplots(figsize=self.figsize)
        fig.suptitle(self.title, fontsize=16, fontweight='bold')
        
        if not self.steps:
            return fig, None
        
        # Get array length for bar width
        arr_len = len(self.steps[0]['array'])
        max_val = max(max(step['array']) for step in self.steps)
        
        bars = None
        comparisons_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, 
                                   verticalalignment='top', fontsize=10,
                                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        step_text = ax.text(0.02, 0.88, '', transform=ax.transAxes,
                           verticalalignment='top', fontsize=10,
                           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        def animate(frame):
            nonlocal bars
            
            ax.clear()
            step = self.steps[frame]
            arr = step['array']
            
            # Define colors for each bar
            colors = ['#3498db'] * len(arr)  # Blue for unsorted
            
            # Color sorted elements green
            for idx in step.get('sorted_indices', []):
                if idx < len(colors):
                    colors[idx] = '#2ecc71'  # Green for sorted
            
            # Color comparing elements red
            for idx in step.get('comparing', []):
                if idx < len(colors):
                    colors[idx] = '#e74c3c'  # Red for comparing
            
            # Create bars
            bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', linewidth=0.5)
            
            # Set up axes
            ax.set_ylim(0, max_val * 1.1)
            ax.set_xlim(-0.5, len(arr) - 0.5)
            ax.set_ylabel('Value', fontsize=12, fontweight='bold')
            ax.set_xlabel('Index', fontsize=12, fontweight='bold')
            ax.set_title(self.title, fontsize=14, fontweight='bold')
            ax.set_xticks(range(len(arr)))
            
            # Update info text
            action = step.get('action', 'processing')
            comparisons_text.set_text(f"Step: {frame} | Action: {action}")
            step_text.set_text(f"Total steps: {len(self.steps)}")
            
            fig.canvas.draw_idle()
            return list(bars) + [comparisons_text, step_text]
        
        ani = animation.FuncAnimation(fig, animate, frames=len(self.steps),
                                     interval=interval, blit=False, repeat=True)
        
        if save_path:
            try:
                ani.save(save_path, writer='pillow')
                print(f"Animation saved to {save_path}")
            except Exception as e:
                print(f"Could not save animation: {e}")
        
        return fig, ani
    
    def show_animation(self, interval=100):
        """Display the animated visualization"""
        fig, ani = self.create_animation(interval=interval)
        plt.show()
    
    def create_step_view(self, step_number=None, figsize=(10, 6)):
        """
        Create a static view of a specific sorting step
        
        Args:
            step_number: Which step to display (0-indexed). If None, shows final state
        
        Returns:
            fig, ax: Matplotlib figure and axes objects
        """
        if step_number is None:
            step_number = len(self.steps) - 1
        
        if step_number >= len(self.steps):
            step_number = len(self.steps) - 1
        
        step = self.steps[step_number]
        arr = step['array']
        max_val = max(max(s['array']) for s in self.steps)
        
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(f"{self.title} - Step {step_number}/{len(self.steps)-1}", 
                    fontsize=14, fontweight='bold')
        
        # Define colors
        colors = ['#3498db'] * len(arr)
        for idx in step.get('sorted_indices', []):
            if idx < len(colors):
                colors[idx] = '#2ecc71'
        for idx in step.get('comparing', []):
            if idx < len(colors):
                colors[idx] = '#e74c3c'
        
        # Create bars
        bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', linewidth=1)
        
        ax.set_ylim(0, max_val * 1.1)
        ax.set_xlim(-0.5, len(arr) - 0.5)
        ax.set_ylabel('Value', fontsize=12, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12, fontweight='bold')
        ax.set_xticks(range(len(arr)))
        
        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, arr)):
            ax.text(bar.get_x() + bar.get_width()/2, val + max_val*0.02,
                   str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        return fig, ax
    
    def display_step(self, step_number=None):
        """Display a static view of a sorting step"""
        fig, ax = self.create_step_view(step_number)
        plt.tight_layout()
        plt.show()
    
    def create_comparison_figure(self, figsize=(14, 6)):
        """
        Create a figure comparing initial and final states
        
        Returns:
            fig: Matplotlib figure object
        """
        if len(self.steps) < 2:
            print("Not enough steps for comparison")
            return None
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        fig.suptitle(self.title + " - Before & After", fontsize=14, fontweight='bold')
        
        # Initial state
        initial = self.steps[0]['array']
        max_val = max(max(s['array']) for s in self.steps)
        ax1.bar(range(len(initial)), initial, color='#3498db', edgecolor='black', linewidth=1)
        ax1.set_title('Initial Array', fontsize=12, fontweight='bold')
        ax1.set_ylim(0, max_val * 1.1)
        ax1.set_ylabel('Value', fontsize=11)
        ax1.set_xlabel('Index', fontsize=11)
        
        # Final state
        final = self.steps[-1]['array']
        ax2.bar(range(len(final)), final, color='#2ecc71', edgecolor='black', linewidth=1)
        ax2.set_title('Sorted Array', fontsize=12, fontweight='bold')
        ax2.set_ylim(0, max_val * 1.1)
        ax2.set_ylabel('Value', fontsize=11)
        ax2.set_xlabel('Index', fontsize=11)
        
        plt.tight_layout()
        return fig
    
    def get_step_info(self, step_number):
        """Get information about a specific step"""
        if step_number >= len(self.steps):
            return None
        return self.steps[step_number]
    
    def total_steps(self):
        """Get total number of steps"""
        return len(self.steps)
