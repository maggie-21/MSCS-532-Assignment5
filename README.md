# MSCS-532-ASSIGNMENT3

## Overview
This assignment explores and compares two fundamental algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The objective is to analyze their efficiency, scalability, and performance across different input types, as well as to implement and test each algorithm.

- **Randomized Quicksort**: A sorting algorithm that uses a random pivot selection to maintain average-case \(O(n \log n)\) performance, even on challenging inputs like sorted or reverse-sorted arrays.
- **Hashing with Chaining**: A hash table implementation that uses chaining to handle collisions, maintaining efficient insert, search, and delete operations even with a high load factor.


## Project Structure
- `DeterministicQuickSort.py`: Contains the implementation of **Deterministic Quicksort**.
- `RandomizedQuickSort.py`: Contains the implementation of **Randomized Quicksort**.
- `TestDeterministicQuickSort.py`: Script with test cases to evaluate the performance of Deterministic Quicksort.
- `TestRandomizedQuickSort.py`: Script with test cases to evaluate the performance of Randomized Quicksort.
- `CompareQuickSort.py`: Script to compare the performance of Deterministic and Randomized Quicksort on various input types and sizes.




## Requirements
- **Python 3.x** is required to run the scripts.
- No additional libraries are needed as this implementation uses standard Python libraries.

## Usage

### 1. Randomized Quicksort
To test the **Randomized Quicksort** implementation, you can run the `TestRandomizedQuickSort.py` script:

```bash
python3 TestRandomizedQuickSort.py
```
This script:

- Tests the performance of Randomized Quicksort on various input types (empty array, random array, sorted array, reverse-sorted array, and array with repeated elements).
- Compares execution times across different input sizes, verifying the \(O(n \log n)\) average-case complexity.

### 2. Compare Randomized Quicksort and Deterministic Quicksort
To compare **Deterministic Quicksort** with **Randomized Quicksort**, you can run the `CompareQuickSort.py` script:

```bash
python3 CompareQuickSort.py
```
This script:

- Compares execution times of Randomized and Deterministic Quicksort on the same input types and sizes.
- Demonstrates the effect of pivot selection on performance, particularly for sorted and reverse-sorted arrays.

### 3. Compare Deterministic and Randomized Quicksort
To compare the performance of both algorithms, run the `CompareQuickSort.py` script:

```bash
python3 CompareQuickSort.py
```
This script:
- Compares the execution times of Deterministic and Randomized Quicksort on identical input types and sizes.
- Demonstrates the significant performance improvement of Randomized Quicksort on sorted and reverse-sorted arrays.
## Results
The test results are saved as output in the terminal and can be used to analyze the relative efficiency of the two implementations. Key observations include:
- Randomized Quicksort consistently avoids the \(O(n^2)\) worst-case performance observed in Deterministic Quicksort for sorted and reverse-sorted arrays.
- Both algorithms perform efficiently (\(O(n \log n)\)) for random and repeated-element arrays.




### Conclusion
This project provides a comprehensive analysis of **Randomized Quicksort** and **Hashing with Chaining**, exploring their strengths, limitations, and best use cases. The test scripts allow users to observe the efficiency and robustness of each algorithm under different input scenarios.
