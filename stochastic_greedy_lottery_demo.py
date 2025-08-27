import random
from collections import defaultdict
from math import comb

# Parameters
NUMBERS = 43   # numbers 1–43
PICKS = 6      # choose 6 numbers per ticket
COVER_SIZE = 5 # target coverage (5-of-6)

def generate_ticket():
    """Generate a random lottery ticket of 6 numbers (sorted)."""
    return tuple(sorted(random.sample(range(1, NUMBERS+1), PICKS)))

def ticket_score(ticket, freq=None, popularity_penalty=False):
    """
    Score a ticket.
    - freq: optional dict {num: bias probability} from historical data.
    - popularity_penalty: if True, penalize commonly picked numbers.
    """
    score = 0.0
    if freq:
        for n in ticket:
            # If drawing bias exists: prefer higher probability
            score += freq.get(n, 1/NUMBERS)
    else:
        score = 1.0

    if popularity_penalty and freq:
        # Inverse weighting to avoid popular numbers
        for n in ticket:
            score -= 0.5 * freq.get(n, 1/NUMBERS)

    return score

def stochastic_greedy(num_tickets=100, freq=None, popularity_penalty=False, iterations=20000):
    """
    Stochastic greedy: sample many tickets, keep the best scoring ones.
    """
    best = []
    for _ in range(iterations):
        t = generate_ticket()
        s = ticket_score(t, freq=freq, popularity_penalty=popularity_penalty)
        if len(best) < num_tickets:
            best.append((s, t))
            best.sort(reverse=True)
        elif s > best[-1][0]:
            best[-1] = (s, t)
            best.sort(reverse=True)
    return [t for _, t in best]

if __name__ == "__main__":
    # Example usage without history
    print("=== Example tickets ===")
    tickets = stochastic_greedy(num_tickets=20)
    for t in tickets:
        print(t)
