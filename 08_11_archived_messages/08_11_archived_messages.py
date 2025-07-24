def archive_messages(sent_messages):
    '''Simulate archiving messages and return a list of archived messages.'''
    archived_messages = []
    while sent_messages:
        message = sent_messages.pop(0)
        print(f"Archiving message: {message}")
        archived_messages.append(message)

    return archived_messages
messages = ["Hello, World!", "How are you today?", "Goodbye!"]
archived = archive_messages(messages[:])
print("Messages who wanted to be archived:", messages)
print("All archived messages:", archived)