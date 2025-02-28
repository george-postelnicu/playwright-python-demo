# playwright-python-demo
It's a simple demo project to show-case features of `pytest-playwright` on [Lucanet](https://www.lucanet.com/en/) website

## what does this project show-case?
* positive and negative test cases;
* page object pattern;
* using a data driven approach;
* separating concerns and passing data down to the correct level of responsibility;
* using python data class;
* using python static method;
* using pytest/playwright fixtures;
* using different types of playwright locators and chaining them to other locators or filters;
* handling multiple pages with playwright.

## requirements

Before setting up the project, ensure that you have the following installed:
1. **Python 3.12**
This project requires at least Python 3.12. You can download it from the official [Python website](https://www.python.org/downloads/).
2. **pipenv**
Pipenv is necessary to manage the project's dependencies. You can install pipenv using `pip`:
   `pip install pipenv`

## installation steps

Follow these steps to set up the project environment:
1. **Clone the repository** (or download the source code if you haven’t already).
   ```shell
      git clone https://github.com/george-postelnicu/playwright-python-demo
      cd playwright-python-demo
   ```

2. **Install project dependencies**
Run the following command to create a virtual environment and install the required dependencies listed in the `Pipfile`:
   `pipenv install`

3. **Activate the virtual environment**
After the dependencies are installed, activate the virtual environment using:
   `pipenv shell`

## running the tests
Running all the tests is as easy as calling the `pytest` library without any parameters
   `clear;pytest`

If you would like to see the browser or change it, please modify manually the file found in root directory `pytest.ini`
   ```text
   [pytest]
   addopts = --tracing on
             --screenshot on
             --browser chromium
             --base-url https://www.lucanet.com/en/
   ;          --headed
   ;          --slowmo 500
   ```

For more information on how to debug the tests please read [Run-in-debug-mode](https://playwright.dev/python/docs/debug#run-in-debug-mode)