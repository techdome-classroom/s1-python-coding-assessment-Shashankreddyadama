def decode_message( s: str, p: str) -> bool:
    message=s
    pattern=p
    m, n = len(message), len(pattern)
    
    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: an empty message matches an empty pattern
    dp[0][0] = True
    
    # Handle the case where the pattern starts with *
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '?':
                # '?' matches any single character
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                # '*' matches empty sequence or non-empty sequence
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                # Exact match required for current characters
                dp[i][j] = dp[i - 1][j - 1] and message[i - 1] == pattern[j - 1]
    
    # The result will be in dp[m][n]
    return dp[m][n]
 