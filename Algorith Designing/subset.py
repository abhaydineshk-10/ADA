def subset_sum(S, target):
    result = []
    
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        
        for i in range(start, len(S)):
            path.append(S[i])
            backtrack(i + 1, path, current_sum + S[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result


# Example usage
S = [3, 34, 4, 12, 5, 2]
target = 9
subsets = subset_sum(S, target)

print(f"Subsets of {S} that sum to {target}:")
for subset in subsets:
    print(subset)