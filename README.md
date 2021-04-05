## Instagram Automatic Account Creator Bot

<p>This small piece of code will create an account automatically by randomizing names. You need Selenium library installed. This is an ongoing work. Beware that Instagram has security measures to prevent bot usage. Do not forget to change the Web driver you use from the part of the code:</p>

Download selenium chrome drive: 
https://chromedriver.chromium.org/downloads

Download selenium FireFox drive: 
https://www.lambdatest.com/blog/selenium-firefox-driver-tutorial/

Set Environment Variables
```Python
export DRIVER_PATH='/Users/roy.bahian/rb-repo/temp/instegram/chromedriver'
```


<h2>Requirements</h2>
<p> run
<code>
  pip3 install -r requirements.txt
</code> 
</p>

<h2>New features</h2>

<ul>
  <li>Fake email address</li>
  <li>Getting verification code</li>
</ul> 


### Usage
export DRIVER_PATH='/Users/roy.bahian/rb-repo/temp/instegram/chromedriver'
python3 botAccountCreate.py --chrome

