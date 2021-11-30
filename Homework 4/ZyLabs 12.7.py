# Ismael Diaz (PSID: 1846093)
# CIS 2348 Homework #4 ZyLabs 12.7

def fat_burning_heart_rate():
    heartrate = (220-age) * .70
    return heartrate


def get_age():
    age = int(input())
    if age > 75 or age < 18:
        raise ValueError("Invalid age.")
    else:
        return age


if __name__ == "__main__":
    try:
        age = get_age()
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.")
    else:
        print("Fat burning heart rate for a {} year-old: {:.1f} bpm".format(age, fat_burning_heart_rate()))
