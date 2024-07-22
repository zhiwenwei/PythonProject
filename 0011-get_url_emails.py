import re
import requests
def get_emails_from_url(url):
    try:
        response = requests.get(url)
        #response.raise_for_status()
        content = response.text

        # Regular expression to find email addresses
        # Other way：email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        email_pattern = r'\b\w+@\w+\.\w+\b'
        emails = re.findall(email_pattern, content)

        # Convert list to set to remove duplicates
        unique_emails = set(emails)

        return unique_emails
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
def main():
    url = input("请输入提取邮箱的URL地址: ")
    emails = get_emails_from_url(url)

    if emails:
        print("找到以下邮箱地址:")
        for email in emails:
            print(email)
    else:
        print("没有找到邮箱地址")

if __name__ == "__main__":
    main()
