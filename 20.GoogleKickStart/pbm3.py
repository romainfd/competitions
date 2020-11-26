# import matplotlib.pyplot as plt
import numpy as np

def cost_to_move_to(target, initial_wheels, N):
    cost = 0
    for wheel in initial_wheels:
        dist = abs(wheel - target)
        cost += min(dist, N - dist)
    return cost


def best_mean(wheels, W, N):
    std_normal = np.std(wheels)
    std_wrapping_top = np.std([wheel - N if wheel > N // 2 else wheel for wheel in wheels])
    std_wrapping_bottom = np.std([wheel + N if wheel < N // 2 else wheel for wheel in wheels])
    best_std = min(std_normal, std_wrapping_top, std_wrapping_bottom)
    if abs(std_normal - best_std) < 0.001:
        return np.mean(wheels), wheels
    if abs(std_wrapping_top - best_std) < 0.001:
        return np.mean([wheel - N if wheel > N // 2 else wheel for wheel in wheels]), [
            wheel - N if wheel > N // 2 else wheel for wheel in wheels]
    return np.mean([wheel + N if wheel < N // 2 else wheel for wheel in wheels]), [
        wheel + N if wheel < N // 2 else wheel for wheel in wheels]


def optimal(W, N, wheels):
    # We perform a Metropolis like algorithm : moving slowly to the optimal position
    # We update all wheels which can give a strictly better solution (strictly shorter path) based on current solution
    updated_faces = 1
    while updated_faces > 0:
        # what would be the best target with the current wheel positions
        mean, wheels = best_mean(wheels, W, N)
        mean = round(mean)
        # Update wheels to find local minimum (which is global based on shape of the problem) (based on plots in test cases but is it really the case? Based on dichotomy approach on derivative not working, it might be wrong...)
        updated_faces = 0
        for pos, wheel_face in enumerate(wheels):
            if wheel_face - mean > N // 2:
                wheels[pos] -= N
                updated_faces += 1
            elif wheel_face - mean < - N // 2:
                wheels[pos] += N
                updated_faces += 1
    optimal_moves_count = cost_to_move_to(round(sum(wheels) / W), wheels, N)
    print("Case #" + str(case + 1) + ": " + str(optimal_moves_count))


def small_N(W, N, wheels):
    costs = []
    for target in range(N):
        costs.append(cost_to_move_to(target, wheels, N))
    # plt.plot(costs)
    # plt.show()
    # from numpy import diff
    # print(diff(costs))
    # plt.plot(diff(costs))
    # plt.show()
    print("Case #" + str(case + 1) + ": " + str(min(costs)))


def minimal_search(W, N, wheels):
    # Moving through values to get minimum
    a, b = dichotomy(W, N, wheels)
    # a has negative derivative and b has positive one
    if a < b:
        # we have a minimum in b
        min_cost = find_around(b, wheels, N)
    elif a > b:
        # we have a maximum in b
        min_cost = find_around(b + N // 2, wheels, N)
    else:
        min_cost = min(
            find_around(b, wheels, N),
            find_around(b + N // 2, wheels, N)
        )
    print("Case #" + str(case + 1) + ": " + str(min_cost))


def find_around(target, wheels, N):
    return min(
        cost_to_move_to(target % N, wheels, N),
        cost_to_move_to((target - 1) % N, wheels, N),
        cost_to_move_to((target + 1) % N, wheels, N)
    )


def dichotomy(W, N, wheels):
    # Find the point on which the derivative is 0
    # Looks only in a [0, N/2] window to find an optimum and then checks if it's min or max
    def derivative(target):
        return cost_to_move_to(target + 1, wheels, N) - cost_to_move_to(target, wheels, N)
    a = 0
    b = N // 2
    if derivative(a) > derivative(b):
        a, b = b, a
    while abs(b - a) > 1:
        m = (a + b) // 2
        value = derivative(m)
        if value == 0:
            return m, m
        elif value > 0:
            b = m
        else:
            a = m
    return a, b


nb_cases = int(input())
for case in range(nb_cases):
    W, N = map(int, input().split(" "))
    wheels = list(map(lambda w: int(w) - 1, input().split(" ")))
    # BENCHMARK (we know it's correct)
    small_N(W, N, wheels)
    optimal(W, N, wheels)
