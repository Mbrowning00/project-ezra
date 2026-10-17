from datetime import datetime

def get_time():
    current_time = datetime.now()
    return current_time.strftime("%I:%M %P")

def normalize_command(command):
    command = command.strip().lower()

    aliases = {
        "good bye": "goodbye",
        "bye": "goodbye",
        "hi": "hello",
        "hey": "hello",
        "what time is it": "time"
    }

    return aliases.get(command, command)
    

def respond(command):
    if command == "hello":
        return "Hello! How can I help you?"
    elif command == "goodbye":
        return "Goodbye! Talk to you later."
    elif command == "time":
        return "The current time is " + get_time()
    else:
        return "Sorry, I don't understand that concept"

while True:
    user_command = input("Enter a command: ")
    user_command = normalize_command(user_command)

    response = respond(user_command)
    print(response)
          
    if user_command == "goodbye":
        break