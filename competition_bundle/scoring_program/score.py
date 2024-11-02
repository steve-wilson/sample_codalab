#!/usr/bin/env python

# Some libraries and options
import os
from sys import argv
import sys
import yaml
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

if __name__ == "__main__":

    # set up the directories
    input_dir = argv[1]
    output_dir = argv[2]
    print(input_dir, output_dir)
    print(os.listdir(input_dir))
    os.makedirs(output_dir, exist_ok=True)
    print(os.listdir(output_dir))
    res_dir = os.path.join(input_dir, 'res')
    ref_dir = os.path.join(input_dir, 'ref')
    print(os.listdir(res_dir))
    print(os.listdir(ref_dir), flush=True)


    # set the file paths
    score_file = os.path.join(output_dir, 'scores.txt')
    pred_file = os.path.join(input_dir, 'res', 'preds.txt')
    ground_truth_file = os.path.join(input_dir, 'ref', "labels.txt")

    print(score_file, pred_file, ground_truth_file)
    print("===",flush=True)
    sys.stdout.flush()

    with open("output2.txt",'w') as out:
        print(str(os.listdir(res_dir)))

    # load the data
    preds = [line.strip() for line in open(pred_file).readlines()]
    ground_truth = [line.strip() for line in open(ground_truth_file).readlines()]

    # compute the scores
    accuracy = accuracy_score(ground_truth, preds)
    precision = precision_score(ground_truth, preds, pos_label='yes')
    recall = recall_score(ground_truth, preds, pos_label='yes')
    f1 = f1_score(ground_truth, preds, pos_label='yes')

    # write the reuslts
    results = f"accuracy: {accuracy}\nprecision: {precision}\nrecall: {recall}\nf1-score: {f1}"
    with open(score_file,'w') as score_fh:
        score_fh.write(results)