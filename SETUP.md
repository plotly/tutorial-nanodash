# NanoDash Tutorial: Setup Instructions

Thanks for registering for the NanoDash tutorial! The following outlines installation instructions for setting up your local machine before the tutorial.

The terminal commands in these instructions are intended for Bash or a similar Unix shell. If you are on Windows, use Git Bash or another Windows Bash shell tool.

## 1. Cloning the repository

Clone the repository onto your machine:

```bash
$ git clone https://github.com/plotly/tutorial-nanodash
$ cd tutorial-nanodash/
```

## 2. Setting up your Python environment

This tutorial is intended to be completed with **Python 3.12** (or newer). Older versions of Python may work, but the tutorial has only been tested with 3.12.

We encourage the use of a virtual environment to keep things clean. Feel free to use your favorite virtual environment manager. If you don't have one, we recommend `uv`. To create and activate a virtual environment using `uv`, first make sure you are in the root directory of the repository, then run:

```bash
$ pip install uv
$ uv venv --python 3.12
```

To activate the `uv` virtual environment, run:

```bash
$ source .venv/bin/activate
```

Make sure the environment is correctly activated by checking which `python` your terminal is using:

```bash
$ which python
```

The end of the path should look like `.venv/bin/python`.

Finally, verify your Python version:

```bash
$ python --version
```

You should see some version of `Python 3.12`.



## 3. Installing requirements

After setting up and activating your Python virtual environment, install the requirements for the tutorial. 

If you are using `uv`, run:

```bash
$ uv pip install -r requirements.txt
```

Otherwise:

```bash
$ pip install -r requirements.txt
```

## 4. Checking that everthing is working

To make sure everything is installed correctly, try running the Exercise 7 tests:

```bash
$ python -m pytest exercise7/
```

You should see a message indicating that one test has passed.

That's it, you're all set up! 

Feel free to take a look at the [README](https://github.com/plotly/tutorial-nanodash/blob/main/README.md) for information about the repository structure and tutorial exercises. See you there!
