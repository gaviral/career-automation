#!/usr/bin/env python3
"""
Tree visualization for Tech Interview Prep structure.
Follows Dear PyGui best practices: separation of concerns, modular structure, clean code.
"""
import dearpygui.dearpygui as dpg
import json
import sys
import time
from pathlib import Path

# ============================================================================
# MODEL: Data and business logic
# ============================================================================

class TreeModel:
    """Handles data loading and tree structure operations."""
    
    @staticmethod
    def load_from_json(filepath):
        """Load tree structure from JSON file."""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def calculate_positions(node, level=0, x=0, y=0, spacing_x=150, spacing_y=100):
        """
        Recursively calculate positions for all nodes using tree layout algorithm.
        Returns the node with added position metadata.
        """
        node['level'] = level
        node['x'] = x
        node['y'] = y
        
        if 'children' in node and node['children']:
            num_children = len(node['children'])
            total_width = num_children * spacing_x
            start_x = x - total_width / 2
            
            for i, child in enumerate(node['children']):
                child_x = start_x + i * spacing_x + spacing_x / 2
                child_y = y + spacing_y
                TreeModel.calculate_positions(
                    child, 
                    level + 1, 
                    child_x, 
                    child_y, 
                    spacing_x * 0.8,  # Reduce spacing for deeper levels
                    spacing_y
                )
        
        return node


# ============================================================================
# VIEW: UI configuration and rendering
# ============================================================================

class TreeTheme:
    """Centralized theme configuration."""
    
    # Color palette for different levels
    COLORS = {
        0: (74, 144, 226),    # Level 0: Blue
        1: (126, 211, 33),    # Level 1: Green
        2: (245, 166, 35),    # Level 2: Orange
        3: (189, 16, 224),    # Level 3+: Purple
    }
    
    CONNECTION_COLOR = (255, 255, 255, 150)
    CONNECTION_THICKNESS = 1
    
    # Node sizing
    NODE_MIN_WIDTH = 100
    NODE_HEIGHT = 35
    NODE_PADDING = 5
    
    # Text
    TEXT_SIZE = 10
    TEXT_CHAR_WIDTH = 8  # Approximate character width
    
    # Window dimensions
    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 900
    
    @classmethod
    def get_color_for_level(cls, level):
        """Get color for a given tree level."""
        return cls.COLORS.get(level, cls.COLORS[3])


class TreeView:
    """Handles rendering of tree structure."""
    
    def __init__(self, canvas_tag):
        self.canvas = canvas_tag
    
    def draw_node(self, node, parent_pos=None):
        """Draw a single node and its connection to parent."""
        level = node['level']
        color = TreeTheme.get_color_for_level(level)
        
        x, y = node['x'], node['y']
        width = max(
            TreeTheme.NODE_MIN_WIDTH,
            len(node['name']) * TreeTheme.TEXT_CHAR_WIDTH
        )
        height = TreeTheme.NODE_HEIGHT
        
        # Draw connection line from parent
        if parent_pos:
            dpg.draw_line(
                parent_pos,
                (x, y),
                color=TreeTheme.CONNECTION_COLOR,
                thickness=TreeTheme.CONNECTION_THICKNESS,
                parent=self.canvas
            )
        
        # Draw node rectangle
        dpg.draw_rectangle(
            (x - width/2, y - height/2),
            (x + width/2, y + height/2),
            color=color,
            fill=color,
            parent=self.canvas
        )
        
        # Draw node text
        text_x = x - width/2 + TreeTheme.NODE_PADDING
        text_y = y - TreeTheme.TEXT_SIZE/2
        dpg.draw_text(
            (text_x, text_y),
            node['name'],
            size=TreeTheme.TEXT_SIZE,
            parent=self.canvas
        )
    
    def draw_tree(self, node, parent_pos=None):
        """Recursively draw entire tree structure."""
        self.draw_node(node, parent_pos)
        
        # Calculate child connection point
        child_parent_pos = (node['x'], node['y'] + TreeTheme.NODE_HEIGHT/2)
        
        # Draw children
        if 'children' in node and node['children']:
            for child in node['children']:
                self.draw_tree(child, child_parent_pos)


# ============================================================================
# CONTROLLER: Application logic
# ============================================================================

class TreeApp:
    """Main application controller."""
    
    def __init__(self, data_file, runtime_seconds=10):
        self.data_file = data_file
        self.runtime_seconds = runtime_seconds
        self.tree_data = None
    
    def initialize(self):
        """Initialize application context and load data."""
        dpg.create_context()
        self.tree_data = TreeModel.load_from_json(self.data_file)
        TreeModel.calculate_positions(
            self.tree_data,
            x=TreeTheme.WINDOW_WIDTH / 2,
            y=50,
            spacing_x=200,
            spacing_y=120
        )
    
    def setup_ui(self):
        """Create and configure UI elements."""
        with dpg.window(
            label="Tech Interview Prep Tree",
            width=TreeTheme.WINDOW_WIDTH,
            height=TreeTheme.WINDOW_HEIGHT
        ):
            with dpg.drawlist(
                width=TreeTheme.WINDOW_WIDTH - 20,
                height=TreeTheme.WINDOW_HEIGHT - 20
            ) as canvas:
                view = TreeView(canvas)
                view.draw_tree(self.tree_data)
    
    def run(self):
        """Start the application main loop."""
        dpg.create_viewport(
            title='Tech Interview Prep Visualization',
            width=TreeTheme.WINDOW_WIDTH,
            height=TreeTheme.WINDOW_HEIGHT
        )
        dpg.setup_dearpygui()
        dpg.show_viewport()
        
        start_time = time.time()
        while dpg.is_dearpygui_running() and (time.time() - start_time) < self.runtime_seconds:
            dpg.render_dearpygui_frame()
        
        dpg.destroy_context()


# ============================================================================
# ENTRY POINT
# ============================================================================

def main():
    """Application entry point."""
    # Parse command-line arguments
    runtime = int(sys.argv[1]) if len(sys.argv) == 2 else 10
    data_file = Path(__file__).parent / 'tree_data.json'
    
    # Create and run application
    app = TreeApp(data_file, runtime)
    app.initialize()
    app.setup_ui()
    app.run()


if __name__ == "__main__":
    main()
