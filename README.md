# Wordle on Terminal: A simple implementation in Python
I implemented this game just to show my kid a fun side of programming. Btw, she is now showing more interest in learning programming. ;)

## Installation
1. Create a `venv`
```sh
python -m venv venv
```
2. Activate `venv`
```sh
source ./venv/bin/activate
```
4. Install dependencies
```sh
pip install -r requirements.txt
```
6. Start the game
```sh
python wordle.py
```

## Usage
```sh
python wordle.py --help                                                                                                                     Py python 13:45:41
usage: wordle.py [-h] [--nltk]

optional arguments:
  -h, --help  show this help message and exit
  --nltk      Enable dictionary check for each word.
```
> Use --nltk switch to enable dictionary check. without this, there will not be any dictionary check.
> In case of nltk enabled, this program will try to download 'words' database for spell check.

### Steps
1. First player has to provide a word. Don't worry, it is hidden. :)
2. Now first player can pass screen to second player, where he has to guess word by using hints provided by `wordle` based on characters.
3. Second player will get 10 chances to guess it right.

## Screenshot
![image](https://user-images.githubusercontent.com/10027388/150939471-9420c8b8-f081-4cc2-ac8b-ec84e2c01789.png)

## TODO
Generate random word to enable single player mode.
