from utils import get_number_from_filename, get_ordered_scripts

names = [
    '045.createtable.sql',
    '045createtable.sql',
    'foobar32.somestatement.sql'
    '2345.sofhihfd.sql',
    '10000000.dfjdkjfkd.sql',
    '-124fjdkfjkdfjkdj.sql',
    '-12345.fjkdfjdk.sql'
]

print(get_number_from_filename(names))


