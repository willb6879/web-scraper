# Ram Module Web Scraper

This is a python library for dealing with extracting RAM module and spot prices off the dramexchange.com website every 24 hours. Places data in a csv file.

## Installation
### For Linux
1. Open command line
2. Enter "cd <file path>" to the location you wish to put package
3. Enter "git clone https://github.com/willb6879/web-scraper.git"

### For Windows
1. Open command line
2. Enter "cd <file path>" to the location you wish to put package
3. Enter "git clone https://github.com/willb6879/web-scraper.git"

## Automating the web scraper
### Linux
1. Create shell file
* First create a .sh file in the /home/<user> directory
* In this .sh file, enter "cd <path to 'web_scraping' file in package>" so we can access both the ram_data.csv file and ram_scraper.py files
* Next, in the .sh file, write "python3 ram_scraper.py" to run the scraper
* Save the file 
* Remember to keep this in the /home/<user> directory

2. Edit the crontab file to scheduled scraping task
* In linux we use something known as a "cron" job via crontab
* crontab allows you to run a task (script in our case) in order to perform tasks on a schedule
* Simply enter "crontab -e" into cmd to open a cron file
* In the file it gives you documentation regarding how to set the frequency of the automation
* Once you have the correct time parameters enter "bash <name of .sh file>" after the frequency parameters
* Save the file
* Your are all done! The scraper will now run as a scheduled task

### Windows
1. Create shell file
* First create a .sh file in the /home/<user> directory
* In this .sh file, enter "cd <path to 'web_scraping' file in package>" so we can access both the ram_data.csv file and ram_scraper.py files
* Next, in the .sh file, write "python3 ram_scraper.py" to run the scraper
* Save the file 
* Remember to keep this in the /home/<user> directory

2. Use Windows Task Scheduler to schedule scraping task
* Open windows explorer and enter 'Task Scheduler'
* In the right screen, click on 'Create Basic Task'
* Set a 'trigger' to specify the schedule you wish to have the scraping performed
* Set an 'action' to run your .sh file (specify path)
* Click 'Next' and you are finished! The scraper will run as a scheduled task

## Licensing


