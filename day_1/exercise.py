# ITP Week 2 Day 1 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

for item in inventory:
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory[item] -= 1
    print(inventory[item])
    # NOTE: recall that item represents the key of the key:value pair

# # SCENARIO: REMOVE ANY 0 ITEMS

for item in inventory:
    # use an if statement to check if the value is 0 and then remove it
    inventory [item] -= 1
    if inventory [item] < 1:
        del inventory [item]

    print(inventory)

