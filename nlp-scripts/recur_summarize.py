import sys
from functools import reduce
from nltk.tokenize import sent_tokenize
import simple_sum as simsum


OUT_SEN_COUNT = 10
IN_SEN_COUNT = 50


# Also stolen from the interwebs
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def read_file(text_file):
    with open(text_file) as tf:
        return tf.read()


def should_end(text_sents):
    sentence_count = len(text_sents)
    limit = OUT_SEN_COUNT
    print("Text has", sentence_count, "sentences.")
    print("The limit is", limit)
    should_stop = sentence_count <= limit
    if should_stop:
        print("Stopping")
    else:
        print("Continuing")
    return should_stop


def join_sents(s1, s2):
    return s1 + " " + s2


def recur_summarize(sum_fun, text, recur_count = 0):
    print("\nRecurred", recur_count, "times\n")
    text_sents = sent_tokenize(text)
    if should_end(text_sents):
        return text

    sen_chunks = chunks(text_sents, IN_SEN_COUNT)
    sum_chunks = []

    for sen_chunk in sen_chunks:
        temp_text = reduce(join_sents, sen_chunk.copy())
        temp_sum = temp_text
        if len(sen_chunk) >= OUT_SEN_COUNT: # We have to check that the input has >= sentences as the output
            temp_sum = sum_fun(temp_text)
        sum_chunks.append(temp_sum)

    joined_sum = reduce(join_sents, sum_chunks)
    return recur_summarize(sum_fun, joined_sum, recur_count + 1)



if __name__ == "__main__":
    text_file = sys.argv[1]
    print("Recursively summarizing", text_file, "\n\n")

    fs = simsum.FrequencySummarizer()
    text = read_file(text_file)

    def sf(text):
        summary = fs.summarize(text, OUT_SEN_COUNT)
        return reduce(join_sents, summary)

    summary = recur_summarize(sf, text)

    print_width = 50
    print("\n" + print_width*"#")
    print("THE SUMMARY".center(print_width))
    print(print_width*"#", "\n\n")
    print(summary)

    output_fname = "summary_" + text_file.split("/")[-1]
    with open(output_fname, mode="w") as sf:
        sf.write(summary)
