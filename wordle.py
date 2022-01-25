#!/usr/bin/env python

"""
This is simple implementation of word game 'Wordle'.
"""
__author__ = "Abhishek Varshney"


import argparse
import getpass
import os
import sys
from typing import List

from rich.console import Console

MAX_RETRY = 10
console = Console()


def nltk_setup():
    """A simple trick to download 'words' database."""
    import nltk

    try:
        nltk.data.find("corpora/words")
    except:
        console.print("words package not found. Downloading...")
        nltk.download("words")
        console.print("Download is successful.")


def clear():
    """Using system calls to clear screen."""
    # For windows
    if os.name == "nt":
        _ = os.system("cls")
    # For mac and linux
    else:
        _ = os.system("clear")


def print_guess_table(table: List[List[str]]):
    """Using rich library to print colored output and legend."""
    for row in table:
        console.print(" ".join(row))

    if table:
        print("")
        console.print("  Legend:")
        console.print(
            "    [magenta]Magenta[/magenta]: Letter doesn't exist in original word."
        )
        console.print("    [yellow]Yellow[/yellow]: Letter exists, but at different place.")
        console.print("    [green]Green[/green]: Letter exists, at same place.")


def create_and_print_guess_table(
    guess: str, word: str, printable_table: List[List[str]]
) -> List[List[str]]:
    """Find out which letters are at correct place and which are at wrong place.
    Also, make sure that only exact number of letters should be shown as misplaced.
    e.g: word = lad, guess : dad, first 'd' will be treated as wrong letter as 'd'
    at 3rd place is already present."""
    print_vals = []
    id_used = {}

    if not guess:
        print_guess_table(printable_table)
        return printable_table

    for x, y in zip(guess, word):
        if x == y:
            print_vals.append(f"[green]{x}[/green]")
        elif x in word:
            if x not in id_used:
                id_used[x] = []
            # but same letter should not be present at same place. Case of repeated letter.
            same_pos_not_found = False
            for idx, l in enumerate(word):
                if x == l and guess[idx] != x and idx not in id_used:
                    same_pos_not_found = True
                    id_used[x].append(idx)

            if same_pos_not_found:
                print_vals.append(f"[yellow]{x}[/yellow]")
            else:
                print_vals.append(f"[magenta]{x}[/magenta]")
        else:
            print_vals.append(f"[magenta]{x}[/magenta]")
    printable_table.append(print_vals)
    print_guess_table(printable_table)

    return printable_table


def get_word() -> str:
    clear()
    word = getpass.getpass("Enter a word: ").upper()
    retry_word = getpass.getpass("Repeat word : ").upper()

    if word != retry_word:
        print("Both words are not matching!!")
        sys.exit()

    if len(word) == 0:
        sys.exit()

    if args.nltk and word.lower() not in words_set:
        print("Not a valid dictionary word!!")
        sys.exit()

    return word


def main():
    word = get_word()
    word_len = len(word)
    guess = ""
    retry = 0
    tries = []
    guessed = False
    printable_table = []

    while guess != word and retry < MAX_RETRY:
        clear()
        printable_table = create_and_print_guess_table(guess, word, printable_table)
        console.print(f"\nRetry left: {MAX_RETRY - retry}")
        guess = input(f"Enter your guess (Length: {word_len}): ").upper()
        if len(guess) != word_len:
            console.print("[red]Wrong Length of Word.[/red]")
            input("Press Enter to continue...")
            guess = ""
            continue

        if guess in tries:
            console.print("[red]Already tried.[/red]")
            input("Press Enter to continue...")
            guess = ""
            continue

        if args.nltk and guess.lower() not in words_set:
            console.print("[red]Not a valid dictionary word!![/red]")
            input("Press Enter to continue...")
            guess = ""
            continue

        retry += 1

        tries.append(guess)

        if word == guess:
            console.print(
                f"\n[green]Congratulations!! You guessed it right in {retry} {'tries' if retry > 1 else 'try'}.[/green]"
            )
            guessed = True
            break

    if not guessed:
        console.print("\n[red]Sorry, you couldn't guess the word.[/red]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--nltk",
        help="Enable dictionary check for each word.",
        default=False,
        action="store_true",
    )
    args = parser.parse_args()
    if args.nltk:
        # nltk will be enabled only when --nltk flag is passed.
        nltk_setup()
        from nltk.corpus import words

        words_set = set(words.words())

    main()
