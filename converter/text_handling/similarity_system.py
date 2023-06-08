from os import path
from converter.models import Word
import subprocess
import math
import multiprocessing



class Similarity():
    @staticmethod
    def calculate_similarity(target_word, word_list):
        """
        This call a C file to sped up our work.

        In general we need a word_list which is all words learned stored in database
        and a target word whose we'll compare.

        The structure tend to run in that wall:
        target_word = 'banana'
        word_list = ['banana', 'apple', 'one']

        similarity = [0.8, 0.1, 0,2]

        return the higher value from similarity getting it in wordlist
        example:
            banana, because the banana has the value 0.8 which is the higher value from our list
        
        """
        batch_size = 100

        num_batches = math.ceil(len(word_list) / batch_size)
        similarity_scores = []

        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, len(word_list))
            batch = word_list[start_idx:end_idx]

            # Convert the target word and batch to bytes
            target_word_bytes = target_word.encode()
            word_list_bytes = [word.encode() for word in batch]

            # Execute the C program and pass the target word and batch as arguments
            C_PROGRAM_PATH = path.join(
                path.dirname(__file__),
                'workflows',
                'similarity_calculator'
            )
            args = [C_PROGRAM_PATH, target_word_bytes] + word_list_bytes

            try:
                # Run the C program
                result = subprocess.run(args, capture_output=True, text=True, check=True)
                
                # Get the output from the C program
                output = result.stdout.strip()
                batch_similarity_scores = list(map(float, output.split()))
                similarity_scores.extend(batch_similarity_scores)

            except subprocess.CalledProcessError as e:
                print(f"An error occurred while running the C program: {e.stderr}")
                return []

        return similarity_scores


class Database:
    """
    All our words from database
    """
    #Make 1000 rows process per each batch
    all_elements_object = list(Word.objects.values_list('word', flat=True))

    



class text_handling():
    def __init__(self):
        self.original_text = ''
        self.processed_text = []

    def get_nearest(self, word: str):
        """
        Get the word that best matches all database comparisons
        """
        list_similarity = Similarity.calculate_similarity(target_word=word, word_list=Database.all_elements_object)
        higher_value_index = list_similarity.index(max(list_similarity))

        return Database.all_elements_object[higher_value_index]

    def __main__(self, text: str):
        """
        The main function
        """

        self.original_text = text
        self.processed_text = self.original_text.split(' ')

        with multiprocessing.Pool() as pool:
            final_result = pool.map(self.get_nearest, self.processed_text)

        return ' '.join(final_result)
    

    





"""
Usage:

target_word = "example"
word_list = ["example1", "example2", "example3"]

similarity_scores = Similarity.calculate_similarity(target_word, word_list)
print(f"Similarity scores: {similarity_scores}")
"""




    