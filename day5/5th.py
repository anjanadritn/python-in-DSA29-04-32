from collections import deque

def interleave_queue(q):
    n = len(q)

    # Step 1: Split first half
    fh = deque()
    for _ in range(n // 2):
        fh.append(q.popleft())

    # Step 2: Interleave
    while fh:
        q.append(fh.popleft())   # from first half
        q.append(q.popleft())    # from second half

    return q


# Example usage
q = deque([8, 9, 1, 2, 3, 5,9])
result = interleave_queue(q)
print(result)