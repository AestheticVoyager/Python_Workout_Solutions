# DomirScire

import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd:
        open(csv_filename, 'w') as output:
            inline = csv.reader(passwd, delimiter=':')
            outfile = csv.writer(ouput, delimiter="\t")
            for record in infile:
                if len(record) > 1:
                    outfile.writerow((record[0], record[2]))

if __name__ == "__main__":
    passwd_to_csv(passwd_filename, csv_filename)
