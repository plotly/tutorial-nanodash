# NanoDash Tutorial: Setup Instructions

Thanks for registering for the NanoDash tutorial! The following outlines installation instructions for setting up your local machine before the tutorial.

The terminal commands in these instructions are intended for Bash or a similar Unix shell. If you are on Windows, use Git Bash or another  Bash shell tool for Windows.

## 1. Cloning the repository

Clone the repository onto your machine:

```bash
$ git clone https://github.com/plotly/tutorial-nanodash
$ cd tutorial-nanodash/
```

## 2. Setting up your Python environment

This tutorial is intended to be completed with **Python 3.12** (or newer). Older versions of Python may work, but the tutorial has only been tested with 3.12.

We encourage the use of a virtual environment to keep things clean. Feel free to use your favorite virtual environment manager. If you don't have a favorite, we recommend `uv`. To create a virtual environment using `uv`, first make sure you are in the root directory of the repository, then run:

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

The path should be the path to your current working directory, followed by `.venv/bin/python`.

Finally, verify your Python version:

```bash
$ python --version
```

You should see some version of `Python 3.12`.



## 3. Installing requirements

After setting up and activating your Python virtual environment, install the requirements for the tutorial.

_Note: When using a `uv` virtual environment, `pip` must be replaced by `uv pip`._

If you are using `uv`, run:

```bash
$ uv pip install -r requirements.txt
```

Otherwise:

```bash
$ pip install -r requirements.txt
```

Verify that the requirements are installed, and check package versions, by running the following if you are using `uv`:

```bash
$ uv pip freeze | grep -E "flask|pandas|plotly|requests|pytest|selenium"
```

Or if you are not using `uv`:

```bash
$ pip freeze | grep -E "flask|pandas|plotly|requests|pytest|selenium"
```

The output should look something like this:

```
flask==3.1.0
pandas==2.2.3
plotly==6.0.1
pytest==8.3.5
requests==2.32.3
selenium==4.31.0
```

It's okay if your installed package versions are slightly different, as long as the following step completes successfully.


## 4. Checking that everthing is working

To make sure everything is installed correctly, try running the Exercise 7 tests:

```bash
$ python -m pytest exercise7/
```

You should see a message indicating that one test has passed.

---

That's it, you're all set up!  🎉

Feel free to take a look at the [README](https://github.com/plotly/tutorial-nanodash/blob/main/README.md) for information about the repository structure and tutorial exercises. See you there!
