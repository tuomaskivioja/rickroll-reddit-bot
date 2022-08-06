import praw
from urllib.parse import quote_plus

reddit = praw.Reddit(
    client_id="yAawAXpkNmFdw7H-yHQoDw",
    client_secret="DhuyrXlT3EvcXfmHEXHdB-fMgB9wDw",
    user_agent="A bot that tries to Rick Roll you v1.0",
    password="appleidishalloween",
    username="rickrollmelodies",
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



QUESTIONS = ["How to", "Where to"]
REPLY_TEMPLATE = "This should have what you're looking for: https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"


subreddit = reddit.subreddit("learnpython")
for submission in subreddit.stream.submissions():
    print(submission)
