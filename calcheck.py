import sys
import requests

# Disable all warnings from urllib3
requests.packages.urllib3.disable_warnings()

def verify_email(email):
    """Verify the given email address."""
    # Replace *** in the URL with the email address
    url = f"https://calendar.google.com/calendar/ical/{email}/public/basic.ics"

    try:
        # Make an HTTP call to the URL without SSL certificate verification
        response = requests.get(url, verify=False)

        # Check the response headers for the presence of the "x-frame-options: SAMEORIGIN" string
        if 'x-frame-options' in response.headers and response.headers['x-frame-options'].upper() == 'SAMEORIGIN':
            # Append an asterisk if the HTTP response code is 200
            asterisk = " *" if response.status_code == 200 else ""
            print(f"{email}{asterisk}")
        # If the header is not present, nothing is printed
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with {email}: {e}")

def main():
    if len(sys.argv) > 1:
        # If there are command-line arguments, verify each email address
        for email in sys.argv[1:]:
            verify_email(email.strip())
    else:
        # Otherwise, read from sys.stdin
        for line in sys.stdin:
            email = line.strip()
            verify_email(email)

if __name__ == "__main__":
    main()
