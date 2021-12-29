___ Xbonacci(signature,n):
    digit = -len(signature)
    while len(signature) < n:
        signature.append(sum(signature[digit:]))
    return signature __ n >= len(signature) else signature[:n]


