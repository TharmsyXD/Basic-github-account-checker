import requests

def check_github(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{username} is a valid GitHub username!")
    else:
        print(f"{username} is not a valid GitHub username.")

    username = input("Enter a GitHub username to check: ")
    check_github(username)
