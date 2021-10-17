import check50
import uva.check50.py
import check50.internal
import csv
import os
import re
import sys

check50.internal.register.before_every(lambda: sys.path.append(os.getcwd()))
check50.internal.register.after_every(sys.path.pop)

@check50.check()
def exists():
    """climate.ipynb exists."""
    check50.include("../dist/climate/climate.txt")
    check50.exists("climate.ipynb")


@check50.check(exists)
def compiles():
    """climate.ipynb compiles."""
    uva.check50.py.nbconvert("climate.ipynb")
    uva.check50.py.compile("climate.py")
    return uva.check50.py.run("climate.py").stdout


@check50.check(compiles)
def min_temp(stdout):
    """print de minimum temperatuur"""
    try:
        find_int("Minimum:", -114, stdout)
        return
    except check50.Failure:
        pass
    find_float("Minimum:", -11.4, stdout)


@check50.check(compiles)
def avg_temp(stdout):
    """print de gemiddelde temperatuur"""
    try:
        find_int("Gemiddelde:", 135, stdout)
        return
    except check50.Failure:
        pass
    find_float("Gemiddelde:", 13.5, stdout)


@check50.check(compiles)
def max_temp(stdout):
    """print de maximum temperatuur"""
    try:
        find_int("Maximum:", 375, stdout)
        return
    except check50.Failure:
        pass
    find_float("Maximum:", 37.5, stdout)


@check50.check(compiles)
def median(stdout):
    """print de mediaan van de temperaturen"""
    try:
        find_int("Mediaan:", 135, stdout)
        return
    except check50.Failure:
        pass
    find_float("Mediaan:", 13.5, stdout)


@check50.check(compiles)
def modus(stdout):
    """print de modus van de temperaturen"""
    try:
        find_int("Modus:", 90, stdout)
        return
    except check50.Failure:
        pass
    find_float("Modus:", 90.0, stdout)


@check50.check(compiles)
def variation_yearly(stdout):
    """print de variatie van temperaturen per jaar"""
    check50.include("answers/variation_yearly.csv")
    with open("variation_yearly.csv") as f:
        answers = list(csv.DictReader(f))
    
    for a in answers:
        text_int = "{} varieerde de temperatuur tussen {} op {} {} en {} op {} {}".format(*a.values())
        a["min_temp"] = int(a["min_temp"]) / 10
        a["max_temp"] = int(a["max_temp"]) / 10
        text_float = "{} varieerde de temperatuur tussen {} op {} {} en {} op {} {}".format(*a.values())

        if text_int not in stdout and text_float not in stdout:
            text = "In " + text_float
            raise check50.Failure(
                f'kon "{text}" niet vinden in de output',
                help="let extra goed op de spelling en of er niet te veel spaties staan"
            )


@check50.check(compiles)
def longest_heatwave(stdout):
    """print de langste hittegolf voor ieder jaar"""
    check50.include("answers/longest_heatwave.csv")
    with open("longest_heatwave.csv") as f:
        answers = list(csv.DictReader(f))

    for a in answers:
        text = "{} duurde de langste hittegolf {} dagen".format(*a.values())

        if text not in stdout:
            text = "In " + text
            raise check50.Failure(
                f'kon "{text}" niet vinden in de output',
                help="let extra goed op de spelling en of er niet te veel spaties staan"
            )

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


def find_int(prompt, number, text):
    number = int(number)
    pattern = r"\d+"
    answer = int(_find_number(prompt, pattern, text))
    
    if answer != number:
        raise check50.Failure(f"verwachtte {number}, maar vond {answer}")


def find_float(prompt, number, text):
    number = float(number)
    pattern = r"\d+[.,]\d+"
    answer = float(_find_number(prompt, pattern, text))

    if answer != number:
        raise check50.Failure(f"verwachtte {number}, maar vond {answer}")


def _find_number(prompt, pattern, text):
    match = re.search(prompt + r"[^\d-]*(-*" + pattern + r")", text)
    if not match:
        raise check50.Failure(
            f'kon "{prompt}" niet vinden in de output',
            help=f"let erop dat {prompt} precies zo wordt geprint"
        )

    return match.groups(0)[0]