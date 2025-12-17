def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status['title']} {status['occupation']}"
           "around.")
    
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.