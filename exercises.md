# NanoDash Tutorial Exercises

The 6 exercises to be completed for this tutorial are located in the directories `exercise1/` through `exercise6/`.

Each exercise folder contains the following:

- A partial copy of the NanoDash codebase (under `exerciseN/nanodash/`), containing one or more spots for you to "fill-in-the-blanks" by implementing part of the NanoDash logic

- A sample app (`exerciseN/app.py`) which will run correctly once the exercise has been completed

- A tests file (`test_exerciseN.py`) which will pass once the exercise has been completed.
  - To run the tests for exercise N from the repository root: `python -m pytest exerciseN/`
  - To run the tests for exercise N from within the exercise directory: `python -m pytest`

## Exercise outline

Each exercise focuses on implementing a specific part of the NanoDash framework.

### Exercise 1: Making a basic Flask server which serves a static HTML page

**Goal**: Set up a simple Flask server that serves one static HTML page.

**Tasks**:
- Implement the `full_html()` function of the `NanoDash` class in `exercise1/nanodash/nanodash.py` to return a valid HTML webpage.
- Define a Flask route inside the `NanoDash.__init__()` function which returns the value of `full_html()` for the route `/`.

**Files to modify**
- `exercise1/nanodash/nanodash.py`

**Command to run tests**
`python -m pytest exercise1/`

### Exercise 2: Implement UI components

**Goal**: Implement basic UI component objects to use as building blocks for page layouts.

**Tasks**:
- Review the implementations of the `Page`, `Header` and `Text` classes in `exercise2/nanodash/components.py`
- Implement the `__init__()` and `html()` methods of the `TextField` class
- Implement the `__init__()` and `html()` methods of the `Dropdown` class

**Files to modify**:
- `exercise2/nanodash/components.py`

**Command to run tests**
`python -m pytest exercise2/`

### Exercise 3: Implement Graph component 

**Goal**: Implement the Graph component, which uses Plotly.js to display Plotly figures in the browser

**Tasks**:
- Implement the the `__init__()` and `html()` methods of the `Graph` class in `exercise3/nanodash/components.py`

**Files to modify**:
- `exercise3/nanodash/components.py`

**Command to run tests**
`python -m pytest exercise3/`

### Exercise 4: Browser to Server Communication — Gathering the page state

**Goal**: Implement the Javascript logic to capture the state of all components on the page, and bundle it into a JSON request to send to the Flask server.

Don't worry — we've provided some useful helper functions inside the Javascript file; all you need to do is put them together in the right way.

**Tasks**:
- Implement the `getState()` function in `exercise4/nanodash/static/index.js`.

**Files to modify**:
- `exercise4/static/index.js`

**Command to run tests**
`python -m pytest exercise4/`

### Exercise 5: Running callbacks

**Goal**: Implement the Python logic which receives the page state from the frontend, runs the necessary callbacks, and sends the results back to the frontend. Also implement the logic which allows a user to add a callback to their app.

**Tasks**:
- Implement the `handle_change()` function in `exercise5/nanodash/nanodash.py`
- Implement the `add_callback()` function in `exercise5/nanodash/nanodash.py`

**Files to modify**:
- `exercise5/nanodash/nanodash.py`

**Command to run tests**
`python -m pytest exercise5/`

### Exercise 6: Updating the page with callback results

**Goal**: Implement the Javascript logic to update the page's UI components based on the callback results received from the server.

**Tasks**:
- Implement the `updateValues()` function in `exercise6/nanodash/static/index.js`

**Files to modify**:
- `exercise6/nanodash/static/index.js`

**Command to run tests**
`python -m pytest exercise6/`

### Exercise 7: Write your own NanoDash Application

**Goal**: Use the NanoDash framework to write your own interactive dashboard. You can modify the framework or add new components if you like.

**Tasks**:
- Pick a dataset
- Modify `exercise7/app.py` to define an app layout, add graphs and interactive components, and add at least one callback

**Files to modify**:
- `exercise7/app.py`

There are no tests for this exercise since your app can do whatever you like!

## Resources

- Plotly.js documentation: https://plotly.com/javascript/
- Plotly.py documentation: https://plotly.com/python/
- Flask documentation: https://flask.palletsprojects.com/
- Pittsburgh data: https://data.wprdc.org/