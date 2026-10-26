
import math

def alpha_beta(node, depth, maximizing_player, values, height, alpha, beta):
    # Base case: leaf node
    if depth == height:
        return values[node]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            val = alpha_beta(
                2 * node + i,
                depth + 1,
                False,
                values,
                height,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(
                2 * node + i,
                depth + 1,
                True,
                values,
                height,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-beta pruning
            if beta <= alpha:
                break

        return best


# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))

if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3

    result = alpha_beta(
        0, 0, True, values, height, -math.inf, math.inf
    )

    print("The optimal value is:", result)
