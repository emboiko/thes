## thes.py

###### A quick romp through Selenium page objects - This application would likely run much quicker with [bs4](https://pypi.org/project/beautifulsoup4/), [nightmare](https://github.com/segmentio/nightmare), or [puppeteer](https://github.com/puppeteer/puppeteer).

Why spend 3 seconds doing something when you can spend 3 hours learning to automate it? *thes* prints synonyms to the console with headless browser automation and a few [xpath](https://developer.mozilla.org/en-US/docs/Web/XPath) selectors using data peeled from [thesaurus.com](https://www.thesaurus.com/).

<div align="center">
<img src="https://i.imgur.com/Yq1zQrF.png">
<img src="https://i.imgur.com/5nqRMwS.png?1">
<img src="https://i.imgur.com/S8kEaPW.png">
</div>

#### Installation And Usage

- Download [Chromium Webdriver](https://chromedriver.chromium.org/downloads) and place it on the system PATH
- With Python:
    - `python -m virtualenv path/to/venv` Make a virtual environment of your choosing. 
    - `scripts/activate.ps1` (or whichever script suits your shell)
    - `pip install requirements.txt` (currently just Selenium & PyInstaller)
    - `python thes.py {synonym} [limit]` 
    

- Executable:
    - `dist/thes/thes.exe {synonym} [limit]`
    
    	**or**
        
    - `New-Alias thes /path/to/thes.exe`
    - `thes {synonym} [limit]`
