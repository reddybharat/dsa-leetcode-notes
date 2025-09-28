| Situation / Input                       | Best Approach                   | Why / When                                                                  |
| --------------------------------------- | ------------------------------- | --------------------------------------------------------------------------- |
| Array is **sorted**                     | Binary Search / Two Pointers    | Sorted order enables log-time search and pointer sweeps.                    |
| Need **all subsets/permutations**       | Backtracking                    | Explore entire solution space with pruning.                                 |
| Given a **Tree**                        | DFS / BFS                       | DFS for recursion & depth problems, BFS for level-order/shortest path.      |
| Given a **Graph**                       | DFS / BFS                       | DFS for connectivity/cycles, BFS for shortest path/bipartite check.         |
| Given a **Linked List**                 | Two Pointers                    | Fast/slow pointers for cycle detection, middle, or intersection.            |
| Recursion **not allowed**               | Stack                           | Explicitly simulate call stack.                                             |
| Must solve **in-place**                 | Swap values / Encode in pointer | Save space by reusing array slots or encoding visited state.                |
| Find **max/min subarray/subset/option** | Dynamic Programming (DP)        | Break into subproblems, store results, reuse for efficiency.                |
| Find **top/least K items**              | Heap / QuickSelect              | Heap for streaming or online queries; QuickSelect for average O(n).         |
| Find **common strings**                 | Map / Trie                      | Map for counting; Trie for prefix-based problems.                           |
| General fallback                        | Map/Set OR Sort                 | Hashing for O(1) lookup; Sorting when hashing not allowed or order matters. |
