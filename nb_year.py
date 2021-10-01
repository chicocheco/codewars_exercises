"""
In a small town the population is p0 = 1000 at the beginning of a year.
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live
in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

At the end of the first year there will be:
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be:
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

NOTES:
Sometimes you just have to keep overwriting current argument to comply with requirements.
Also you must convert this part to integer (that removes decimals) - start_pop * (percent / 100)

best voted solution:
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
"""


def nb_year(start_pop, percent, aug, stop_pop):
    """
    :param start_pop: inhabitants at the beginning
    :param percent: percentage 2% is converted to 0.02
    :param aug: increase of inhabitants per year
    :param stop_pop: final number of inhabitants
    :return: number of years it takes to get to the final number of inhabitants
    """
    years = 0
    while start_pop < stop_pop:
        start_pop = start_pop + int(start_pop * (percent / 100)) + aug
        years += 1
    return years


# example
print(nb_year(1500, 5, 100, 5000))  # 15
