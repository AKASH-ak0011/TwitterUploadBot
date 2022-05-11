import tweepy
import pandas as pd
import gspread
import os
import requests

# from oauth2client.service_account import ServiceAccountCredentials


BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAJ5QaQEAAAAAvJtgzTrjwFpHV0W5tFJlgWJo0RI%3Dpb92Gt9l8nycOKcoElMweUuK77CnObDrRsuEpNkorChtPzAy52'

def connect_to_twitter():
    bearer_token = os.environ.get('BEARER_TOKEN')
    return {"Authorization": "Bearer {}".format(bearer_token)}


    def make_request(headers):
        url = "https://twitter.com/home"#"https://api.twitter.com/2/tweets"
        params = {
            "tweet.fields": "author_id,created_at,lang",
            "ids": "21,1293593516040269825,1334542969530183683",
        }
    return requests.request("GET", url, headers=headers, params=params).json()

    {"data":[{"created_at":"2006-03-21T20:51:43.000Z","author_id":"13","text":"just setting up my twttr","id":"21","lang":"en"},{"created_at":"2020-08-12T17:01:42.000Z","author_id":"2244994945","text":"It’s finally here! \uD83E\uDD41 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8","id":"1293593516040269825","lang":"en"},{"created_at":"2020-12-03T17:00:13.000Z","author_id":"783214","text":"2020 in one word","id":"1334542969530183683","lang":"en"}]}

def authenticate_to_google():
    scope = [
        "https://spreadsheets.google.com/posts"
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "https://docs.google.com/spreadsheets/d/1tt_QviU15TMMQYS3W8BYuBMSp0R8xuuOrquHV4d2JiU/edit?usp=sharing", scope
    )
    return credentials




def main():
    headers = connect_to_twitter()
    response = make_request(headers)
    df = make_df(response)
    credentials = authenticate_to_google()
    gc = gspread.authorize(credentials)
    workbook = gc.open_by_key("posts")
    sheet = workbook.worksheet("Sheet1")
    sheet.update("A1", [df.columns.values.tolist()] + df.values.tolist())


# if __name__ == "__main__":
#     main()