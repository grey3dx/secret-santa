from participants import read_participants
from preprocess import initialize_dicts, create_object_list
from generator import secret_santa
from email_client import fire_emails

# from email_client import *

responses = "responses_2024_test.csv"

def main():
    participants = read_participants(responses)

    ss_map = {}
    while (not ss_map):
        try:
            potentials = initialize_dicts(participants)
            ss_map = secret_santa(potentials)
        except:
            pass

    ss_tuples = create_object_list(participants, ss_map)
    print(ss_tuples)

    fire_emails(ss_tuples)


if __name__ == "__main__":
    main()
