import collections

DAY_NAMES = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']

def coalesce_days(days):
    """Given a list of days, emit a set of ranges of contiguous days, where each range is
    (start_day, end_day). start and end will be the same day for non-contiguous days."""
    start = None
    end = None
    for d in days:
        if end is not None and d != end + 1:
            yield (start, end)
            start = None
            end = None
        if start is None:
            start = d
        end = d
    yield (start, end)

def format_day_range(start, end):
    if start == end:
        return DAY_NAMES[start]
    else:
        return '-'.join(DAY_NAMES[d] for d in (start, end))

def format_days(days):
    return ', '.join(format_day_range(*rng) for rng in coalesce_days(days))

def format_hours(hrs):
    return '-'.join(hrs)

def format_opening_hours(hours_by_day):
    days_by_distinct_hours = collections.defaultdict(list)
    for day, day_hours in enumerate(hours_by_day):
        days_by_distinct_hours[tuple(day_hours)].append(day)

    return ['%s: %s' % (format_days(days), format_hours(hours)) for days, hours
            in sorted((days, hours) for hours, days in days_by_distinct_hours.iteritems())]

if __name__ == "__main__":

    examples = [
        [
            ['9:00', '5:00'], # Monday
            ['9:00', '5:00'], # Tuesday
            ['9:00', '5:00'], # ...
            ['9:00', '5:00'],
            ['9:00', '5:00'],
            ['9:00', '5:00'],
            ['9:00', '5:00'],
        ],
        [
            ['9:00', '5:00'], # Monday
            ['9:00', '5:00'], # Tuesday
            ['9:00', '5:00'], # ...
            ['9:00', '5:00'],
            ['9:00', '5:00'],
            ['12:00', '5:00'],
            ['12:00', '5:00'],
        ],
        [
            ['8:00', '4:00'], # Monday
            ['9:00', '5:00'], # Tuesday
            ['8:00', '4:00'], # ...
            ['9:00', '5:00'],
            ['8:00', '4:00'],
            ['12:00', '5:00'],
            ['12:00', '5:00'],
        ],
        [
            ['8:00', '4:00'], # Monday
            ['8:00', '4:00'], # Tuesday
            ['8:00', '4:00'], # ...
            ['9:00', '5:00'],
            ['8:00', '4:00'],
            ['12:00', '5:00'],
            ['12:00', '5:00'],
        ],
    ]

    for example in examples:
        print '\n'.join(format_opening_hours(example))
        print
