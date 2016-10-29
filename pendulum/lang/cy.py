# -*- coding: utf-8 -*-

translations = {
    # Days
    'days': {
        0: 'Dydd Sul',
        1: 'Dydd Llun',
        2: 'Dydd Mawrth',
        3: 'Dydd Mercher',
        4: 'Dydd Iau',
        5: 'Dydd Gwener',
        6: 'Dydd Sadwrn'
    },
    'days_abbrev': {
        0: 'Sul',
        1: 'Llun',
        2: 'Maw',
        3: 'Mer',
        4: 'Iau',
        5: 'Gwe',
        6: 'Sad'
    },

    # Months
    'months': {
        1: 'Ionawr',
        2: 'Chwefror',
        3: 'Mawrth',
        4: 'Ebrill',
        5: 'Mai',
        6: 'Mehefin',
        7: 'Gorffenaf',
        8: 'Awst',
        9: 'Medi',
        10: 'Hydref',
        11: 'Tachwedd',
        12: 'Rhagfyr',
    },
    'months_abbrev': {
        1: 'Ion',
        2: 'Chwe',
        3: 'Maw',
        4: 'Ebr',
        5: 'Mai',
        6: 'Meh',
        7: 'Gor',
        8: 'Aws',
        9: 'Med',
        10: 'Hyd',
        11: 'Tach',
        12: 'Rhag',
    },

    # Units of time
    'year': ['{count} year', '{count} years'],
    'month': ['{count} month', '{count} months'],
    'week': ['{count} week', '{count} weeks'],
    'day': ['{count} day', '{count} days'],
    'hour': ['{count} hour', '{count} hours'],
    'minute': ['{count} minute', '{count} minutes'],
    'second': ['{count} second', '{count} seconds'],

    # Relative time
    'ago': '{time} yn ôl',
    'from_now': '{time} from now',
    'after': '{time} after',
    'before': '{time} before',

    # Ordinals
    'ordinal': lambda x: 'th' if 10 <= x % 100 < 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(x % 10, "th"),

    # Meridians
    # [time] is a (hour, minute) tuple
    'meridian': lambda time: 'yb' if 0 <= time[0] < 12 else 'yh',

    # Date formats
    'date_formats': {
        'LTS': 'h:mm:ss A',
        'LT': 'h:mm A',
        'L': 'MM/DD/YYYY',
        'LL': 'MMMM D, YYYY',
        'LLL': 'MMMM D, YYYY h:mm A',
        'LLLL': 'dddd, MMMM D, YYYY h:mm A',
    },
}
