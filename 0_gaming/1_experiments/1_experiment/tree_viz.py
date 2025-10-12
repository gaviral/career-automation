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

try:
    import pyautogui
    SCREENSHOT_AVAILABLE = True
except ImportError:
    SCREENSHOT_AVAILABLE = False

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
    def initialize_collapsed_state(node, collapsed=False):
        """
        Initialize collapsed state for all nodes.
        Nodes with children start expanded by default.
        """
        node['collapsed'] = collapsed
        node['has_children'] = 'children' in node and len(node.get('children', [])) > 0
        
        if node['has_children']:
            for child in node['children']:
                TreeModel.initialize_collapsed_state(child, collapsed=False)
    
    @staticmethod
    def calculate_node_width(node):
        """
        Calculate actual width needed for a single node including indicators.
        Stores the width in the node for later use.
        Uses DearPyGUI's text size measurement for accuracy.
        """
        # Prepare the full text that will be displayed (including indicators)
        node_text = node['name']
        if node.get('has_children', False):
            # Account for the indicator that will be added in draw_node
            indicator = "⊕" if node.get('collapsed', False) else "⊖"
            node_text = f"{indicator} {node_text}"

        try:
            # Try to get actual text size from DearPyGUI (requires context)
            text_width, text_height = dpg.get_text_size(node_text, size=TreeTheme.TEXT_SIZE)
        except (SystemError, RuntimeError):
            # Fallback: estimate text size when DearPyGUI context not ready
            # Count different character types for accurate width estimation
            letters = sum(1 for c in node_text if c.isalpha())
            numbers = sum(1 for c in node_text if c.isdigit())
            spaces = sum(1 for c in node_text if c.isspace())
            symbols = len(node_text) - letters - numbers - spaces

            # Calculate total width based on character type weights
            total_width = (letters * 9) + (numbers * 8) + (spaces * 6) + (symbols * 12)

            # Account for indicator if present
            if node.get('has_children', False):
                total_width += 20  # Extra space for ⊕ or ⊖

            text_width = total_width
            text_height = 20  # Estimated height for TEXT_SIZE=15

        # Calculate node dimensions with proper padding
        width = max(TreeTheme.NODE_MIN_WIDTH, text_width + 2 * TreeTheme.NODE_PADDING_X)
        height = max(TreeTheme.NODE_HEIGHT, text_height + 2 * TreeTheme.NODE_PADDING_Y)

        node['width'] = width
        node['height'] = height
        return width
    
    @staticmethod
    def calculate_subtree_width(node, min_gap=20):
        """
        Calculate the width needed for a node's entire subtree dynamically.
        Uses actual measured node widths.
        """
        # Calculate this node's width
        node_width = TreeModel.calculate_node_width(node)
        
        if 'children' not in node or not node['children']:
            # Leaf node: just its own width plus gap
            return node_width + min_gap
        
        # Sum the widths of all children's subtrees
        children_width = sum(
            TreeModel.calculate_subtree_width(child, min_gap)
            for child in node['children']
        )
        
        # Return the maximum of node width and children width
        return max(node_width + min_gap, children_width)
    
    @staticmethod
    def calculate_positions(node, level=0, x=0, y=0, vertical_spacing=120):
        """
        Dynamic tree layout algorithm that prevents overlap.
        Uses actual measured node sizes for positioning.
        """
        node['level'] = level
        node['x'] = x
        node['y'] = y
        
        if 'children' in node and node['children']:
            # Calculate width needed for each child's subtree
            child_widths = [
                TreeModel.calculate_subtree_width(child)
                for child in node['children']
            ]
            total_width = sum(child_widths)
            
            # Position children left to right based on their subtree widths
            current_x = x - total_width / 2
            for i, child in enumerate(node['children']):
                child_x = current_x + child_widths[i] / 2
                child_y = y + vertical_spacing
                TreeModel.calculate_positions(
                    child,
                    level + 1,
                    child_x,
                    child_y,
                    vertical_spacing
                )
                current_x += child_widths[i]
        
        return node
    
    @staticmethod
    def get_tree_bounds(node):
        """
        Calculate the actual bounding box of the tree.
        Returns (min_x, min_y, max_x, max_y).
        """
        min_x = node['x'] - node.get('width', 100) / 2
        max_x = node['x'] + node.get('width', 100) / 2
        min_y = node['y'] - node.get('height', 35) / 2
        max_y = node['y'] + node.get('height', 35) / 2
        
        # Skip collapsed children
        if not node.get('collapsed', False) and 'children' in node and node['children']:
            for child in node['children']:
                child_bounds = TreeModel.get_tree_bounds(child)
                min_x = min(min_x, child_bounds[0])
                min_y = min(min_y, child_bounds[1])
                max_x = max(max_x, child_bounds[2])
                max_y = max(max_y, child_bounds[3])
        
        return (min_x, min_y, max_x, max_y)


