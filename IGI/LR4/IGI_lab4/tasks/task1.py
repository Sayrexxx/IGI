import csv
import pickle


class DataProcessor:
    """
    Class for serializing, deserializing, searching, and sorting data using different formats.
    """

    def __init__(self, data):
        """
        Initializes a DataProcessor object.

        Args:
            data (dict): The data to be processed.
        """
        self.data = data

    def serialize_to_csv(self, filename):
        """
        Serializes data to a CSV file.

        Args:
            filename (str): The name of the CSV file.

        Returns:
            None
        """
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in self.data.items():
                writer.writerow([key, value])

    @staticmethod
    def deserialize_from_csv(filename):
        """
        Deserializes data from a CSV file.

        Args:
            filename (str): The name of the CSV file.

        Returns:
            dict: The deserialized data.
        """
        data = {}
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                key, value = row
                data[key] = value
        return data

    def serialize_with_pickle(self, filename):
        """
        Serializes data using the pickle module.

        Args:
            filename (str): The name of the pickle file.

        Returns:
            None
        """
        with open(filename, 'wb') as picklefile:
            pickle.dump(self.data, picklefile)

    @staticmethod
    def deserialize_with_pickle(filename):
        """
        Deserializes data from a pickle file.

        Args:
            filename (str): The name of the pickle file.

        Returns:
            dict: The deserialized data.
        """
        with open(filename, 'rb') as picklefile:
            data = pickle.load(picklefile)
        return data

    def search_data(self, key):
        """
        Searches for a value in the data based on the provided key.

        Args:
            key (str): The key to search for.

        Returns:
            str: The value corresponding to the key, or None if the key is not found.
        """
        return self.data.get(key)

    def sort_data(self, reverse=False):
        """
        Sorts the data based on the keys.

        Args:
            reverse (bool, optional): Whether to sort in reverse order. Defaults to False.

        Returns:
            dict: The sorted data.
        """
        sorted_data = dict(sorted(self.data.items(), key=lambda x: x[0], reverse=reverse))
        return sorted_data

    def calculate_success_percentage(self):
        """
        Calculates the success percentage for the class.

        Returns:
            float: The success percentage.
        """
        total_students = len(self.data)
        successful_students = 0
        for student in self.data.values():
            total_marks = sum(student['grades'])
            average_marks = total_marks / len(student['grades'])
            if average_marks >= 60:
                successful_students += 1

        success_percentage = (successful_students / total_students) * 100
        return success_percentage

    def get_low_achievers(self):
        """
        Retrieves a list of low-achieving students.

        Returns:
            list: The list of low-achieving students.
        """
        low_achievers = []
        for student, data in self.data.items():
            total_marks = sum(data['grades'])
            average_marks = total_marks / len(data['grades'])
            if average_marks < 40:
                low_achievers.append(student)
        return low_achievers

    def get_high_achievers(self):
        """
        Retrieves a list of high-achieving students.

        Returns:
            list: The list of high-achieving students.
        """
        high_achievers = []
        for student, data in self.data.items():
            total_marks = sum(data['grades'])
            average_marks = total_marks / len(data['grades'])
            if average_marks >= 90:
                high_achievers.append(student)
        return high_achievers

    def get_student_info(self, student_name):
        """
        Retrieves information about a specific student.

        Args:
            student_name (str): The name of the student.

        Returns:
            dict: Information about the student, including their grades.
        """
        return self.data.get(student_name, {})


def task1():
    # Создаем словарь с данными об учениках
    students = {
        'John Doe': {'grades': [85, 90, 92]},
        'Jane Smith': {'grades': [20, 40, 35]},
        'David Johnson': {'grades': [92, 88, 95]},
        'Emily Davis': {'grades': [70, 65, 68]},
        'Michael Brown': {'grades': [95, 92, 98]},
        'Sarah Wilson': {'grades': [31, 22, 15]},
        'Robert Anderson': {'grades': [75, 78, 80]},
        'Jessica Thompson': {'grades': [90, 92, 95]},
        'Andrew Martinez': {'grades': [85, 88, 90]},
        'Olivia Davis': {'grades': [95, 98, 92]}
    }

    # Создаем объект DataProcessor
    processor = DataProcessor(students)

    while True:
        print("Меню:")
        print("1. Расчет процента успеваемости в классе за год")
        print("2. Формирование списка неуспевающих")
        print("3. Формирование списка отличников")
        print("4. Получение информации о школьнике по его имени")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            # Расчет процента успеваемости
            success_percentage = processor.calculate_success_percentage()
            print(f"Процент успеваемости: {success_percentage}%")
        elif choice == "2":
            # Формирование списка неуспевающих
            low_achievers = processor.get_low_achievers()
            print("Список неуспевающих:", low_achievers)
        elif choice == "3":
            # Формирование списка отличников
            high_achievers = processor.get_high_achievers()
            print("Список отличников:", high_achievers)
        elif choice == "4":
            # Получение информации о школьнике
            student_name = input("Введите имя ученика: ")
            student_info = processor.get_student_info(student_name)
            if student_info:
                print("Информация о школьнике:")
                print("Имя:", student_name)
                print("Оценки:", student_info.get('grades'))
            else:
                print("Ученик не найден.")
        elif choice == "0":
            # Выход из программы
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
