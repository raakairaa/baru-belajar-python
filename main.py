import sys
import time
import threading
from itertools import cycle
from colorama import init, Fore, Style
from rich.console import Console
from rich.text import Text
from curses import wrapper
import os

# Inisialisasi colorama
init(autoreset=True)

# Rich Console untuk animasi
console = Console()

# Lirik Lagu dan Durasi
LYRICS = [
    ("panas - panase srenege kuwi", 5),
    ("kang nguliti awak iki", 4),
    ("nanging sih panas rasaning ati", 4),
    ("nyawang kedadean ikiiiiiiii", 5),
    ("python lyrics music by @syaaikoo", 5),
]

# Warna dan gaya ANSI
COLORS = cycle([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])


# =========================== Fungsi Animasi CLI =========================== #
def fade_in_text(text):
    """Efek fade-in menggunakan manipulasi warna ANSI."""
    for i in range(1, 11):
        brightness = int(30 + (i * 22.5))  # Rentang brightness 30-255
        color = f"\033[38;2;{brightness};{brightness};{brightness}m"
        sys.stdout.write(f"{color}{text}\r")
        sys.stdout.flush()
        time.sleep(0.1)
    print()  # Pindah ke baris berikutnya


def scroll_text(text):
    """Efek scrolling horizontal menggunakan sys.stdout.write()."""
    width = os.get_terminal_size().columns
    padded_text = " " * width + text + " " * width
    for i in range(len(padded_text) - width):
        sys.stdout.write("\r" + padded_text[i : i + width])
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def typing_effect(text):
    """Efek mengetik (progressive reveal)."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def show_ascii_animation():
    """Animasi ASCII art sederhana."""
    wave = ["-", "\\", "|", "/"]
    for _ in range(10):
        for frame in wave:
            sys.stdout.write(f"\r{frame} Loading...")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\rDone!        ")


def rich_effects():
    """Menggunakan pustaka rich untuk gaya dinamis."""
    text = Text("Rich Text Example")
    text.stylize("bold magenta", 0, 4)
    text.stylize("italic cyan", 5, 9)
    text.stylize("underline yellow", 10, 15)
    console.print(text)


# =========================== Antarmuka Terminal =========================== #
def curses_interface(stdscr):
    """Antarmuka dinamis menggunakan curses."""
    curses.curs_set(0)
    stdscr.nodelay(1)
    height, width = stdscr.getmaxyx()
    text = "Welcome to the Interactive Lyrics Display"
    x_pos = width

    while x_pos + len(text) > 0:
        stdscr.clear()
        stdscr.addstr(height // 2, x_pos, text)
        stdscr.refresh()
        x_pos -= 1
        time.sleep(0.05)


# ============================= Multithreading ============================= #
def lyrics_display():
    """Menampilkan lirik dengan berbagai efek secara multithreading."""
    for lyric, delay in LYRICS:
        threading.Thread(target=fade_in_text, args=(lyric,)).start()
        time.sleep(delay)


# ============================== Menjalankan =============================== #
def main():
    """Fungsi utama untuk menjalankan program."""
    console.print("[bold magenta]Welcome to Lyrics Animation![/bold magenta]\n")
    
    print("\n[1] Fade-in Text")
    fade_in_text("Hello World with Fade-in Effect!")

    print("\n[2] Scrolling Text")
    scroll_text("This is a scrolling text example...")

    print("\n[3] Typing Effect")
    typing_effect("Typing effect in progress...")

    print("\n[4] ASCII Animation")
    show_ascii_animation()

    print("\n[5] Rich Effects")
    rich_effects()

    print("\n[6] Curses Interface")
    wrapper(curses_interface)

    print("\n[7] Multithreading Lyrics Display")
    lyrics_display()


if __name__ == "__main__":
    main()
