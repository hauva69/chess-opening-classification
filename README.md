# chess-opening-classification

Chess opening classification data consists of data, which enables developers
to classify positions with an English name, ECO code and NIC code.

# The origin of the data

I copied the data from the source code of Lasker database by Andrew Tridgell
and others. Tridgell considered all the various sources to be GPL compatible,
so I will, at least for now, use also GPL for this project, even though
original data has much more permissible copying rules.

I was unable to locate Lasker, but I found a fork called [Capablanca]
(https://github.com/ddugovic/capablanca).

# Character encoding in the English long names

The original data is ASCII only, with a special escaping for some of the
accented characters. Many long names which should have accented characters
are ASCII only and some long names are spelled in several different ways.

My intention is to make the long names UTF-8 compatible and for the correct
spelling I have used Wikipedia as a source.

# The format of the data

The modified data is currently in the Python files, but more sensible would
be use JSON similar to [eco](https://github.com/niklasf/eco).
