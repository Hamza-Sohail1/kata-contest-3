def highest_value_palindrome(s, n, k):
    result = list(s)
    
    # two var i and j for comparing left and right value to make it palindrome
    for i in range(n // 2 + 1):
        j = n - i - 1
        if result[i] != result[j]:
            # it means that we can make above string palindrome within the max limit of changes allowed
            if k <= 0:
                return "-1"
            max_char = max(result[i], result[j])
            result[i] = result[j] = max(result[i], result[j])
            k -= 1

    i = 0
    # if we have more changes remaining then we can convert digits to 9 to get highest value palindrome
    while (i < n/2 and k > 0):
        j = n - i - 1
        if result[i] == '9':
            i += 1
            continue

        # if we have already change that index then we can ignore that change and replace its value with 9
        # or if it is center in case of odd length then only single change is needed
        if result[i] != s[i] or result[j] != s[j] or i == j:
            result[i] = result[j] = '9'
            k -= 1
        else:
            if k >= 2:
                # if they are not previously swapped then replaced both with 9 and dec by 2 because we have done 2 swaps
                result[i] = result[j] = '9'
                k -= 2
        
        i +=1

    return "".join(result)

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input().rstrip()
    
    result = highest_value_palindrome(s, n, k)
    
    print(result)
