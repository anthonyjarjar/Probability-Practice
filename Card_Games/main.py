from blackjack import test_results

a, b, c = test_results(1000)

print(f"Player Wins: {a}\nHouse Wins: {b}")

if c != 0:
    print(f"Ties: {c}")
