/* 
This was made using Chat_GPT, i don't know code in C

In the script, the calculateSimilarity function takes a string and an
array of values, along with the number of values (numValues). It calculates
the similarity between each value and the string using the following steps:

It initializes a variable similaritySum to keep track of the sum of similarities.
It iterates over each value in the array using a for loop.
For each value, it compares the characters of the string and the value
one by one and counts the number of matching characters.
It calculates the similarity as the ratio of matching characters to
the length of the longer string.
It adds the similarity to similaritySum.
After processing all the values, it calculates the average similarity
by dividing similaritySum by the number of values.
The average similarity is returned by the function.
In the main function, an example usage is shown where string is set
to "example", and values is an array of three example values.
The calculateSimilarity function is called with these values, and
 the average similarity is printed.
Please note that this script calculates similarity based on the ratio
of matching characters, which is a simple approach. Depending on your
 requirements, you might want to consider using more sophisticated
  algorithms for string similarity, such as Levenshtein distance or cosine similarity.
*/


#include <stdio.h>
#include <string.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Insufficient arguments.\n");
        return 1;
    }

    // Get the target word
    const char* target_word = argv[1];

    #pragma omp parallel for
    for (int i = 2; i < argc; i++) {
        const char* current_word = argv[i];

        int target_word_length = strlen(target_word);
        int current_word_length = strlen(current_word);

        int max_length = (target_word_length > current_word_length) ? target_word_length : current_word_length;
        int min_length = (target_word_length < current_word_length) ? target_word_length : current_word_length;

        int matching_characters = 0;
        for (int j = 0; j < min_length; j++) {
            if (target_word[j] == current_word[j]) {
                matching_characters++;
            }
        }

        float similarity = (float)matching_characters / max_length;
        printf("%f ", similarity);
    }

    printf("\n");
    return 0;
}

