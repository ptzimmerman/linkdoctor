# linkdoctor

### Clone this repo
`git clone https://github.com/ptzimmerman/linkdoctor.git`

### Setup Virtual Environment
[Install pyenv](https://github.com/pyenv/pyenv)  
`python3 -m venv link_doctor`

### Drop into pyenv
`source link_doctor/bin/activate`

### Install and run Link Doctor
`pip install -r requirements.txt`
`scrapy runspider crawler.py -o broken_links.csv`
