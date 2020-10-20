def seconds_from_date(date: str) -> int:
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return int(year * 365 * 86400 + month * 30 * 86400 + day * 86400)

def date_from_seconds(second: int) -> str:
    days, seconds = divmod(second, 86400)
    years, days = divmod(days, 365)
    months, days = divmod(days, 30)
    return "-".join([str(years), str(months), str(days)]), seconds
