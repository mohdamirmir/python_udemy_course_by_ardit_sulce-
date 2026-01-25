def strength(password):
    result = {}
    
    result["length"] = True if len(password) > 8 else False
    
    digit = False
    uppercase = False
    
    for char in password:
        if char.isdigit():
            digit = True
    


    for char in password:
        if char.isupper():
            uppercase = True
    
    result["digit"] = digit    
    result["uppercase"] = uppercase
        

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"
    
    
strength("abcde")