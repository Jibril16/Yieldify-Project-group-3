import csv


def read_tsv(filename):
    """Function that reads a tsv file

    :param filename: Filename path (e.g. "campaigns-50.tsv")
    :type filename: str

    :return: list of rows in file. Each row is a list as well
    :rtype: list
    """
    data = []
    with open(filename, newline='') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


def simple_token(code):
    """Function that breaks string into tokens by splitting on white space

    :param code: Code to be split
    :type code: str

    :return: list of tokens
    :rtype: list
    """
    tokens = code.split('')
    return tokens


if __name__ == '__main__':
    data = read_tsv("campaigns-50.tsv")
    for line in data:
        (campaign_id, website_id, code) = line
        print(campaign_id, code)
        try:
            print(simple_token(code))
        except:
            print("Cannot create tokens")