# ============================================================================
# VIEW: UI configuration and rendering
# ============================================================================

class TreeTheme:
    """Apple-inspired minimal theme configuration."""

    # Apple-inspired color palette - subtle, professional
    COLORS = {
        0: (52, 152, 219, 220),    # Level 0: Soft blue with transparency
        1: (46, 204, 113, 220),    # Level 1: Soft green with transparency
        2: (241, 196, 15, 220),    # Level 2: Soft yellow with transparency
        3: (155, 89, 182, 220),    # Level 3+: Soft purple with transparency
    }

    # Refined connection styling
    CONNECTION_COLOR = (120, 120, 120, 100)  # Subtle gray
    CONNECTION_THICKNESS = 2

    # Enhanced node styling
    NODE_MIN_WIDTH = 120
    NODE_HEIGHT = 50
    NODE_PADDING_X = 16  # More generous padding
    NODE_PADDING_Y = 14  # More generous padding

    # Apple-style border radius
    NODE_CORNER_RADIUS = 8

    # Typography - clean and readable
    TEXT_SIZE = 15

    # Refined spacing
    MIN_HORIZONTAL_GAP = 30  # More breathing room
    LEVEL_VERTICAL_SPACING = 140  # Increased vertical spacing

    # Shadow for depth
    NODE_SHADOW_COLOR = (0, 0, 0, 30)
    NODE_SHADOW_OFFSET = 2

    # Canvas and layout
    CANVAS_PADDING = 150  # Padding around tree content
    WINDOW_WIDTH = 1900
    WINDOW_HEIGHT = 1100
    
    # Zoom settings
    ZOOM_MIN = 0.3  # Minimum zoom level (30%)
    ZOOM_MAX = 3.0  # Maximum zoom level (300%)
    ZOOM_STEP = 0.1  # Zoom increment per scroll
    
    @classmethod
    def get_color_for_level(cls, level):
        """Get color for a given tree level."""
        return cls.COLORS.get(level, cls.COLORS[3])


