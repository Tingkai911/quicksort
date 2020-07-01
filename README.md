# quicksort

quicksort and count the number of comparison needed to sort the array
pseudo code as follows

quicksort (array A, length n)
- if n == 1, return
- randomly choose a pivot, p
- partition A around p such that everything to the left of p is <p and everything right of p is >p
- recursively sort <p array
- recursively sort >p array
