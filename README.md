# doctolib monitoring

This script checks approx every 1.5 hours whether an appointement for a doctor is free before a set date.

If a date is available, it outputs on stdout and exits otherwise outputs on stderr.

Usage :
```
usage: doctolib.py [-h] -d DATE -u URL

optional arguments:
  -h, --help            show this help message and exit
  -d DATE, --date DATE  format : dd-mm-yyyy.
  -u URL, --url URL     set the url to check
```

# URL
Go on the URL of the doctor you want an appointement with

Use the availabilities.json URL from the doctor's booking page

