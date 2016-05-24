import csv
import os


def parse_csv(filename):
    """ Open CSV file and convert data into dictionary list
    :param filename: string
    :return:
    """
    items = []

    if not os.path.isfile(filename):
        print('File with CSV does not exists')
        return items

    with open(filename) as raw:
        reader = csv.DictReader(raw)
        for row in reader:
            items.append(row)

    return items


if __name__ == '__main__':

    file = os.path.join(os.getcwd(), 'twitter_data_1463565798000_1463997798000.csv')
    t = parse_csv(file)
    print(t)
