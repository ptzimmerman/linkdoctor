# linkdoctor

### Clone this repo
`git clone https://github.com/ptzimmerman/linkdoctor.git`

### Setup Virtual Environment
If you don't have a virtual environment set up and you're on macOS, [go here](https://opensource.com/article/19/5/python-3-default-mac)  
`python3 -m venv link_doctor`

### Drop into pyenv
`source link_doctor/bin/activate`

### Install and run Link Doctor
`pip install -r requirements.txt`
`scrapy runspider crawler.py -o broken_links.csv`
