import csv

with open("Names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("New emails.csv", "w", newline="") as new_emails:
        csv_writer = csv.writer(new_emails)

        for line in csv_reader:
            email = "".join(line[2:])
            csv_writer.writerow([email])