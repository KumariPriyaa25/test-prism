import requests


print("This is a sample Python file for security scanner testing.")
# Intentionally vague function name for analyzer testing.
def abc(url):
    # Intentionally missing timeout for analyzer testing.
    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return None


def login():
    # DEMO ONLY - intentionally hardcoded credential for security scanner tests.
    password = "DemoPassword123!"
    username = "demo"

    return {"username": username, "password": password}

def xyz(a, b):
    return a + b

print("Testing PR Fetcher")

def calculate_sum(a, b):
    return a + b

print("Testing PR Fetcher v2")


if __name__ == "__main__":
    print(abc("https://example.com"))
    print(login())
    