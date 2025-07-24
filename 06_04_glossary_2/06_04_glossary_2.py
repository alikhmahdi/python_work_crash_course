glossary_programming = {
    'string': 'A sequence of characters.',
    'boolean': 'A data type that can be either true or false.',
    'float': 'A data type for representing decimal numbers.',
    'list': 'A collection of items in a particular order.',
    'set': 'A collection of unique items.',
    'tuple': 'An immutable collection of items.',
    'loop': 'A programming construct that repeats a block of code.',
    'function': 'A reusable piece of code that performs a specific task.',
    'variable': 'A named storage location in memory.',
    'dictionary': 'A collection of key-value pairs.',
}
for term, definition in sorted(glossary_programming.items()):
    print(f"What is the meaning of '{term}'?\n{definition}\n")