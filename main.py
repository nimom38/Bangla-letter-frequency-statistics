import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

freq = {}


def read_file(filename='corpora.txt'):
    f = open(filename, "r", encoding="utf-8")
    for character in f.read():
        if (character in freq):
            freq[character] += 1
        else:
            freq[character] = 1


def main():
    read_file()

    bangla_alphabets = 'অআ াই িঈ ীউ ুঊ ূঋ ৃএ েঐ ৈও োঔ ৌকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎংঃ'
    bangla_alphabets = "".join(bangla_alphabets.split())
    sorted_counts = []

    for character in bangla_alphabets:
        if character in freq:
            sorted_counts.append(freq[character])
        else:
            sorted_counts.append(0)

    total_count = 0

    for value in sorted_counts:
        total_count += value

    sorted_counts = [100 * value / total_count for value in sorted_counts]

    fig, ax = plt.subplots(figsize=(40, 20))
    prop = fm.FontProperties(fname='kalpurush.ttf')
    ax.legend(prop=prop)

    font_dirs = ['./', ]
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    font_list = fm.createFontList(font_files)
    fm.fontManager.ttflist.extend(font_list)
    plt.tick_params(labelsize=20)

    plt.bar(range(len(bangla_alphabets)), sorted_counts, align='center')
    plt.xticks(np.arange(len(bangla_alphabets)),
               list(bangla_alphabets), fontfamily='Kalpurush')

    plt.xlabel('বর্ণ-সমূহ', fontsize=24, fontfamily='Kalpurush')
    plt.ylabel('শতকরা-হার (%)', fontsize=24, fontfamily='Kalpurush')

    fig.suptitle(
        'Relative Frequencies of letters in Bengali text\nCreated by Gazi Mohaimin Iqbal', fontsize=18)

    plt.show()


if __name__ == "__main__":
    main()
