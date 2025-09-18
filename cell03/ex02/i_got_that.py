# i_got_that.py
print("What you gotta say? : \r")
while True:
    user_input = input()
    
    if user_input == "STOP":
        break
    else:
        print("I got that! Anything else? : ", end="")
