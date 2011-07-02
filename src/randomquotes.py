"""
A random quote generator. Useful to put a call into at the end of your bashrc
"""
import sys,os,commands,random,time

#seed the time
random.seed(time.time())

def getquotes(infilenam):
    """A quote generator that parses a file of human readable quotes.
    
    The infilename is the name of the file to read. The quotes are stored in 
    the format <quote text> -- <author> on one line."""
    quotelist = []
    infile = open( infilenam, "rb" )
    #TODO could maybe pick a line in file and only read that one?
    for line in infile:
        if line.startswith('\n'):
            continue
        else:
            line = line.rstrip("\n")
            quotelist.append(line.split("--"))
    numquotes = len(quotelist)
    quotenum = random.randint(0, numquotes-1)
    quote = quotelist[quotenum]
    print (quote[0])#the quote
    print "\t --"+(quote[1])#the author

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Usage:  python <scriptname> <quotesfile>"
        sys.exit(1)
    getquotes(sys.argv[1])
