"""Imagine that you have bought a bunch of lottery tickets and wrote down their numbers into the list. Now, it's time to figure out whether you have a winning ticket.

You know that all winning tickets are no less than 44. Fill the empty fields in the code (these ones ...) to check if you have at least one winning ticket.

You DON'T need to print the answer."""

# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= 44 for i in tickets]
tickets_bool = any(winning_tickets)
