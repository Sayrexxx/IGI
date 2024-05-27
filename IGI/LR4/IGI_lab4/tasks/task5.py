import numpy as np


class NumPyOperations:
    """
        The NumPyOperations represents some functions of numpy package.
    """
    def __init__(self, n, m):
        """
        Initialize the NumPyOperations class.

        Args:
            n (int): Number of rows.
            m (int): Number of columns.
        """
        self.n = n
        self.m = m
        self.matrix = None

    def generate_matrix(self):
        """
        Generate a random integer matrix of size (n, m).

        Returns:
            numpy.ndarray: Generated matrix.
        """
        self.matrix = np.random.randint(0, 10, size=(self.n, self.m))
        return self.matrix

    def sort_matrix_by_last_column(self):
        """
        Sort the matrix by the elements in the last column in descending order.

        Returns:
            numpy.ndarray: Sorted matrix.
        """
        sorted_matrix = self.matrix[self.matrix[:, -1].argsort()][::-1]
        return sorted_matrix

    def calculate_mean_last_column(self):
        """
        Calculate the mean value of the elements in the last column.

        Returns:
            float: Mean value of the last column.
        """
        mean_value = np.mean(self.matrix[:, -1])
        return round(mean_value, 2)

    def calculate_mean_last_column_custom(self):
        """
        Calculate the mean value of the elements in the last column using a custom formula.

        Returns:
            float: Mean value of the last column.
        """
        column = self.matrix[:, -1]
        mean_value = column.sum() / len(column)
        return round(mean_value, 2)

    def perform_mathematical_operations(self):
        """
        Perform mathematical and statistical operations on the matrix.

        Returns:
            tuple: Mean, median, correlation, variance, and standard deviation.
        """
        mean = np.mean(self.matrix)
        median = np.median(self.matrix)
        correlation = np.corrcoef(self.matrix[:, 0], self.matrix[:, 1])
        variance = np.var(self.matrix)
        std_deviation = np.std(self.matrix)

        return mean, median, correlation, variance, std_deviation


def task5():
    """
    Main function to interact with the user.
    """
    while True:
        try:
            n = int(input("Enter the number of rows: "))
            m = int(input("Enter the number of columns: "))

            numpy_ops = NumPyOperations(n, m)
            matrix = numpy_ops.generate_matrix()

            sorted_matrix = numpy_ops.sort_matrix_by_last_column()
            print("Sorted matrix:")
            print(sorted_matrix)

            mean_value_standard = numpy_ops.calculate_mean_last_column()
            mean_value_custom = numpy_ops.calculate_mean_last_column_custom()
            print("Mean value (standard):", mean_value_standard)
            print("Mean value (custom):", mean_value_custom)

            mean, median, correlation, variance, std_deviation = numpy_ops.perform_mathematical_operations()
            print("Mean:", mean)
            print("Median:", median)
            print("Correlation:", correlation)
            print("Variance:", variance)
            print("Standard Deviation:", std_deviation)

            choice = input("Do you want to perform another operation? (y/n): ")
            if choice.lower() != "y":
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        except Exception as e:
            print("An error occurred:", str(e))