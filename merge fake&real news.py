import csv


def merge_fake_and_real(fake_file, real_file, output_file):
    with open(fake_file, 'r') as fake_news, open(real_file, 'r') as real_news, open(output_file, 'w',
                                                                                    newline='') as outfile:
        fake_reader = csv.reader(fake_news)
        real_reader = csv.reader(real_news)
        writer = csv.writer(outfile)

        writer.writerow(['news_name', 'label'])

        for fake_row in fake_reader:
            writer.writerow([fake_row[0], '0'])

        for real_row in real_reader:
            writer.writerow([real_row[0], '1'])


merge_fake_and_real('news_names.csv', 'Authentic_news_names.csv', 'noutput.csv')