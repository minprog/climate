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
    """print een overzicht per jaar van het maximum en minimum voor dat jaar"""
    check50.include("answers/variation_yearly.csv")
    with open("variation_yearly.csv") as f:
        answers = list(csv.DictReader(f))
    
    for a in answers:
        text_int = "{} varieerde de temperatuur tussen {} graden op {}/{} en {} graden op {}/{}".format(*a.values())
        a["min_temp"] = int(a["min_temp"]) / 10
        a["max_temp"] = int(a["max_temp"]) / 10
        text_float = "{} varieerde de temperatuur tussen {} graden op {}/{} en {} graden op {}/{}".format(*a.values())

        find_any_prints([text_float, text_int], stdout)


@check50.check(compiles)
def longest_heatwave(stdout):
    """print een overzicht per jaar van de lengte van de langste hittegolf"""
    zero_days = "duurde de langste hittegolf 0 dagen"
    if zero_days in stdout:
        raise check50.Failure(
            f'vond het volgende in de output: "{zero_days}"',
            help="print geen jaartallen uit waarin er geen hittegolf heeft plaatsgevonden"
        )

    check50.include("answers/longest_heatwave.csv")
    with open("longest_heatwave.csv") as f:
        answers = list(csv.DictReader(f))

    for a in answers:
        text = "{} duurde de langste hittegolf {} dagen".format(*a.values())
        find_any_prints([text], stdout)


@check50.check(compiles)
def outliers(stdout):
    """print de outliers voor ieder jaar"""
    check50.include("answers/outliers.csv")
    with open("outliers.csv") as f:
        answers = list(csv.DictReader(f))

    for a in answers:
        text_int = "{} is de waarde op {}/{}/{} een outlier".format(*a.values())
        a["temp"] = int(a["temp"]) / 10
        text_float = "{} is de waarde op {}/{}/{} een outlier".format(*a.values())

        find_any_prints([text_float, text_int], stdout)


def find_any_prints(prints, stdout):
    if all(p not in stdout for p in prints):
        raise check50.Failure(
            f'Kon "{prints[0]}" niet vinden in de output.',
            help="Let extra goed op de spelling en of er niet te veel spaties staan.\n"\
                    "    Print een dag in een datum altijd uit als twee karakters, bijvoorbeeld 03 juni 2019.\n"\
                    "    Temperaturen mogen in tienden of hele graden Celsius worden geprint, bijvoorbeeld: 395 of 39.5"
        )


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
