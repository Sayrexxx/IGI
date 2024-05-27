import re
import zipfile


class TextAnalyzer:
    """
    The TextAnalyzer class analyzes a text file and provides various statistics about the text.
    """

    def __init__(self, input_file, output_file):
        """
        Initializes a new instance of the TextAnalyzer class.

        Args:
            input_file (str): The path to the input file.
            output_file (str): The path to the output file.
        """
        self.input_file = input_file
        self.output_file = output_file

    def analyze_text(self):
        """
        Analyzes the text from the input file and writes the statistics to the output file.
        """
        with open(self.input_file, 'r') as file:
            text = file.read()

        sentences = re.split('[.!?]', text)
        num_sentences = len(sentences)

        num_narrative = len(re.findall('[^.!?]+', text))
        num_interrogative = len(re.findall('\?[^\?]+', text))
        num_imperative = len(re.findall('![^!]+', text))

        total_length = sum(len(sentence.split()) for sentence in sentences)
        avg_sentence_length = total_length / num_sentences

        words = re.findall('\w+', text)
        total_word_length = sum(len(word) for word in words)
        avg_word_length = total_word_length / len(words)

        num_smileys = len(re.findall('[:;]-*[\(\)\[\]]+', text))

        with open(self.output_file, 'w') as file:
            file.write(f"Number of sentences in the text: {num_sentences}\n")
            file.write(f"Number of narrative sentences: {num_narrative}\n")
            file.write(f"Number of interrogative sentences: {num_interrogative}\n")
            file.write(f"Number of imperative sentences: {num_imperative}\n")
            file.write(f"Average sentence length in characters: {avg_sentence_length}\n")
            file.write(f"Average word length in characters: {avg_word_length}\n")
            file.write(f"Number of smileys in the text: {num_smileys}\n")

        with zipfile.ZipFile('results.zip', 'w') as zip_file:
            zip_file.write(self.output_file, arcname='results.txt')


# Example usage of the TextAnalyzer class

def task2():
    analyzer = TextAnalyzer('/home/sayrex/PycharmProjects/IGI_lab4/tasks/input.txt', 'output.txt')
    analyzer.analyze_text()