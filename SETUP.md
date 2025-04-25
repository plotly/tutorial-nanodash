# NanoDash tutorial: Setup instructions

Thanks for registering for the NanoDash tutorial! This guide provides step-by-step instructions to set up your local machine for the tutorial.

The terminal commands below are intended for Bash or similar Unix shells. If you are using Windows, you can use Git Bash, WSL, or another Bash shell tool.

## 1. Cloning the repository

Clone the repository onto your machine:

```bash
$ git clone https://github.com/plotly/tutorial-nanodash
$ cd tutorial-nanodash/
```

## 2. Setting up your Python environment

This tutorial is intended to be completed with **Python 3.12** (or newer). Older versions of Python may work, but the tutorial has only been tested with 3.12.

We encourage the use of a virtual environment. You can use any virtual environment manager you prefer. If you don't have a favorite, we recommend `uv`. 

To create a virtual environment using `uv`, first make sure you are in the root directory of the repository, then run:

```bash
$ pip install uv
$ uv venv --python 3.12
```

To activate the `uv` virtual environment, run:

```bash
$ source .venv/bin/activate
```

Verify that your environment is correctly activated and using the right Python version by running:

```bash
$ which python
$ python --version
```

`which python` should output a path ending with ` .venv/bin/python`

`python --version` should output `Python 3.12.x`

## 3. Installing requirements

After setting up and activating your Python virtual environment, install the requirements for the tutorial, which are listed in `requirements.txt`.

_Note: When using a `uv` virtual environment, `pip` must be replaced by `uv pip`._

If you are using `uv`, run:

```bash
$ uv pip install -r requirements.txt
```

Otherwise:

```bash
$ pip install -r requirements.txt
```

Next, verify that the key packages are installed correctly.

If you are using `uv`, run:

```bash
$ uv pip freeze | grep -E "flask|pandas|plotly|requests|pytest|selenium"
```

Otherwise:

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


## 4. Checking that everything is working

To make sure everything is installed correctly, try running the Exercise 7 tests:

```bash
$ python -m pytest exercise7/
```

You should see a message indicating that one test has passed.

That's it, you're all set up! 🎉

## Next steps

If you like, feel free to take a look at the [README](https://github.com/plotly/tutorial-nanodash/blob/main/README.md) for information about the repository structure and tutorial exercises.

See you there!
