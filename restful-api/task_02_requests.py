#!/usr/bin/python3
"""make a request and work with json data, finally transfer to csv file"""


import requests
import csv


def fetch_and_print_posts():
    response = response.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        post = response.json()
        for post in posts:
            print(post['title'])


fetch_and_print_posts()


def fetch_and_save_posts():
    response = response.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    posts_list = [{"id": post["id"], "title": post["title"],
                   "body": post["body"]} for post in posts]

    with open('posts.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts_list)


fetch_and_save_posts()
