from collections import deque, defaultdict

def alienOrder(words):
    # Step 1: Initialize data structures
    adj_list = defaultdict(set)
    in_degree = defaultdict(int)
    all_chars = set()

    # Step 2: Add all characters to the set
    for word in words:
        for char in word:
            all_chars.add(char)
            if char not in in_degree:
                in_degree[char] = 0

    # Step 3: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in adj_list[word1[j]]:
                    adj_list[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):
                return ""

    # Step 4: Topological Sort (Kahn’s Algorithm)
    queue = deque([char for char in all_chars if in_degree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in adj_list[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == len(all_chars):
        return "".join(result)
    else:
        return ""
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))  
