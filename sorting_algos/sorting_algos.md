# Sorting Algorithms

## Algorithm Comparison Table

| Algorithm      | Best Case  | Average Case | Worst Case | Space Complexity | Stable | In-Place | Notes                    |
| -------------- | ---------- | ------------ | ---------- | ---------------- | ------ | -------- | ------------------------ |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes    | Yes      | Simple but inefficient   |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)             | No     | Yes      | Minimizes swaps          |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes    | Yes      | Good for small datasets  |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes    | No       | Divide and conquer       |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | No     | Yes      | Popular general-purpose  |
| Heap Sort      | O(n log n) | O(n log n)   | O(n log n) | O(1)             | No     | Yes      | Uses heap data structure |
| Radix Sort     | O(nk)      | O(nk)        | O(nk)      | O(n+k)           | Yes    | No       | Non-comparison based     |
| Counting Sort  | O(n+k)     | O(n+k)       | O(n+k)     | O(k)             | Yes    | No       | For integer sorting      |
| Bogo Sort      | O(n)       | O((n+1)!)    | O(∞)       | O(1)             | No     | Yes      | Joke algorithm           |

## Implementation Status

| Algorithm      | Implemented | File           | Last Updated | Status   |
| -------------- | ----------- | -------------- | ------------ | -------- |
| Bogo Sort      | ✅           | `bogo_sort.py` | -            | Complete |
| Bubble Sort    | ❌           | -              | -            | Pending  |
| Selection Sort | ❌           | -              | -            | Pending  |
| Insertion Sort | ❌           | -              | -            | Pending  |
| Merge Sort     | ❌           | -              | -            | Pending  |
| Quick Sort     | ❌           | -              | -            | Pending  |
| Heap Sort      | ❌           | -              | -            | Pending  |

## Testing Results

| Algorithm | Input Size | Time (ms) | Memory (MB) | Test Cases Passed |
| --------- | ---------- | --------- | ----------- | ----------------- |
| Bogo Sort | 10         | -         | -           | -/-               |
| Bogo Sort | 100        | -         | -           | -/-               |
| Bogo Sort | 1000       | -         | -           | -/-               |

---

*Note: You can update this table as you implement and test different sorting algorithms.*