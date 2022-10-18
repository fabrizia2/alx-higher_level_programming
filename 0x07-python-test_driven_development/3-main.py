#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Renish", "Okago")
say_my_name("Brenda", "Trezy")
say_my_name("Kefa")
try:
    say_my_name(12, "Bicko")
except Exception as e:
    print(e)
