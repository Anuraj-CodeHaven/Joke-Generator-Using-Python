#Author :Anuraj R

import random as r
import time 
def joking():
    jokes_dict = {
    1: "Why don’t scientists trust atoms? Because they make up everything!",
    2: "What did the ocean say to the beach? Nothing, it just waved.",
    3: "Why did the scarecrow win an award? Because he was outstanding in his field!",
    4: "Why don’t skeletons fight each other? They don’t have the guts.",
    5: "What do you call fake spaghetti? An impasta!",
    6: "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    7: "How does a penguin build its house? Igloos it together!",
    8: "Why did the bicycle fall over? Because it was two-tired!",
    9: "What’s orange and sounds like a parrot? A carrot!",
    10: "Why can’t you give Elsa a balloon? Because she will let it go.",
    11: "What do you call cheese that isn’t yours? Nacho cheese.",
    12: "How does NASA organize a party? They planet.",
    13: "Why did the chicken join a band? Because it had the drumsticks.",
    14: "Why was the math book sad? Because it had too many problems.",
    15: "How does a computer get drunk? It takes screenshots.",
    16: "Why did the golfer bring extra pants? In case he got a hole in one.",
    17: "What do you call a fish wearing a bowtie? Sofishticated.",
    18: "How do you make a tissue dance? You put a little boogie in it.",
    19: "What do you get when you cross a snowman and a vampire? Frostbite.",
    20: "Why did the tomato turn red? Because it saw the salad dressing.",
    21: "How does a scientist freshen their breath? With experi-mints.",
    22: "Why don’t crabs give to charity? Because they’re shellfish.",
    23: "How do you catch a whole school of fish? With bookworms.",
    24: "Why did the golfer bring extra pants? In case he got a hole in one.",
    25: "How do you organize a space party? You planet.",
    26: "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field!",
    27: "Why are elevator jokes so good? They work on so many levels.",
    28: "How does a penguin build its house? Igloos it together!",
    29: "What do you call a snowman with a six-pack? An abdominal snowman.",
    30: "Why did the cookie go to the hospital? Because it felt crummy.",
    31: "How do you make a Kleenex dance? Put a little boogie in it.",
    32: "What’s a skeleton’s least favorite room in the house? The living room.",
    33: "Why don’t skeletons fight each other? They don’t have the guts.",
    34: "Why did the photo go to jail? It was framed!",
    35: "How does the moon cut his hair? Eclipse it.",
    36: "What do you get when you cross a snowman and a vampire? Frostbite.",
    37: "Why did the stadium get hot after the game? All the fans left.",
    38: "Why don’t skeletons play music in church? They don’t have organs.",
    39: "How do you catch a squirrel? Climb a tree and act like a nut!",
    40: "Why can’t your nose be 12 inches long? Because then it would be a foot.",
    41: "Why did the scarecrow win an award? Because he was outstanding in his field!",
    42: "What do you call a pile of cats? A meowtain.",
    43: "Why was the math book sad? Because it had too many problems.",
    44: "How does a computer get drunk? It takes screenshots.",
    45: "Why don’t oysters donate to charity? Because they are shellfish.",
    46: "How does NASA organize a party? They planet.",
    47: "Why did the tomato turn red? Because it saw the salad dressing.",
    48: "How do you make holy water? You boil the hell out of it.",
    49: "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    50: "What do you call a fish wearing a bowtie? Sofishticated.",
    51: "Why did the golfer bring extra pants? In case he got a hole in one.",
    52: "How do you make a Kleenex dance? Put a little boogie in it.",
    53: "Why can’t you give Elsa a balloon? Because she will let it go.",
    54: "How does a scientist freshen their breath? With experi-mints.",
    55: "Why don’t crabs give to charity? Because they’re shellfish.",
    56: "Why was the computer cold? It left its Windows open.",
    57: "How do you catch a whole school of fish? With bookworms.",
    58: "What did one wall say to the other? I’ll meet you at the corner.",
    59: "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field!",
    60: "How does a penguin build its house? Igloos it together!",
    61: "Why are elevator jokes so good? They work on so many levels.",
    62: "What’s a skeleton’s least favorite room in the house? The living room.",
    63: "Why did the photo go to jail? It was framed!",
    64: "How does the moon cut his hair? Eclipse it.",
    65: "Why did the stadium get hot after the game? All the fans left.",
    66: "Why don’t skeletons fight each other? They don’t have the guts.",
    67: "Why did the cookie go to the hospital? Because it felt crummy.",
    68: "How do you make holy water? You boil the hell out of it.",
    69: "What do you get when you cross a snowman and a vampire? Frostbite.",
    70: "How do you catch a squirrel? Climb a tree and act like a nut!",
    71: "What do you call a pile of cats? A meowtain.",
    72: "How do you make a Kleenex dance? Put a little boogie in it.",
    73: "How does NASA organize a party? They planet.",
    74: "Why don’t skeletons play music in church? They don’t have organs.",
    75: "Why can’t your nose be 12 inches long? Because then it would be a foot.",
    76: "What did one wall say to the other? I’ll meet you at the corner.",
    77: "Why did the tomato turn red? Because it saw the salad dressing.",
    78: "How does a scientist freshen their breath? With experi-mints.",
    79: "Why was the computer cold? It left its Windows open.",
    80: "How do you make holy water? You boil the hell out of it.",
    81: "Why don’t oysters donate to charity? Because they are shellfish.",
    82: "What do you call a pile of cats? A meowtain.",
    83: "How do you catch a squirrel? Climb a tree and act like a nut!",
    84: "What’s orange and sounds like a parrot? A carrot!",
    85: "Why did the scarecrow win an award? Because he was outstanding in his field!",
    86: "What did the ocean say to the beach? Nothing, it just waved.",
    87: "Why don’t scientists trust atoms? Because they make up everything!",
    88: "How does the moon cut his hair? Eclipse it.",
    89: "Why don’t skeletons fight each other? They don’t have the guts.",
    90: "Why did the photo go to jail? It was framed!",
    91: "How do you make a Kleenex dance? Put a little boogie in it.",
    92: "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    93: "What do you call fake spaghetti? An impasta!",
    94: "Why was the math book sad? Because it had too many problems.",
    95: "Why did the bicycle fall over? Because it was two-tired!",
    96: "Why don’t crabs give to charity? Because they’re shellfish.",
    97: "How does a penguin build its house? Igloos it together!",
    98: "How do you catch a whole school of fish? With bookworms.",
    99: "How does NASA organize a party? They planet.",
    100: "Why was the computer cold? It left its Windows open."
    }
    
    joke=r.randint(1,100)
    print(jokes_dict[joke])
    
print("----Welcome to the Applications----\n\n\n----Keep Smile😃 Stay Healthy ----")
print("\n\n")
while True:
    print("\nThinking for a Joke Wait .....\n\n")
    print("----------------")
    time.sleep(2)
    joking()
    print("------------------")
    print("\n\nAre you enjoy the Joke...\nIf not enjoy the above joke enter \"yes\" for creating a new one.....\notherwise enter \"no\" to quit...\n ")

    choice =input("Enter your choice only \"yes\" or \"no\" ").lower()
    if choice=="no":
        print("\n----Thank you for Using ----")
        break
    
