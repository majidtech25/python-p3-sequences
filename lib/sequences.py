#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    if length > 0:
        sequence.append(0)
    if length > 1:
        sequence.append(1)
    while len(sequence) < length:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    print(sequence)
 
    
  
  
  
    