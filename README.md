# VK URL shortener

A script that allows you to get a VK short link to a web page and get a number of clicks on the short link.

### How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Should add your VK application access token to the .env file.
```
VK_TOKEN = 'd7ea29cbd7ea29cbd7ea29cb88d4cdb609dd7ead7ea29cbb062f7804d6b892f092d494b' 
```
You can find your token in the Service Access Key field of the VK ID Application Settings section. More info here https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token


### How to use
```
main.py [-h] link
```
If you provide long link the script returns shortened link. If you provide shortened link the script returns number of clicks.


### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).