import sys
import os
from Bio import SeqIO


def main(fasta):
    new_headers = set()
    new_fasta = os.path.splitext(os.path.basename(fasta))[0] + \
            '.reheadered.fasta'
    dup_fasta = os.path.splitext(os.path.basename(fasta))[0] + \
            '.reheadered.duplicates.fasta'
    new_fh = open(new_fasta, 'wt')
    dup_fh = open(dup_fasta, 'wt')
    for record in SeqIO.parse(fasta, 'fasta'):
        parts = record.description.split('/')[1:]
        if len(parts) < 3:
            raise ValueError("Not enough parts for record {}".format(
                record.description))
        if len(parts) > 3:
            raise ValueError("Too many parts for record {}".format(
                record.description))
        parts[2] = parts[2].split('|')[0]
        new_id = '/'.join(parts).replace(' ', '_')
        if new_id in new_headers:
            sys.stderr.write("Duplicate sequence ID: {}\n".format(new_id))
            SeqIO.write(record, dup_fh, "fasta")
        else:
            new_headers.add(new_id)
            record.id = new_id
            SeqIO.write(record, new_fh, "fasta")
    new_fh.close()
    dup_fh.close()
    sys.stderr.write("Finished - created de-duplicated and re-headered file " +
                     "{}\nSequences with duplicate sequence IDs in {}\n".format(
                         new_fasta, dup_fasta))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: {} msa.fasta".format(sys.argv[0]))
    main(sys.argv[1])
