Usage

The script accepts input from either the command line or stdin

`python3 ./calcheck.py email1 email2 ... emailn`

or

`python3 ./calcheck.py < emails_file.txt`

Emails which exist on the google platform are printed to stdout
Emails with public calendars are followed by a *

Output is written to stdout, one email per row
