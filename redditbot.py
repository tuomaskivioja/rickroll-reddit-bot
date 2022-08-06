import praw
from urllib.parse import quote_plus

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="DESCRIPTION",
    password="YOUR_PASSWORD",
    username="YOUR_USERNAME",
)


def evaluate_post(submission):
    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print(f"Replying to: {submission.title}")
            submission.reply(body=reply_text)
            print(f"Successfully Rick rolled {submission.title}")
            # A reply has been made so do not attempt to match other phrases.
            return True



QUESTIONS = ["How to", "Where to"] #add more here
REPLY_TEMPLATE = "This should have what you're looking for: https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"


subreddit = reddit.subreddit("CHOOSE_SUBREDDIT_NAME")
counter = 0
for submission in subreddit.stream.submissions():
    if evaluate_post(submission) == True:
        counter += 1
    if counter == 5:
        break
