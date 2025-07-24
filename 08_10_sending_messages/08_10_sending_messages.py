def send_messages(messages):
    '''Simulate sending messages and return a list of sent messages.'''
    sent_messages = []
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)
        
    return sent_messages
messages = ["Hello, World!", "How are you today?", "Goodbye!"]
sent = send_messages(messages)
print("Messages didn't send successfully:", messages)
print("All sent messages:", sent)
