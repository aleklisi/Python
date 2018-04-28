import os


def file_len(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def read_file(fileName):
    with open(fileName) as f:
        lines = f.read().splitlines()
    return lines


def each_from_list_to_int(list):
    result = []
    for elem in list:
        try:
            result.append(int(elem))
        except ValueError:
            continue
        else:
            continue
    return result


def chunk_it(seq, num):
    avg = len(seq) / int(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def write_to_file(txt, filename):
    file = open(filename, "a")
    file.write(txt)
    file.close()


def listFiles(dirname):
    return os.listdir(dirname)


def get_output_filename(inputfileneme):
    return "dataAgg/agg" + inputfileneme


def aggregate_file(directory, infilename):
    dataStr = read_file(directory + "/" + infilename)
    dataInt = each_from_list_to_int(dataStr)
    dataChucked = chunk_it(dataInt, 24)
    outfilename = get_output_filename(infilename)
    i = 1;

    for chunk in dataChucked:
        aggregate = int(sum(chunk) / len(chunk))
        write_to_file(str(i) + "," + str(aggregate) + "\n", outfilename)
        i += 1


InDirectory = "data"
files = listFiles(InDirectory)
for file in files:
    aggregate_file(InDirectory, file)
