import re

from processing.score_processor import process_scores
from generators.number_generator import generate_numbers
from file_utils.file_handler import save_emails


scores = [25, 40, 50, 80, 90]

result = process_scores(scores)

print(f"\nFinal Result: {result}")


print("\nIterator Example")

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


print("\nGenerator Example")

for num in generate_numbers():

    print(num)


print("\nRegex Example")

text = """
Contact us:
abc@gmail.com
test@yahoo.com
"""

emails = re.findall(
    r"\S+@\S+\.\S+",
    text
)

print("Emails Found:", emails)

save_emails(emails)