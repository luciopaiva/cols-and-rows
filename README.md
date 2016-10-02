
# prep tools

Tools for manipulating text files, line by line, using regular expressions.

# prepm - replace with group matching

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

# prepf - filtering lines

Simple tool to filter (in or out) lines of the input file.

## Usage

    cat input.txt | ./prep.py [-x] <filter_pattern>

Where `filter_pattern` is the regular expression used to decided whether the line should be filtered or not. By default,
a match means the line is printed to the output. If `-x` is passed, the a match omits the line from the output.

For example, say you have a `sar` output like this:

    19:39:42         0,00 288915,31      0,00      0,00
    19:39:43         0,00 283270,30      0,00      0,00
    19:39:44         0,00 286699,00      0,00      0,00
    19:39:45         2,00 286293,00      0,00      0,00
    19:39:46         0,00 287045,00      0,00      0,00
    19:39:47         0,00 286393,00      0,00      0,00
    19:39:48         0,00 286517,00      0,00      0,00

    19:39:48       idgm/s    odgm/s  noport/s idgmerr/s
    19:39:49         0,00 289463,64      0,00      0,00

The output has a periodic header line, as well as a blank line. We want to filter this out:

    > cat input.txt | ./prepf.py -x '^$|idgm'
    19:39:42         0,00 288915,31      0,00      0,00
    19:39:43         0,00 283270,30      0,00      0,00
    19:39:44         0,00 286699,00      0,00      0,00
    19:39:45         2,00 286293,00      0,00      0,00
    19:39:46         0,00 287045,00      0,00      0,00
    19:39:47         0,00 286393,00      0,00      0,00
    19:39:48         0,00 286517,00      0,00      0,00
    19:39:49         0,00 289463,64      0,00      0,00

Now we can use `prepm` to select columns:

    > cat input.txt | ./prepf.py -x '^$|idgm' | ./prepm.py '^(\S+)\s+\S+\s+(\d+).*$' '\1\t\2'
    19:39:42	288915
    19:39:43	283270
    19:39:44	286699
    19:39:45	286293
    19:39:46	287045
    19:39:47	286393
    19:39:48	286517
    19:39:49	289463
