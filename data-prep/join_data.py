import csv
import os

dir_in = '../exports'
dir_out = '../files'


fh_out = os.path.join(dir_out, 'tickets-gen-all.csv')

columns = [
    'number',
    'created',
    'caller',
    'opened_at',
    'opened_by',
    'priority',
    'state',
    'category',
    'subcategory',
    'assignment_group',
    'bpl_location',
    'nyp_locaiton',
    'resolved',
    'assigned_to',
    'system',
    'closed_at',
    'closed_by',
    'mat_source',
    'reassignment_count',
    'reopen_count',
    'resolved_by',
    'updated_on',
    'updated_by'
]


def save2csv(fh, row):
    with open(fh, 'a') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=',', quotechar='"',
            quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(row)


def content_reader(fh):
    with open(fh, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip header
        next(reader)

        for row in reader:
            yield row


if __name__ == '__main__':
    # create header in out file
    save2csv(fh_out, columns)

    for file in os.listdir(dir_in):
        reader = content_reader(os.path.join(dir_in, file))
        for row in reader:
            save2csv(fh_out, row)
