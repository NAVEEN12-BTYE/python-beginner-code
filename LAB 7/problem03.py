# union_lists.py

from typing import List

def union_lists(a: List[int], b: List[int]) -> List[int]:
    seen = set()
    result = []
    for x in a + b:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

# Example usage
if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 2, 1]
    l2 = [3, 5, 6, 2]
    print("Union:", union_lists(l1, l2))  # [1,2,3,4,5,6]
