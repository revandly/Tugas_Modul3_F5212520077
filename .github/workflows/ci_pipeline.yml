name: Python CI Pipeline - Sistem Perpustakaan

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    # STEP FLAKE8 LINTER (Sesuai Tugas 1)
    - name: Run flake8 linter
      run: |
        flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics

    - name: Run tests with pytest
      run: |
        pytest