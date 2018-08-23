import jieba
import numpy
import json
import os

data_train_raw = 'data/data_train_raw.txt'
finance_dict = 'data/user_dict.txt'

jieba.load_userdict(open(finance_dict, 'r', encoding='utf-8'))


def segment_json(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        data_set = []
        for lidx, line in enumerate(fin):
            sample = json.loads(line.strip())
            data_set.append(sample)

    for sample in data_set:
        sample['segmented_question'] = list(jieba.cut(sample['question']))
        for doc in sample['documents']:
            doc['segmented_title'] = list(jieba.cut(doc['title']))
            segmented_paragraphs = []
            for para in doc['paragraphs']:
                segmented_paragraphs.append(list(jieba.cut(para)))
            doc['segmented_paragraphs'] = segmented_paragraphs

        # segmented_answers = []
        # for answer in sample['answers']:
        #     segmented_answers.append(list(jieba.cut(answer)))
        # sample['segmented_answers'] = segmented_answers

    print(data_set[0])

    with open(filename + '.after', 'w', encoding='utf-8') as fout:
        for sample in data_set:
            json.dump(sample, fout, ensure_ascii=False)
            fout.write('\n')


if __name__ == '__main__':
    segment_json('data/data_dev.txt')
