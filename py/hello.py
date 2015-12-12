#!/usr/bin/env python3

import skilstak.colors as c
import time

def print_pink(hello):
    print(c.m + hello)

def print_red(hello):
    print(c.r + hello)

def print_orange(hello):
    print(c.o + hello)

def print_yellow(hello):
    print(c.y + hello)

def print_plain(hello):
    print("hello")

def print_color(hello):
    while True:
         print(c.rc() +  hello, end=" ")

def print_multi(hello):
    while True:
         print(c.clear + c.multi(hello))
         time.sleep(0.5)
