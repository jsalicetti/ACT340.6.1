#  p1

states2 = {
    "Los Angeles": "California",
    "Albany": "New York",
    "Honolulu": "Hawaii",
    "Juneau": "ALaska",
    "Austin":"Texas"
}

states = dict([
    ("California","Los Angeles" ),
    ("New York","Albany" ),
    ("Hawaii", "Honolulu" ),
    ("Alaska", "Juneau" ),
    ("Texas", "Austin")
])

print(type(states))
print(type(states2))
print(states)
print(states2)


# p2

numbers= dict([
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
    (5, 'Five')
])

numbers[1]

numbers[6] = 'Six'
print(numbers)

numbers[1]= '1'
print(numbers)

del numbers[1]
print(numbers)

# p2

print(states["California"])

states["Florida"] = "Tallahase"
print(states)

states["California"] = "Sacremento"
print(states)

del states['Alaska']
print(states)

# p3

playlist = dict([
    ("Machine Girl1", "Ghost"),
    ("Machine Girl2", "Rigged Game"),
    ("Machine Girl3", "Frenesi"),
    ("Machine Girl4", "Glass Ocean"),
    ("Machine Girl5", "Thousand Pound Butterfly"),
    ("Machine Girl6", "Krystle")
])

for key in playlist:
    print(key)
for values in playlist.values():
    print(values)

for key, value in playlist.items():
    print(f"{value} by {key} is in the current playlist") #the key inside the curly brackets comes from our key iterator in the for loop

del playlist["Machine Girl6"]
print(playlist)

playlist["Taylor Swift"] = "Anti-Hero"

print(playlist)

prefix = "REMIX: "

playlist["Machine Girl1"] = prefix + playlist["Machine Girl1"]

print(playlist)

def allSongs(playlist):
    for key, value in playlist.items():
        print(f"Artist: {key}")
        print(f"Song: {value}")

allSongs(playlist)