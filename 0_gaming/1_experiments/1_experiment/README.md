# Tech Interview Prep Tree Visualization

A dynamic, scrollable tree visualization tool for organizing and displaying technical interview preparation content using DearPyGUI.

## Features

- **Dynamic Node Sizing**: Nodes automatically resize based on text content
- **Scrollable Canvas**: Full horizontal and vertical scrolling support for large trees
- **JSON-Driven**: Tree structure defined in `tree_data.json` for easy modification
- **Screenshot Capability**: Automatic screenshot capture during runtime
- **Clean Architecture**: Follows MVC pattern with separation of concerns

## Requirements

- Python 3.12+
- DearPyGUI 2.1.0+
- Pillow (for screenshots)
- PyAutoGUI (for screenshots)

## Installation

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -r requirements.txt
```

## Usage

```bash
# Run with default 10 seconds
python tree_viz.py

# Run with custom duration (in seconds)
python tree_viz.py 5
```

## Project Structure

```
tree_viz.py           # Main visualization application
tree_data.json        # Tree structure definition
tree_data_backup.json # Backup of tree structure
requirements.txt      # Python dependencies
README.md            # This file
```

## Architecture

### Model (TreeModel)
- `load_from_json()`: Loads tree structure from JSON
- `calculate_node_width()`: Dynamic node sizing based on text
- `calculate_subtree_width()`: Calculates space needed for subtrees
- `calculate_positions()`: Layout algorithm for positioning nodes

### View (TreeView + TreeTheme)
- `TreeTheme`: Centralized styling and configuration
- `TreeView.draw_node()`: Renders individual nodes
- `TreeView.draw_tree()`: Recursive tree rendering

### Controller (TreeApp)
- `initialize()`: Sets up context and loads data
- `setup_ui()`: Creates UI with scrolling support
- `run()`: Main application loop

## Modifying the Tree

Edit `tree_data.json` to add/remove nodes. Structure:

```json
{
  "name": "Node Name",
  "children": [
    {"name": "Child 1"},
    {
      "name": "Child 2",
      "children": [...]
    }
  ]
}
```

## Features for Future Enhancement

- [ ] Interactive node expansion/collapse
- [ ] Zoom in/out functionality
- [ ] Search and filter
- [ ] Editable node text
- [ ] Export to various formats (PNG, PDF, SVG)
- [ ] Themes and color schemes
- [ ] Keyboard navigation

## Design Principles

1. **Separation of Concerns**: MVC-like architecture
2. **Dynamic Calculations**: No hardcoded sizes or positions
3. **Extensibility**: Easy to add new features
4. **Maintainability**: Clear, documented code
5. **Performance**: Efficient rendering and layout algorithms

## Notes

- The tree automatically calculates optimal spacing to prevent overlap
- Nodes are color-coded by level (Blue→Green→Orange→Purple)
- Screenshots are saved to `tree_viz_screenshot.png`
- Canvas size is set to 4000x2000 to accommodate large trees

