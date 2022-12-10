from getpass import getpass
import hashlib
import random
import string
import sys
from dbconfig import dbconfig

from rich import print as printc
from rich.console import Console

console = Console()


def config():
    # Create database
    db = dbconfig()
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE yoga")
    except Exception as e:
        printc("[red][!] An error occurred while trying to create db. Check if database with name 'yoga' already exists - if it does, delete it and try again.")
        console.print_exception(show_locals=True)
        sys.exit(0)
        
    printc("[green][+][/green] Database 'yoga' created")

    # Create tables
    query = "CREATE TABLE yoga.entries (REG_NO char, NAME varchar(255), ADDRESS varchar(255), AGE varchar(255), BATCH varchar(255))"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")

    query = "CREATE TABLE yoga.payment (REG_NO char, JAN char, FEB char, APRIL char, MAR char, MAY char, JUN char, JUL char, AUG char, SEPT char, OCT char, NOV char, DECEM char)" #,    DEC char)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'payment' created")


    db.commit()

    printc("[green][+][/green] Added to DB")
    printc("[green][+][/green] Config Done!!!")
    db.close()


config()
