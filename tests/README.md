# NanoDash Tutorial Tests

This directory contains test modules for validating student implementations of the NanoDash framework.

## Test Structure

The tests are organized by exercise, matching the incremental steps of the tutorial:

1. **Exercise 1: Flask Server Setup** (`test_exercise1.py`)
   - Tests if a basic Flask server runs
   - Verifies HTML structure and required script inclusion

2. **Exercise 2: Component Implementation** (`test_exercise2.py`)
   - Tests if required components (TextInput and Dropdown) render correctly
   - Validates component interaction works as expected

3. **Exercise 3: Graph Component** (`test_exercise3.py`)
   - Tests if Plotly graphs render correctly
   - Verifies graph structure and elements

4. **Callback Implementation**
   - **Exercise 4a: Client-to-Server** (`test_exercise4a.py`): Tests if frontend can send state to backend
   - **Exercise 4b: Server Processing** (`test_exercise4b.py`): Tests if callbacks process inputs correctly
   - **Exercise 4c: UI Updates** (`test_exercise4c.py`): Tests if frontend updates based on callback responses

5. **Exercise 5: Complete Application** (`test_exercise5.py`)
   - Tests a complete nanodash application with real data
   - Validates the application behaves correctly with user interaction

## Helper Modules
- **test_utils.py**: Helper functions for interacting with web components, and making server start / stop. 

## Running Tests

Tests require:
- Selenium WebDriver
- Chrome browser
- Running Flask server (tests will start and stop servers automatically)

Run tests for a specific exercise:
```
pytest tests/test_exercise1.py -v
```

Run all tests:
```
pytest tests/
```

## Dependencies

- Selenium
- pytest
- requests
- Flask (for the student implementation)