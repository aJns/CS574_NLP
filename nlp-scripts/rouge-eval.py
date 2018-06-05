from pythonrouge.pythonrouge import Pythonrouge


data_dir = "../project-data/the_Alchemist"
summary_filenames = [
        "cliffsnotes_alchemist.txt",
        "gradesaver_alchemist.txt",
        "sparknotes_alchemist.txt",
        ]

summaries = []
for fn in summary_filenames:
    with open(data_dir + "/" + fn) as sum_f:
        temp_sum = sum_f.read()
        summaries.append(temp_sum)

for i in range(len(summaries)):
    # system summary(predict) & reference summary
    summary = [[ summaries[i] ]]
    references = [[ summaries[i+1:] + summaries[:i] ]]

    # initialize setting of ROUGE to eval ROUGE-1, 2, SU4
    # if you evaluate ROUGE by sentence list as above, set summary_file_exist=False
    # if recall_only=True, you can get recall scores of ROUGE
    rouge = Pythonrouge(summary_file_exist=False,
                        summary=summary, reference=references,
                        n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
                        recall_only=True, stemming=True, stopwords=True,
                        word_level=True, length_limit=True, length=50,
                        use_cf=False, cf=95, scoring_formula='average',
                        resampling=True, samples=1000, favor=True, p=0.5)
    score = rouge.calc_score()
    print(summary_filenames[i], score)
