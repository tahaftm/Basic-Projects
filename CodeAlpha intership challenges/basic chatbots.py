def greetings():
    print("Hello there, I am a chatbot here to serve you some information.")
def scope():
    print("My job is to assist you with some task.")
def goodbye():
    print("That's alot of talk lets get to sleep now!")
flag = True
while flag:
    user = input("Say: ").lower()
    if "hello" in user or "hi" in user:
        greetings()
    elif "my name is " in user:
        greetings()
    elif "who are you" in user: 
        scope()
    else:
        goodbye()
        flag = False
       