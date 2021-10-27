#Alex Zee, subsampling chip illumina data.
import sys
import mappy as mm
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i1', '--input_file_1')
parser.add_argument('-i2', '--input_file_2')
parser.add_argument('-s', '--subSample_Count', type=int)
args = parser.parse_args()

file1 = args.input_file_1
file2 = args.input_file_2
sample_Count = args.subSample_Count

total_len = 0
for read in mm.fastx_read(file1, read_comment=False):
    total_len += 1

indexes = set(np.random.choice(range(total_len), size=sample_Count, replace=False))

subSample1, subSample2 = open("INPUT_subSample1_final.fastq", "w"), open("INPUT_subSample2_final.fastq", "w")

curr_idx = 0
for read1, read2 in zip(mm.fastx_read(file1, read_comment=False), mm.fastx_read(file2, read_comment=False)):
    if curr_idx in indexes:
        print(f'@{read1[0]}\n{read1[1]}\n+\n{read1[2]}', file=subSample1)
        print(f'@{read2[0]}\n{read2[1]}\n+\n{read2[2]}', file=subSample2)
    curr_idx += 1

subSample1.close()
subSample2.close()