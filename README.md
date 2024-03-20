Usage

the script supports reading from command line or from stdin

`python3 ./calcheck.py email1 email2 ... emailn`

or

`python3 ./calcheck.py < emails_file.txt`

the output is written to stdout, one email per row.
emails which do not exist on the google platform are not printed
emails with public calendars are followed by a *
