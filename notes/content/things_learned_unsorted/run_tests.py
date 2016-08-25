#!/usr/bin/env python
# run_tests.py
# David Branner
# 20150320

"""Run all tests and log output and test results."""

import sys
import os
sys.path.append(os.path.join('lib', 'utils', 'Docstring_Page'))
import docstring_page
import pytest
import datetime

# Generate date/time of current test run.
date_string = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H%MUTC')
full_date = date_string
#
# Pass parameters to Pytest:
#  * verbose output
#  * results logged with date appended to log file
#  * output recorded with date appended to output file
#  * output also displayed to STDOUT via tee
pytest.main(['tests', '-v', '--result-log=./doc/test_results_{}'.format(full_date)])
#
# Generate current list of docstrings and save as Markdown file.
print('Now generating docstring listing page.')
docstring_page.main(directory='tests')