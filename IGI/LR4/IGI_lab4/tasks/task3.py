import math
import matplotlib.pyplot as plt
import numpy as np

class FunctionAnalyzer:
    """
    The FunctionAnalyzer class analyzes a function by calculating its power series expansion and providing additional statistics.
    """

    def __init__(self, x, eps):
        """
        Initializes a new instance of the FunctionAnalyzer class.

        Args:
            x (float): The value of the argument x.
            eps (float): The precision of calculations.
        """
        self.x = x
        self.eps = eps
        self.n = 0
        self.f_x = 0
        self.math_f_x = math.log(1 + x)

    def power_series(self):
        """
        Calculates the power series expansion of the function.

        Returns:
            float: The value of the function calculated using the power series expansion.
        """
        result = 0
        for i in range(1, self.n + 1):
            result += (-1) ** (i - 1) * (self.x ** i) / i
        return result

    def calculate_function(self):
        """
        Calculates the value of the function and additional statistics.
        """
        while True:
            self.n += 1
            self.f_x = self.power_series()
            if abs(self.f_x - self.math_f_x) < self.eps or self.n >= 500:
                break

    def calculate_statistics(self):
        """
        Calculates additional statistics of the function.

        Returns:
            dict: A dictionary containing the calculated statistics.
        """
        sequence = [(-1) ** (i - 1) * (self.x ** i) / i for i in range(1, self.n + 1)]
        mean = sum(sequence) / len(sequence)
        median = np.median(sequence)
        mode = max(set(sequence), key=sequence.count)
        variance = np.var(sequence)
        std_deviation = np.std(sequence)
        statistics = {
            'mean': mean,
            'median': median,
            'mode': mode,
            'variance': variance,
            'std_deviation': std_deviation
        }
        return statistics

    def plot_graphs(self):
        """
        Plots the graphs of the power series and the corresponding function.
        """
        n_values = range(1, self.n + 1)
        f_x_values = [self.power_series() for _ in n_values]
        math_f_x_values = [self.math_f_x] * len(n_values)

        plt.plot(n_values, f_x_values, label="Power Series")
        plt.plot(n_values, math_f_x_values, label="Math Function")
        plt.xlabel('n')
        plt.ylabel('F(x)')
        plt.legend()
        plt.grid(True)
        plt.title('Power Series Expansion vs Math Function')
        plt.savefig('graph.png')
        plt.show()


def task3():
    def test_function():
        x = float(input("Enter the value of x: "))
        eps = float(input("Enter the precision (eps): "))

        analyzer = FunctionAnalyzer(x, eps)
        analyzer.calculate_function()

        statistics = analyzer.calculate_statistics()

        print("x\t n\t F(x)\t\t Math F(x)\t eps")
        print("{}\t {}\t {}\t {}\t {}".format(x, analyzer.n, analyzer.f_x, analyzer.math_f_x, eps))

        print("\nAdditional Statistics:")
        for key, value in statistics.items():
            print("{}: {}".format(key.capitalize(), value))

        analyzer.plot_graphs()


    def repeat_program():
        while True:
            test_function()
            choice = input("Do you want to run the program again? (y/n): ")
            if choice.lower() != "y":
                break

    def exception_handler(func):
        def wrapper():
            try:
                func()
            except Exception as e:
                print("An error occurred: {}".format(str(e)))
                wrapper()

        return wrapper

    @exception_handler
    def task():
        repeat_program()

    task()