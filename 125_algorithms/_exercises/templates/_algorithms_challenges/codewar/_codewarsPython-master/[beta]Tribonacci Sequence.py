___ tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature __ n >= len(signature) else signature[:n]

