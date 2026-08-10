def generate_ai_response(message: str, mode: str = "coach"):
    text = message.lower()
    if mode == "hint":
        return {"mode": mode, "answer": "Start with constraints and observations. Decide the required data structure before writing code."}
    if mode == "review":
        return {"mode": mode, "answer": "Review correctness, edge cases, time complexity, space complexity, naming and unnecessary nested loops."}
    if "array" in text:
        answer = "Check sorting, hashing, two pointers, sliding window, prefix sums and binary search."
    elif "tree" in text:
        answer = "Check DFS, BFS, subtree information and traversal order."
    elif "graph" in text:
        answer = "Check BFS, DFS, shortest path, topological sort and DSU."
    else:
        answer = "Break the problem into constraints, brute force, observation, optimization and complexity."
    return {"mode": mode, "answer": answer}
