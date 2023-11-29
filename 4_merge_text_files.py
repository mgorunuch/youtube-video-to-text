import os


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if not file.startswith('trans_part_output_'):
                continue
            yield file


start_part = 'trans_part_output_'
start_part_len = len(start_part)

end_part = '.mp3.txt'
end_part_len = len(end_part)

ints = []

for filename in get_files(os.path.join(os.getcwd(), 'tmp')):
    path = os.path.join(os.getcwd(), 'tmp', filename)
    ints.append(int(filename[start_part_len:-end_part_len]))


ints.sort()


output = open(os.path.join(os.getcwd(), 'tmp', 'transcript_full.txt'), "w+")
for partname in ints:
    filename = f"{start_part}{partname}{end_part}"
    filepath = os.path.join(os.getcwd(), 'tmp', filename)

    f = open(filepath, "r")
    output.write(f.read())
    f.close()

output.close()
