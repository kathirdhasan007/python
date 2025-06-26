a = input("enter word:").lower()
reverse_str = "" 
for i in a :
    reverse_str = i + reverse_str
    if reverse_str == a:
        answer = "true"
    else:
        answer = "false"
print(answer)