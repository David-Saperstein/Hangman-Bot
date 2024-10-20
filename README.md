# Hangman-Bot
A bot designed to play optimal hangman. If you stump the bot with slang it hasn't heard before; it will update its dictionary for future rounds. The bot uses regular expressions to search efficiently 
 through large dictionaries.

## Installation

```bash
git clone https://github.com/David-Saperstein/Hangman-Bot.git
```

## Usage
Navigate to the installation directory
```bash
python hangman.py
```
Input the current board state using periods for blank spaces.

Example:
```
: .......

e
: .......

a
: .a...a.

n
: .an..an

m
: .an.man

d
: .an.man

g
: .angman
The word is hangman
I got 2 letters wrong
Is that correct? (y/n): y
Hooray!
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
