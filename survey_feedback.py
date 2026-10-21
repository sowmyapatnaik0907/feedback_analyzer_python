
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],
    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter feedback details")

    name = input("Enter name: ")
    feedback = input("Enter written feedback: ")

    rating = int(input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nNew feedbacks added successfully!")

for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text = ' '.join(text.split())
    text = text.lower()

    feedback_data['Feedback'][i] = text

print("\nFeedback cleaned successfully!")

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.split():
            count += 1

    return count


print("\nWord Count Insights")
print("Good:", count_word_in_feedbacks("good"))
print("Poor:", count_word_in_feedbacks("poor"))
print("Excellent:", count_word_in_feedbacks("excellent"))

total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))

longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda text: len(text.split())
)

print("\nLongest Feedback:")
print(longest_feedback)
print("Word Count:", len(longest_feedback.split()))

unique_words = set()

for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        unique_words.add(word)

print("\nUnique Words:")
print(sorted(unique_words))

print("\nFinal Cleaned Feedback Data:")
print(feedback_data)

print("\nFeedbacks Sorted by Rating:")

sorted_feedbacks = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda item: item[3],
    reverse=True
)

for entry in sorted_feedbacks:
    print(entry)
