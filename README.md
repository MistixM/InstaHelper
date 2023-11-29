# InstaHelper

## Description

Simple tool to analyse accounts with a specific query on Instagram.

## Implementation Details

This project uses ```instaloader``` library to manipulate with Instagram (accounts, posts, stories, etc.)

Project uses ```csv``` library to save parsed information. File provides account information (username, full_name, biography, external_url)

Project uses ```json``` library to receiving some data from user: username, password and max count (how many accounts do you want to analyse?)

Also, project uses ```sys``` and ```colorama``` libraries to sometimes manipulate with script and set colors to the terminal window.

In script you can find ```parse_instagram_search()``` function that responsible for parse processing

## How to Run

#### If you want to analyse via .exe file:
1. Download .exe file and put it in a convenient directory.
2. In ```info.json``` you'll find this:

```
{
    "username": "your_instagram_username_here",
    "password": "your_instagram_password_here",
    "max_count": 10 
}
```
```username```: needs for your Instagram username. It's necessary to log in.
```password```: needs for your Instagram password. It's necessary to log in as well.

```max_count```: represents the number of accounts to find (by default 10)

**Fill in all the required information to correct work!**

3. Launch .exe file and wait for the program to authorise you.
4. After authorising you are able to text your required query.
5. Program will display progress information in the terminal window.
6. Program will automatically closed at the end of the parse process.
7. In the same directory you'll find ```data.csv``` with all parsed Instagram accounts information.

#### If you want to analyse via Python:
1. Download Python files and put it in a convenient directory.
2. You'll find same ```info.json``` with the same file configuration as before.
3. Launch Python file via double-click or ```python insthelper.py``` in the terminal window.
4. Same actions with authorising, parsing as .exe program.

## Troubleshooting

#### My .exe program does not start. How to fix?
1. Check your .json file location.
2. Check if .json file exists.
3. Check if .json filled correctly (username, password)
3. If these two solutions don't work, reinstall your program using GitHub.

#### My program has worked for a while but suddenly closed. How to fix?
1. Unfortunately ```instaloader``` library could be seen by Instagram. Instagram may think you're a bot and try to check this by logging out. Also, Instagram may notify you that your account may be locked due to unidentified activity on your account. **Be vigilant about this!**
2. Every third-party application connected to Instagram’s API has a restriction on how many times it may access its data. Instagram has recently decreased its API restriction from 5,000 to 200 requests per hour.
3. Message ```[=] Maximum reached``` means that program has already reached the maximum number of accounts to search.

[More about Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/?locale=en_US#:~:text=Reference-,Rate%20Limits,-A%20rate%20limit)

**How to fix that issue?**

(For 1 and 2) To fix that problem you can just try to parse your information later or use VPN instead. **But I recommend you to try later!**
(For 3) To fix that problem you can just search with another query. **Note! Remember to save your current .csv file, because if you try to search again, the previous data will be changed to the new query!**

