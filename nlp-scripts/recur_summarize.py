import sys
import os.path
from functools import reduce
from nltk.tokenize import sent_tokenize, word_tokenize
import simple_sum as simsum
import txt_differences as txt_dif


OUT_SEN_COUNT = 45
IN_SEN_COUNT = 50
IMP_NOUN_WEIGHT = 1.5

FIN_SUM_WORD_COUNT = 1000


# Also stolen from the interwebs
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def read_file(text_file):
    with open(text_file, encoding="utf8") as tf:
        return tf.read()


def should_end(text):
    word_count = len(word_tokenize(text))
    sen_count = len(sent_tokenize(text))
    limit = FIN_SUM_WORD_COUNT
    print("Text has", sen_count, "sentences.")
    print("Text has", word_count, "words.")
    print("The limit is", limit)
    should_stop = word_count <= limit or sen_count == 1
    if should_stop:
        print("Stopping")
    else:
        print("Continuing")
    return should_stop


def join_sents(s1, s2):
    return s1 + " " + s2


def recur_summarize(sum_fun, text, output_sen_len = OUT_SEN_COUNT, recur_count = 0):
    print("\nRecurred", recur_count, "times\n")
    text_sents = sent_tokenize(text)
    if len(text_sents) <= output_sen_len:
        output_sen_len = output_sen_len - 1

    if should_end(text):
        return text

    sen_chunks = chunks(text_sents, IN_SEN_COUNT)
    sum_chunks = []

    for sen_chunk in sen_chunks:
        temp_text = reduce(join_sents, sen_chunk.copy())
        temp_sum = temp_text
        if len(sen_chunk) >= output_sen_len: # We have to check that the input has >= sentences as the output
            temp_sum = sum_fun(temp_text, output_sen_len)
        sum_chunks.append(temp_sum)

    joined_sum = reduce(join_sents, sum_chunks)
    return recur_summarize(sum_fun, joined_sum, output_sen_len, recur_count + 1)



if __name__ == "__main__":
    text_file = sys.argv[1]
    print("Recursively summarizing", text_file, "\n\n")

    fs = simsum.FrequencySummarizer()
    text = read_file(text_file)
    add_freq = txt_dif.get_noun_freqs(text)

    if IMP_NOUN_WEIGHT != 1:
        add_freq.update((k, v*IMP_NOUN_WEIGHT) for k, v in add_freq.items())

    def sf(text, output_sen_count=OUT_SEN_COUNT):
        summary = fs.summarize(text, output_sen_count, add_freq)
        return reduce(join_sents, summary)

    summary = recur_summarize(sf, text)

    print_width = 50
    print("\n" + print_width*"#")
    print("THE SUMMARY".center(print_width))
    print(print_width*"#", "\n\n")
    print(summary)


    split_path = os.path.split(text_file)
    output_fname = split_path[0] + os.path.sep + "sum" + os.path.sep + "our_summary_" + split_path[1]
    with open(output_fname, mode="w", encoding="utf8") as sf:
        sf.write(summary)
