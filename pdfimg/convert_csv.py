import csv
import sys

txt_file = r"/Users/Nehsus/Desktop/blazeIT/Final/delhi.txt"
csv_file = r"/Users/Nehsus/Desktop/blazeIT/Final/delhi.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\n')
out_csv = csv.writer(open(csv_file, "wb"))

out_csv.writerows(in_txt)

