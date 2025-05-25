# playwright-python-demo

[![Tests](https://github.com/george-postelnicu/playwright-python-demo/actions/workflows/playwright_scheduled.yml/badge.svg)](https://github.com/george-postelnicu/playwright-python-demo/actions/workflows/playwright_scheduled.yml)
[![Last Test Status](https://github.com/george-postelnicu/playwright-python-demo/actions/workflows/playwright_scheduled.yml/badge.svg?branch=main&event=schedule)](https://github.com/george-postelnicu/playwright-python-demo/actions/workflows/playwright_scheduled.yml)

It's a simple demo project to show-case features of `pytest-playwright` on [Lucanet](https://www.lucanet.com/en/) website

## what does this project show-case?
* positive and negative test cases;
* page object pattern;
* separating concerns and passing data down to the correct level of responsibility;
* using faker to generate data;
* using python data class;
* using python static method;
* using pytest/playwright fixtures;
* using pytest parametrize;
* using pytest mark;
* hashing the contents of files to assert it;
* using different types of playwright locators and chaining them to other locators or filters;
* handling python i18n with gettext module;
* handling multiple pages with playwright;
* handling downloads with playwright;
* interacting in the Lucanet pages with custom selects, iframes, modals, form and form validation, nav menu and a language switcher.

## requirements

Before setting up the project, ensure that you have the following installed:
1. **Python 3.12**
This project requires at least Python 3.12. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **pipenv**
Pipenv is necessary to manage the project's dependencies. You can install pipenv using `pip`:
   ```shell
   pip install pipenv
   ```
   
3. **Python i18n**
For Python i18n (internationalization), we'll use Python [gettext module](https://docs.python.org/3/library/gettext.html)
that depending on your system setup, you might need to install [gettext](https://www.gnu.org/software/gettext/manual/) along with its tools
   ```shell
   sudo apt install gettext
   ```

## installation steps

Follow these steps to set up the project environment:
1. **Clone the repository** (or download the source code if you haven’t already).
   ```shell
      git clone https://github.com/george-postelnicu/playwright-python-demo
      cd playwright-python-demo
   ```

2. **Install project dependencies**
Run the following command to create a virtual environment and install the required dependencies listed in the `Pipfile`:
   ```shell
   pipenv install
   ```

3. **Activate the virtual environment**
After the dependencies are installed, activate the virtual environment using:
   ```shell
   pipenv shell
   ```

4. **Generate the binaries for the lokalise portable objects**
We can rely on the msgfmt tool that also comes packaged with gettext.
   ```shell
   msgfmt -o locales/de/LC_MESSAGES/lokalise.mo locales/de/LC_MESSAGES/lokalise.po
   msgfmt -o locales/en/LC_MESSAGES/lokalise.mo locales/en/LC_MESSAGES/lokalise.po
   msgfmt -o locales/es/LC_MESSAGES/lokalise.mo locales/es/LC_MESSAGES/lokalise.po
   msgfmt -o locales/fr/LC_MESSAGES/lokalise.mo locales/fr/LC_MESSAGES/lokalise.po
   msgfmt -o locales/it/LC_MESSAGES/lokalise.mo locales/it/LC_MESSAGES/lokalise.po
   msgfmt -o locales/nl/LC_MESSAGES/lokalise.mo locales/nl/LC_MESSAGES/lokalise.po
   ```

## running the tests
Running all the tests is as easy as calling the `pytest` library without any parameters
   ```shell
   clear;pytest
   ````

Running tests with markers:
   ```shell
   clear;pytest -m title
   clear;pytest -m language
   clear;pytest -m search
   clear;pytest -m window
   clear;pytest -m form
   clear;pytest -m download
   ```

If you would like to see the browser or change it, please modify manually the file found in root directory `pytest.ini`
   ```text
   [pytest]
   addopts = --tracing retain-on-failure
             --screenshot only-on-failure
             --video retain-on-failure
             --browser chromium
             --base-url https://www.lucanet.com/en/
             --junit-xml test-results/junit.xml
   ;          --headed
   ;          --slowmo 500
   ```

## debugging the tests
To open a trace for a failed test
```shell
playwright show-trace test-results/name-of-failed-test/trace.zip
```

For more information on how to debug the tests, please read [Run-in-debug-mode](https://playwright.dev/python/docs/debug#run-in-debug-mode)