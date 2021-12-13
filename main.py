import csv
from faker import Faker


def fake_phonebook(records, headers):
    fake = Faker('nl_NL')
    with open("phonebook.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                "firstName": fake.first_name(),
                "surname": fake.last_name(),
                "preposition": fake.word(),
                "companyName": fake.company(),
                "department": fake.bs(),
                "title": fake.job(),
                "faxNr": fake.phone_number(),
                "emailAddress": fake.email(),
                "extension": fake.random_int(),
                "mobileNr": fake.phone_number(),
                "landLineNr": fake.phone_number(),
                "isPrivate": "false",
                "ownerUserId": fake.uuid4()
            })


if __name__ == '__main__':
    records = 50000
    headers = ["firstName", "surname", "preposition", "companyName", "department", "title", "faxNr", "emailAddress",
               "extension", "mobileNr", "landLineNr", "isPrivate", "ownerUserId"]
    fake_phonebook(records, headers)
    print(f"{records} made up contacts were written to file")
