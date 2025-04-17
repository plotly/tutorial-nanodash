# NanoDash Tutorial Exercises

This repository contains sample apps for each exercise in the NanoDash tutorial. NanoDash is a minimalist dashboard framework for data visualization inspired by Dash.

## Exercise Structure

Each exercise builds on the knowledge from previous exercises and focuses on specific aspects of the NanoDash framework:

## Exercise 1: Basic Flask Server with Static HTML

**Goal**: Set up a simple Flask server that serves static HTML content.

**Tasks**:
- Implement the NanoDash class with basic Flask server functionality
- Create a route for the main page
- Implement the full_html method to generate HTML with proper structure
- Include necessary script tags (Plotly.js, index.js)

**Files to modify**:
- `exercise1/app.py`

**Location**: `/exercise1/`
**Key concepts**: Basic HTML structure, script inclusion

## Exercise 2: Component Implementation

**Goal**: Implement basic UI components.

**Tasks**:
- Implement the TextField component
- Implement the Dropdown component
- Create a page layout using the components

**Files to modify**:
- `exercise2/app.py`

**Location**: `/exercise2/`
**Key components**: `TextField`, `Dropdown`, `Page`

## Exercise 3: Graph Component and Plotly Integration

**Goal**: Create and implement the Graph component with Plotly.js integration.

**Tasks**:
- Implement the Graph component
- Create a Plotly figure and display it using the Graph component
- Ensure proper rendering of SVG elements and axes

**Files to modify**:
- `exercise3/app.py`

**Location**: `/exercise3/`
**Key components**: `Graph` component

## Exercise 4: Frontend to Python Communication

**Goal**: Implement state tracking and sending component state to the server.

**Tasks**:
- Implement the state endpoint in Flask
- Create functions to collect form element states
- Send state changes to the server via POST requests

**Files to modify**:
- `exercise4/app.py`
- `exercise4/static/index.js`

**Location**: `/exercise4/`
**Key concepts**: State tracking, POST requests, JSON handling

## Exercise 5: Python to Frontend Communication

**Goal**: Implement callback registration and execution.

**Tasks**:
- Implement the add_callback method to register callbacks
- Update the state endpoint to execute registered callbacks
- Send callback results back to the client

**Files to modify**:
- `exercise5/app.py`
- `exercise5/static/index.js`

**Location**: `/exercise5/`
**Key concepts**: Callback functions, input/output mapping

## Exercise 6: UI Updates from Callbacks

**Goal**: Update UI components based on callback responses.

**Tasks**:
- Implement the updateValues function to update UI elements
- Handle different types of updates (text, boolean, graph)
- Process multiple outputs from a single callback

**Files to modify**:
- `exercise6/app.py`
- `exercise6/static/index.js`

**Location**: `/exercise6/`
**Key concepts**: DOM manipulation, dynamic updates

## Exercise 5: Complete NanoDash Application

**Goal**: Build a complete data dashboard application using all previous components.

**Tasks**:
- Create a Pittsburgh data explorer dashboard
- Implement filtering and data visualization
- Use callbacks to update multiple components based on user interaction

**Files to modify**:
- `exercise5/app.py`
- `exercise5/static/index.js`

**Location**: `/exercise5/`
**Key features**: Pittsburgh city data exploration, filtering, data visualization

## Running the Exercises

To run any exercise, navigate to its directory and run the `app.py` file:

```bash
cd exercise1
python app.py
```

Then open a web browser and go to: http://127.0.0.1:5000

## Project Structure

Each exercise directory contains:

- `app.py`: The main application file
- `static/`: Directory for static files (like JavaScript)
  - `index.js`: Client-side JavaScript for the exercise

## Exercise Templates

If you want to start with a skeleton template instead of the completed examples, check out the templates in the `tests/exercise_templates/` directory:

- `nanodash_skeleton.py`: Basic framework skeleton
- `components_skeleton.py`: Components implementation skeleton
- `index_js_skeleton.js`: Frontend JavaScript skeleton
- `sample_app_skeleton.py`: Complete app skeleton

## Submission

Submit your completed exercises by following these steps:

1. Complete the implementation for each exercise
2. Ensure all tests pass for each exercise
3. Submit your code to the course repository

## Requirements

- Python 3.6+
- Flask
- Plotly
- Pandas (for Exercise 5)

## Resources

- Plotly.js documentation: https://plotly.com/javascript/
- Flask documentation: https://flask.palletsprojects.com/
- Pittsburgh data: https://data.wprdc.org/