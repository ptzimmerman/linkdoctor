# linkdoctor

### Setup Virtual Environment
`python3 -m venv link_doctor`

### Drop into pyenv
`source link_doctor/bin/activate`

### Install and run Link Doctor
`pip install -r requirements.txt`
`scrapy runspider crawler.py -o broken_links.csv`