class TreeView:
    """Handles rendering of tree structure with interactive features."""

    def __init__(self, canvas_tag, tree_root):
        self.canvas = canvas_tag
        self.tree_root = tree_root
        self.node_rectangles = {}  # Store node bounds for click detection
        self.hovered_node = None  # Track currently hovered node
        self.zoom_level = 1.0  # Current zoom level (1.0 = 100%)
    
    def draw_node(self, node, parent_pos=None):
        """Draw a single node with Apple-style rounded corners and shadows."""
        level = node['level']
        color = TreeTheme.get_color_for_level(level)

        # Apply zoom transformation to coordinates and dimensions
        x = node['x'] * self.zoom_level
        y = node['y'] * self.zoom_level
        width = node.get('width', TreeTheme.NODE_MIN_WIDTH) * self.zoom_level
        height = node.get('height', TreeTheme.NODE_HEIGHT) * self.zoom_level

        # Check if this node is being hovered
        node_id = id(node)
        is_hovered = (self.hovered_node == node_id)

        # Store node bounds for click detection
        self.node_rectangles[node_id] = {
            'node': node,
            'bounds': (x - width/2, y - height/2, x + width/2, y + height/2)
        }

        # Draw subtle shadow first
        shadow_offset = TreeTheme.NODE_SHADOW_OFFSET * self.zoom_level
        corner_radius = TreeTheme.NODE_CORNER_RADIUS * self.zoom_level
        dpg.draw_rectangle(
            (x - width/2 + shadow_offset, y - height/2 + shadow_offset),
            (x + width/2 + shadow_offset, y + height/2 + shadow_offset),
            color=TreeTheme.NODE_SHADOW_COLOR,
            fill=TreeTheme.NODE_SHADOW_COLOR,
            rounding=corner_radius,
            parent=self.canvas
        )

        # Draw connection line from parent
        if parent_pos:
            dpg.draw_line(
                parent_pos,
                (x, y),
                color=TreeTheme.CONNECTION_COLOR,
                thickness=TreeTheme.CONNECTION_THICKNESS * self.zoom_level,
                parent=self.canvas
            )

        # Enhanced hover effect - brighter color and glow
        if is_hovered:
            # Brighten the color for hover effect
            hover_color = (
                min(255, color[0] + 30),
                min(255, color[1] + 30),
                min(255, color[2] + 30),
                color[3]
            )
            # Draw glow effect
            glow_offset = 2 * self.zoom_level
            dpg.draw_rectangle(
                (x - width/2 - glow_offset, y - height/2 - glow_offset),
                (x + width/2 + glow_offset, y + height/2 + glow_offset),
                color=(255, 255, 255, 50),
                fill=(255, 255, 255, 50),
                rounding=corner_radius + glow_offset,
                parent=self.canvas
            )
        else:
            hover_color = color

        # Draw main node rectangle with rounded corners
        dpg.draw_rectangle(
            (x - width/2, y - height/2),
            (x + width/2, y + height/2),
            color=hover_color,
            fill=hover_color,
            rounding=corner_radius,
            parent=self.canvas
        )

        # Draw node text with better typography
        padding_x = TreeTheme.NODE_PADDING_X * self.zoom_level
        padding_y = TreeTheme.NODE_PADDING_Y * self.zoom_level
        text_x = x - width/2 + padding_x
        text_y = y - height/2 + padding_y
        node_text = node['name']

        # Add collapse/expand indicator with refined styling
        if node.get('has_children', False):
            indicator = "⊕" if node.get('collapsed', False) else "⊖"
            node_text = f"{indicator} {node_text}"

        # Draw text with subtle shadow for better readability
        text_color = (255, 255, 255)  # White text for better contrast
        text_size = TreeTheme.TEXT_SIZE * self.zoom_level
        text_shadow_offset = 1 * self.zoom_level

        dpg.draw_text(
            (text_x + text_shadow_offset, text_y + text_shadow_offset),
            node_text,
            color=(0, 0, 0, 80),  # Subtle shadow
            size=text_size,
            parent=self.canvas
        )

        dpg.draw_text(
            (text_x, text_y),
            node_text,
            color=text_color,
            size=text_size,
            parent=self.canvas
        )
    
    def draw_tree(self, node, parent_pos=None):
        """Recursively draw tree structure, skipping collapsed subtrees."""
        self.draw_node(node, parent_pos)
        
        # Skip drawing children if node is collapsed
        if node.get('collapsed', False):
            return
        
        # Calculate child connection point (apply zoom)
        child_parent_pos = (
            node['x'] * self.zoom_level,
            (node['y'] + TreeTheme.NODE_HEIGHT/2) * self.zoom_level
        )
        
        # Draw children
        if 'children' in node and node['children']:
            for child in node['children']:
                self.draw_tree(child, child_parent_pos)
    
    def handle_click(self, canvas_x, canvas_y):
        """
        Handle mouse click to toggle node collapse/expand.
        
        Args:
            canvas_x: Mouse X coordinate in canvas space (scroll-adjusted)
            canvas_y: Mouse Y coordinate in canvas space (scroll-adjusted)
            
        Returns:
            bool: True if a node was clicked and state changed
        """
        for node_id, data in self.node_rectangles.items():
            x1, y1, x2, y2 = data['bounds']
            if x1 <= canvas_x <= x2 and y1 <= canvas_y <= y2:
                node = data['node']
                if node.get('has_children', False):
                    # Toggle collapsed state
                    node['collapsed'] = not node.get('collapsed', False)
                    return True
        return False

    def handle_hover(self, canvas_x, canvas_y):
        """
        Handle mouse hover to update visual feedback.
        
        Args:
            canvas_x: Mouse X coordinate in canvas space (scroll-adjusted)
            canvas_y: Mouse Y coordinate in canvas space (scroll-adjusted)
            
        Returns:
            bool: True if hover state changed (requires redraw)
        """
        hovered_node_id = None

        # Find which node (if any) is being hovered
        for node_id, data in self.node_rectangles.items():
            x1, y1, x2, y2 = data['bounds']
            if x1 <= canvas_x <= x2 and y1 <= canvas_y <= y2:
                hovered_node_id = node_id
                break

        # Update hover state and return True if changed
        if self.hovered_node != hovered_node_id:
            self.hovered_node = hovered_node_id
            return True

        return False

    def set_zoom(self, new_zoom):
        """
        Set zoom level within allowed bounds.
        
        Args:
            new_zoom: Desired zoom level
            
        Returns:
            bool: True if zoom changed (requires redraw)
        """
        # Clamp zoom level to bounds
        clamped_zoom = max(TreeTheme.ZOOM_MIN, min(TreeTheme.ZOOM_MAX, new_zoom))
        
        if clamped_zoom != self.zoom_level:
            self.zoom_level = clamped_zoom
            return True
        return False


# ============================================================================
# CONTROLLER: Application logic
# ============================================================================

