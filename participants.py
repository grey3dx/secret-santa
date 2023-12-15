import csv

class SecretSantaParticipant:
    def __init__(self, timestamp, username, name, email, address, phone, comments):
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone_number = phone
        self.comments = comments

    def get_username(self):
        return self.username

    def __str__(self):
        return f"{self.name} ({self.email})"

def read_participants(file_path):
    participants = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Assuming the first row contains headers

            for row in reader:
                if len(row) == len(headers):  # Ensure the number of columns match headers
                    participant_data = dict(zip(headers, row))
                    participant = SecretSantaParticipant(**participant_data)
                    participants.append(participant)
                else:
                    print(f"Skipping row {row} as it doesn't match the expected format.")

        return participants

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    csv_file_path = 'responses.csv'
    secret_santa_participants = read_participants(csv_file_path)

    for participant in secret_santa_participants:
        print(participant)