import requests
import datetime
import oauth
import os
from pmaw import PushshiftAPI

def try_conn(token):
    headers = {"User-Agent": "de-medium 0.1", "Authorization":"Bearer "+token} 
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    return(response.json())

def get_posts(subreddit):
    api = PushshiftAPI(num_workers=os.cpu_count()*5)
    gen = api.search_submissions(after='2d',
                                  before='1d',
                                  subreddit=subreddit,
                                  )
    return list(gen)

if __name__ == "__main__":
    #token = oauth.get_token()
    #posts = try_conn(token=token)
    #print(posts)
    subreddit = 'mexico'
    posts = get_posts(subreddit)
    post_lists = [{"title":post["title"],"selftext":post["selftext"],"link_flair_text":post["link_flair_text"],"author":post["author"],"created_utc":post["created_utc"]} for post in posts]
    for p in post_lists:
        print(p)
        print()