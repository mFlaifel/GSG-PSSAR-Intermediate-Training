## 4. Step-by-Step Code Execution Trace

Let's dry-run the logic using: **Target = 10** and **Sorted Transactions = `[1, 3, 7, 12]`**

| Step | Left Index (Value) | Right Index (Value) | Current Sum | Distance to Target (10) | Best Sum Tracker | Next Action Decision |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 (`1`) | 3 (`12`) | $1 + 12 = \mathbf{13}$ | 3 units away | **13** | Sum is too high! Decrement `right` pointer. |
| **Step 2** | 0 (`1`) | 2 (`7`) | $1 + 7 = \mathbf{8}$ | 2 units away *(Closer!)* | **8** (Updated) | Sum is too low! Increment `left` pointer. |
| **Step 3** | 1 (`3`) | 2 (`7`) | $3 + 7 = \mathbf{10}$ | 0 units away *(Perfect!)* | **10** (Updated) | **Exact match reached! Return 10 instantly.** |