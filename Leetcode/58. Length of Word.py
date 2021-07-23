def length(s):
    count = 0 
        
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            count += 1
        if s[i] == " " and count >=1:
            return count 
    return count 

print(length("Hello World"))
print(length(" "))
print(length("  s  "))
print(length("abc   "))