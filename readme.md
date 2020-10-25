# Simple shim program in Python

This is a very basic module to help "shim" a program, which is to allow creating a Python script that launches another program, passing through its stdin and arguments.

Usage is simple, pass the path to an executable file to `shim.run()`.

If the path doesn't exist, it'll raise a `FileNotFoundError`.
