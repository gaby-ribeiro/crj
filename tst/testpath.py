"""Path hack to make tests work with pylint."""

import os
import sys

base_path = os.path.realpath(os.curdir).split(os.sep)

# Add project library directory to PYTHONPATH for test executions.
base_path.append('lib')
sys.path.insert(0, os.sep.join(base_path))
