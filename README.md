# Wordle Guesser

A very inefficient algorithm to guess the word for wordle.

Example usage:

```
python3 wordle-hacker.py
Enter confirmed letters: ....e
Enter possible letters: ..a..
Enter avoid letters: crn
```
```
Enter confirmed letters: ....e
Enter possible letters: a....
Enter avoid letters: lik
```
```
Enter confirmed letters: pa..e
Enter possible letters: ..s..
Enter avoid letters: t
The word is pause
```

## Shortcuts

Confirmed and possible letters are automatically padded to 5 characters.

e.g. If the confirmed mask is `..e..`, you can just type `..e`. Same goes with possible mask.

e.g. If there are no confirmed letters, you can just skip the field by pressing enter.

If you want to play another game or restart the guess, just type "restart" at the `Enter confirmed letters` stage

## The Dictionary

The dictionary is taken from [Peter Norvig's](http://norvig.com/ngrams/) compilation of the [1/3 million most frequent English words](http://norvig.com/ngrams/count_1w.txt). Thank you!
