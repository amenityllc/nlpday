Code for the lecture "Extracting Insights From Text Using spaCy's Pipeline"

NLP Day, November 7th 2019

http://nlpday.ml/

# Directory Structure
* `src`
    Main source code directory. Inside, the folder `notebooks` contains the notebook we will working on during the lecture.
* `data`
   Contains the data we will use in a CSV format.


# Prerequisites
1. Make sure to have `Python 3.6`
2. Install `pipenv` by `pip install pipenv`
3. In your terminal, create a new virtual environment inside a new shell, using the command `pipenv shell` (make sure to run all commands inside this shell to not affect your global environment settings).
    This should create a `.venv` folder inside the project's root folder.
4. Install all the requirements using the `Pipfile` and `Pipfile.lock` files by running the following command: `pipenv sync`.