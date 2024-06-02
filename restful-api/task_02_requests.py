#!/usr/bin/python3
"""use requests function in order to get info"""


import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # Print the status code of the response
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()
        
        # Iterate through the parsed JSON data and print the titles of all posts
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        posts_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        # Write data into a CSV file
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(posts_list)
        
        print("Posts have been saved to posts.csv")
    else:
        print("Failed to fetch posts")
