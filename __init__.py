import check50
import uva.check50.py
import check50.internal
import re
import os
import sys

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

@check50.check()
def exists():
    """climate.ipynb exists."""
    check50.include("distro/climate.data")
    check50.exists("climate.ipynb")


@check50.check(exists)
def compiles():
    """climate.ipynb compiles."""
    uva.check50.py.nbconvert("climate.ipynb")
    uva.check50.py.compile("climate.py")
    return uva.check50.py.run("climate.py").stdout


@check50.check(compiles)
def correct_max_temp(stdout):
    """prints the maximum temperature measured"""
    match = re.search("maximale temperatuur[^\d]*(\d+[\.,]\d+)", stdout)
    if not match:
        raise check50.Failure("expected: De maximale temperatuur was XX.XX graden op")

    answer = float(match.groups(0)[0].replace(",", "."))

    if answer != 36.8:
        raise check50.Failure(f"expected 36.8 but found {answer}")


@check50.check(compiles)
def correct_max_temp_day(stdout):
    """prints the day of the maximum temperature"""
    match = re.search("maximale temperatuur[^\d]*\d+[\.,]\d+[^\d]+(\d+) ([a-zA-Z]{3}) ([\d]{4})", stdout)

    if not match:
        raise check50.Failure("expected: De maximale temperatuur was XX.XX graden op XX XXX XXXX")

    day = int(match.groups()[0])
    month = match.groups()[1]
    year = int(match.groups()[2])

    if day != 27 or month.lower() != "jun" or year != 1947:
        raise check50.Failure(f"expected 27 jun 1947 but found {day} {month} {year}")


@check50.check(compiles)
def correct_min_temp(stdout):
    """prints the minimum temperature measured"""
    match = re.search("minimale temperatuur[^\d-]*(-\d+[\.,]\d+)", stdout)
    if not match:
        raise check50.Failure("expected: De minimale temperatuur was -XX.XX graden op")

    answer = float(match.groups(0)[0].replace(",", "."))

    if answer != -11.3:
        raise check50.Failure(f"expected -11.3 but found {answer}")


@check50.check(compiles)
def correct_min_temp_day(stdout):
    """prints the day of the minimum temperature"""
    match = re.search("minimale temperatuur[^\d-]*-\d+[\.,]\d+[^\d]+(\d+) ([a-zA-Z]{3}) ([\d]{4})", stdout)

    if not match:
        raise check50.Failure("expected: De minimale temperatuur was -XX.XX graden op XX XXX XXXX")

    day = int(match.groups()[0])
    month = match.groups()[1]
    year = int(match.groups()[2])

    if day != 20 or month.lower() != "dec" or year != 1938:
        raise check50.Failure(f"expected 20 dec 1938 but found {day} {month} {year}")


@check50.check(compiles)
def correct_longest_freezing_period(stdout):
    """prints the length of the longest freezing period"""
    match = re.search("langste vriesperiode[^\d]*(\d+)", stdout)

    if not match:
        raise check50.Failure("expected: De langste vriesperiode is XX dagen")

    days = int(match.groups()[0])

    if days != 21:
        raise check50.Failure(f"expected 21 days but found {days}")


@check50.check(compiles)
def correct_last_day_freezing(stdout):
    """prints the last day of the longest freezing period"""
    match = re.search("langste vriesperiode[^\d]*\d+[^\d]+(\d+) ([a-zA-Z]{3}) ([\d]{4})", stdout)

    if not match:
        raise check50.Failure("expected: De langste vriesperiode is XX dagen en eindigde op XX XXX XXXX")

    day = int(match.groups()[0])
    month = match.groups()[1]
    year = int(match.groups()[2])

    if day != 24 or month.lower() != "feb" or year != 1947:
        raise check50.Failure(f"expected 24 feb 1947 but found {day} {month} {year}")

    return stdout


@check50.check(correct_last_day_freezing)
def correct_year_heatwave(stdout):
    """prints the year of the first heatwave"""
    if "1911" not in stdout:
        raise check50.Failure("expected 1911 as the year of the first heatwave")
