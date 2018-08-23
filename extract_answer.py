import json
import os

def extract_answer(filename):
    with open(filename,'r',encoding='utf-8') as fin:
        answers=[]
        answers_id=[]
        lines=fin.readlines()
        for line in lines:
            sample=json.loads(line)
            answers_id.append(sample['question_id'])
            if len(sample['answers'])==0:
                answer='\t'
            elif len(sample['answers'])==1:
                answer=sample['answers'][0]
            else:
                answer='.'.join(sample['answers'])

            answer=answer.strip()
            answers.append(answer)

    assert len(answers)==len(answers_id)

    with open(filename+'.extracted.csv','w',encoding='utf-8') as fout:
        for i in range(len(answers)):
            fout.write(str(answers_id[i]))
            fout.write('\t')
            fout.write(str(answers[i]))
            fout.write('\n')



if __name__ == '__main__':
    extract_answer('data/results/test.predicted.json')
