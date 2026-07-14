class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        weight = init

        for _ in range(iterations):
            der = 2 * weight
            weight = weight - learning_rate * der
        
        return round(weight, 5)
