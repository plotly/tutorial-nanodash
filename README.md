# Welcome to the NanoDash tutorial!

This tutorial will demonstrate how interactive web dashboard frameworks like Plotly Dash work, by building a simplified version of Dash itself from scratch using Python, the Flask framework, and a little bit of vanilla JavaScript. 

[Link to Slides](https://docs.google.com/presentation/d/1rbJyN75oafr6xxv5Xs9jWwQkrMgv0drzuLckSWyhAJs/edit?usp=sharing)


## Setup

If you haven't already, please complete the setup instructions outlined in [SETUP.md](https://github.com/plotly/tutorial-nanodash/blob/main/SETUP.md) before continuing.

## Exercises

The 7 exercises to be completed for this tutorial are located in the directories `exercise1/` through `exercise7/`.

Each exercise folder contains the following:

- A partial copy of the NanoDash codebase (under `exerciseN/nanodash/`), containing one or more spots for you to "fill-in-the-blanks" by implementing part of the NanoDash logic

- A sample app (`exerciseN/app.py`) which will run correctly once the exercise has been completed
  - To run the app from the repository root: `python exerciseN/app.py`

- A tests file (`test_exerciseN.py`) which will pass once the exercise has been completed.
  - To run the tests for exercise N from the repository root: `python -m pytest exerciseN/`

## A note on running Pytest
We recommend using the command `python -m pytest` rather than just `pytest`, because it ensures using the Python in your virtual environment rather than the system Python. 

## Exercise outline

Each exercise focuses on implementing a specific part of the NanoDash framework.

### Exercise 1: Making a basic Flask server which serves a static HTML page
---

**Goal**: Set up a simple Flask server that serves one static HTML page.

**Tasks**:
- Implement the `full_html()` function of the `NanoDash` class in `exercise1/nanodash/nanodash.py` to return a valid HTML webpage.

**Files to modify**
- `exercise1/nanodash/nanodash.py`

**Command to run tests**
`python -m pytest exercise1/`

### Exercise 2: Implementing input components
---

**Goal**: Implement basic input components as Python objects, to be used as building blocks for interactive dashboards.

**Tasks**:
- Review the implementations of the `Page`, `Header` and `Text` classes in `exercise2/nanodash/components.py`
- Implement the `html()` method of the `TextInput` class
- Implement the `html()` method of the `Dropdown` class

**Files to modify**:
- `exercise2/nanodash/components.py`

**Command to run tests**
`python -m pytest exercise2/`

### Exercise 3: Implementing the Graph component
---

**Goal**: Implement the Graph component, which uses Plotly.js to display Plotly figures in the browser.

**Tasks**:
- Implement the `html()` method of the `Graph` class in `exercise3/nanodash/components.py`

**Files to modify**:
- `exercise3/nanodash/components.py`

**Command to run tests**
`python -m pytest exercise3/`

### Exercise 4: Gathering the page state when an input changes
---

**Goal**: Implement the Javascript logic to capture the state of all components on the page, and bundle it into a JSON request to send to the Flask server.

Don't worry — we've provided some useful helper functions inside the Javascript file; all you need to do is put them together in the right way.

**Tasks**:
- Implement the `getState()` Javascript function in `exercise4/nanodash/static/index.js`.

**Files to modify**:
- `exercise4/static/index.js`

**Command to run tests**
`python -m pytest exercise4/`

### Exercise 5: Running callbacks
---

**Goal**: Implement the Python logic which receives the page state from the frontend, runs the necessary callbacks, and sends the results back to the frontend. Also implement the logic which allows a user to add a callback to their app.

**Tasks**:
- Implement the `handle_change()` Python function in `exercise5/nanodash/nanodash.py`
- Implement the `add_callback()` Python function in `exercise5/nanodash/nanodash.py`

**Files to modify**:
- `exercise5/nanodash/nanodash.py`

**Command to run tests**
`python -m pytest exercise5/`

### Exercise 6: Updating the page with callback results
---

**Goal**: Implement the Javascript logic to update the page's UI components based on the callback results received from the server.

**Tasks**:
- Implement the `updateValues()` Javascript function in `exercise6/nanodash/static/index.js`

**Files to modify**:
- `exercise6/nanodash/static/index.js`

**Command to run tests**
`python -m pytest exercise6/`

### Exercise 7: Writing your own NanoDash application
---

**Goal**: Use the NanoDash framework to write your own interactive dashboard. You can modify the framework or add new components if you like.

**Tasks**:
- Pick a dataset
- Modify `exercise7/app.py` to define an app layout, add graphs and interactive components, and add at least one callback

**Files to modify**:
- `exercise7/app.py`

There are no tests for this exercise since your app can do whatever you like!

## Resources

- Intro to HTML: https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content#creating_your_first_html_document
- Plotly.js documentation: https://plotly.com/javascript/
- Plotly.py documentation: https://plotly.com/python/
- Flask documentation: https://flask.palletsprojects.com/
- Pittsburgh data: https://data.wprdc.org/