class TreeApp:
    """Main application controller."""
    
    def __init__(self, data_file, runtime_seconds=None):
        self.data_file = data_file
        self.runtime_seconds = runtime_seconds  # None means indefinite
        self.tree_data = None
        self.tree_view = None
        self.canvas_width = 4000
        self.canvas_height = 2000
    
    def initialize(self):
        """Initialize application context and load data."""
        dpg.create_context()
        self.tree_data = TreeModel.load_from_json(self.data_file)
        # Initialize collapsed state
        TreeModel.initialize_collapsed_state(self.tree_data)
        # Initial layout calculation with fallback sizes
        # (will be recalculated after UI setup for accurate measurements)
        TreeModel.calculate_positions(
            self.tree_data,
            x=TreeTheme.WINDOW_WIDTH / 2,
            y=50
        )
        # Calculate required canvas size
        self._update_canvas_size()
    
    def setup_ui(self):
        """Create and configure UI elements with scrolling and mouse support."""
        with dpg.window(
            label="Interview Prep Navigator",
            width=TreeTheme.WINDOW_WIDTH,
            height=TreeTheme.WINDOW_HEIGHT,
            no_scrollbar=False,
            tag="main_window"
        ):
            # Add zoom indicator text at the top
            dpg.add_text("Zoom: 100% (Use mouse wheel to zoom)", tag="zoom_indicator")
            # Use a child window with scrolling enabled
            with dpg.child_window(
                width=-1,
                height=-1,
                horizontal_scrollbar=True,
                no_scrollbar=False,
                tag="scroll_window"
            ):
                with dpg.drawlist(
                    width=int(self.canvas_width),
                    height=int(self.canvas_height)
                ) as canvas:
                    self.tree_view = TreeView(canvas, self.tree_data)

                    # Recalculate layout with accurate text measurements now that DearPyGUI is ready
                    self._recalculate_layout()

                    self.tree_view.draw_tree(self.tree_data)

                    # Add global mouse handlers for drawlist interaction
                    # Note: drawlist primitives (draw_rectangle, draw_text) don't support
                    # item-specific handlers in DearPyGUI. Global handlers with manual
                    # hit-testing is the correct and idiomatic approach for drawlist-based UIs.
                    with dpg.handler_registry():
                        dpg.add_mouse_click_handler(
                            callback=self.on_mouse_click
                        )
                        dpg.add_mouse_move_handler(
                            callback=self.on_mouse_move
                        )
                        dpg.add_mouse_wheel_handler(
                            callback=self.on_mouse_wheel
                        )
    
    def _update_canvas_size(self):
        """Calculate and update canvas size based on actual tree bounds and zoom level."""
        bounds = TreeModel.get_tree_bounds(self.tree_data)
        min_x, min_y, max_x, max_y = bounds

        # Apply zoom to bounds
        zoom = self.tree_view.zoom_level if self.tree_view else 1.0
        min_x *= zoom
        min_y *= zoom
        max_x *= zoom
        max_y *= zoom

        # Calculate canvas size accounting for negative coordinates
        # If min_x is negative, we need extra space on the left
        padding = TreeTheme.CANVAS_PADDING
        left_space = abs(min(0, min_x)) + padding
        right_space = max_x + padding
        top_space = abs(min(0, min_y)) + padding
        bottom_space = max_y + padding

        self.canvas_width = max(left_space + right_space, 2000)  # Minimum 2000px
        self.canvas_height = max(top_space + bottom_space, 1500)  # Minimum 1500px
    
    def on_mouse_click(self):
        """
        Handle mouse click events to toggle node collapse/expand.
        
        Uses manual hit-testing with scroll-aware coordinate transformation.
        This is the idiomatic approach for DearPyGUI drawlist-based UIs, as
        drawlist primitives don't support item-specific click handlers.
        """
        mouse_pos = dpg.get_mouse_pos()
        
        # Transform viewport coordinates to canvas coordinates
        # by accounting for scroll offset
        scroll_x = dpg.get_x_scroll("scroll_window") if dpg.does_item_exist("scroll_window") else 0
        scroll_y = dpg.get_y_scroll("scroll_window") if dpg.does_item_exist("scroll_window") else 0
        
        canvas_x = mouse_pos[0] + scroll_x
        canvas_y = mouse_pos[1] + scroll_y
        
        if self.tree_view and self.tree_view.handle_click(canvas_x, canvas_y):
            self.refresh_tree()

    def on_mouse_move(self):
        """
        Handle mouse move events for hover effects.
        
        Provides real-time visual feedback as user hovers over nodes.
        Uses the same scroll-aware coordinate transformation as click handling.
        """
        mouse_pos = dpg.get_mouse_pos()
        
        # Transform viewport coordinates to canvas coordinates
        scroll_x = dpg.get_x_scroll("scroll_window") if dpg.does_item_exist("scroll_window") else 0
        scroll_y = dpg.get_y_scroll("scroll_window") if dpg.does_item_exist("scroll_window") else 0
        
        canvas_x = mouse_pos[0] + scroll_x
        canvas_y = mouse_pos[1] + scroll_y
        
        if self.tree_view and self.tree_view.handle_hover(canvas_x, canvas_y):
            self.refresh_tree()

    def on_mouse_wheel(self, sender, app_data):
        """
        Handle mouse wheel events for zoom control.
        
        Args:
            sender: DearPyGUI sender
            app_data: Mouse wheel delta (positive = scroll up/zoom in, negative = scroll down/zoom out)
        """
        if not self.tree_view:
            return

        # Calculate new zoom level
        # Positive wheel delta = scroll up = zoom in
        zoom_delta = app_data * TreeTheme.ZOOM_STEP
        new_zoom = self.tree_view.zoom_level + zoom_delta

        # Apply zoom and refresh if changed
        if self.tree_view.set_zoom(new_zoom):
            self._update_zoom_indicator()
            self.refresh_tree()

    def _update_zoom_indicator(self):
        """Update the zoom indicator text to show current zoom level."""
        if self.tree_view and dpg.does_item_exist("zoom_indicator"):
            zoom_percent = int(self.tree_view.zoom_level * 100)
            dpg.set_value("zoom_indicator", f"Zoom: {zoom_percent}% (Use mouse wheel to zoom)")
    
    def refresh_tree(self):
        """Recalculate layout and redraw tree after state change."""
        # Recalculate positions with accurate measurements
        self._recalculate_layout()

        # Clear canvas and redraw
        if self.tree_view:
            dpg.delete_item(self.tree_view.canvas, children_only=True)
            self.tree_view.node_rectangles.clear()
            self.tree_view.hovered_node = None  # Clear hover state
            self.tree_view.draw_tree(self.tree_data)

    def _recalculate_layout(self):
        """Recalculate tree layout with accurate text measurements."""
        # Get tree bounds to determine starting position
        bounds = TreeModel.get_tree_bounds(self.tree_data)
        min_x, min_y, max_x, max_y = bounds

        # Calculate proper starting X position to avoid left overflow
        tree_total_width = max_x - min_x
        padding = TreeTheme.CANVAS_PADDING

        # If tree would overflow left, shift starting position right
        start_x = max(TreeTheme.WINDOW_WIDTH / 2, tree_total_width / 2 + padding)

        # Recalculate positions with proper text size measurements
        TreeModel.calculate_positions(
            self.tree_data,
            x=start_x,
            y=50
        )
        # Update canvas size for new layout
        self._update_canvas_size()
    
    def run(self):
        """Start the application main loop."""
        dpg.create_viewport(
            title='Interview Prep Navigator',
            width=TreeTheme.WINDOW_WIDTH,
            height=TreeTheme.WINDOW_HEIGHT
        )
        dpg.setup_dearpygui()
        dpg.show_viewport()
        
        start_time = time.time() if self.runtime_seconds is not None else None
        screenshot_taken = False

        while dpg.is_dearpygui_running():
            # If runtime_seconds is set, check time limit; otherwise run indefinitely
            if self.runtime_seconds is not None and (time.time() - start_time) >= self.runtime_seconds:
                break
            dpg.render_dearpygui_frame()
            
            # Try to take screenshot after 1.5 seconds
            current_time = time.time()
            if (SCREENSHOT_AVAILABLE and not screenshot_taken and
                start_time is not None and (current_time - start_time) > 1.5):
                try:
                    time.sleep(0.3)  # Brief pause for rendering
                    screenshot = pyautogui.screenshot()
                    screenshot_path = Path(__file__).parent / 'tree_viz_screenshot.png'
                    screenshot.save(screenshot_path)
                    print(f"Screenshot saved: {screenshot_path}")
                    screenshot_taken = True
                except Exception as e:
                    print(f"Screenshot failed: {e}")
                    screenshot_taken = True  # Don't retry
        
        dpg.destroy_context()


# ============================================================================
# ENTRY POINT
# ============================================================================

def main():
    """Application entry point."""
    # Parse command-line arguments
    runtime = int(sys.argv[1]) if len(sys.argv) == 2 else None  # None means indefinite
    data_file = Path(__file__).parent / 'tree_data.json'

    # Create and run application
    app = TreeApp(data_file, runtime)
    app.initialize()
    app.setup_ui()
    app.run()


if __name__ == "__main__":
    main()
