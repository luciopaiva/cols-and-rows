
# prep

Simple tool to map lines from input file following some regular expression pattern. Forget grep, sed or awk... it should
be way simpler than that, at least for the average case!

## Usage

    cat input.txt | ./prep.py <search_pattern> <replace_pattern>

Where `search_pattern` is the regexp pattern to be used to match the portion of each line in the input file to be
replaced by `replace_pattern`. Rules are governed by
[Python's regulare expression syntax](https://docs.python.org/2/library/re.html#regular-expression-syntax).

For example, say you have the following input file:

    13:59:00         0,00 282823,23
    13:59:01         0,00 283311,88
    13:59:02         0,00 288668,69
    13:59:03         0,00 283367,33
    13:59:04         0,00 289152,53
    13:59:05         0,00 286461,00
    13:59:06         0,00 284009,90
    13:59:07         0,00 285977,00
    13:59:08         0,00 288623,23
    13:59:09         0,00 283202,97

And you would like to remove the middle column and separate left and right columns by a tab char, and at the same time
removing the fractional part of the right column. One way to do that is:

    > cat input.txt | ./prep.py '^(\S+).*?(\d+),\d+$' '\1\t\2'
    13:59:00	282823
    13:59:01	283311
    13:59:02	288668
    13:59:03	283367
    13:59:04	289152
    13:59:05	286461
    13:59:06	284009
    13:59:07	285977
    13:59:08	288623
    13:59:09	283202
