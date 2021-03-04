#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_converters/ tests/

black democritus_converters/ tests/

mypy democritus_converters/ tests/

pylint --fail-under 9 democritus_converters/*.py

flake8 democritus_converters/ tests/

bandit -r democritus_converters/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_converters/ tests/
