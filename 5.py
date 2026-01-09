def reverse_number_string(n):
    
    num_str = str(n)
    
   
    reversed_str = num_str[::-1]
    
  
    
    reversed_num = int(reversed_str)
    return reversed_num


number1 = 12345

print(f"Original: {number1}, Reversed: {reverse_number_string(number1)}")

