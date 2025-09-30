# reciprocal-algorithm
A Python implementation of a non-iterative method for reciprocal computation

This repository contains the Python implementation of the algorithm described in the paper "A Non-Iterative Method for Reciprocal Computation by Exact Error Cancellation.

Description

The algorithm provides a direct, non-iterative method for calculating the exact reciprocal of any integer `n > 1`. The core calculate_reciprocal function uses a single, direct integer division (divmod) to derive N1 and R simultaneously.
We demonstrate that s = a/(1 − r), algebraically collapses to the exact identity 1/n while applying these components within the geometric series summation formula,

How to Run

1.  Download the `reciprocal_algorithm.py` file.
2.  Run the script from your terminal: `python reciprocal_algorithm.py`
3.  The program will prompt you to enter an integer for calculation.

Alternatively, you can run the code directly in your browser using Google Colab:
https://colab.research.google.com/drive/1VBviU-VtnGbvkv8HvPdGNyC0qIZ0xeh_?usp=sharing
