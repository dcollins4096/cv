import urllib #request, urllib.error, urllib.parse
import re
import sys
from bs4 import BeautifulSoup
citation_re = re.compile(r'.*Citations to the Article \(([^)]+)\)')
def get_citations(ID):
    url = 'http://adsabs.harvard.edu/abs/%s'%ID
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    atags = soup('a')
    CitationCount = '0'
    for a in atags:
        if a.string is not None:
            match = citation_re.match(a.string)
            if match != None:
                CitationCount=match.group(1)
    return CitationCount

def ref_loop(ref_file,verbose):
    if verbose:
        print("open", ref_file)
    fptr = open(ref_file,'r')
    lines=fptr.readlines()
    fptr.close()

    Output=[]

    count_re = re.compile(r'\\citeform{(.*)}%(.*)')

    fptr = open(ref_file,'w')
    try:
        for line in lines:
            if verbose:
                print(line[:-1])
            match= count_re.match(line)
            if match != None:
                PresentCount=match.group(1)
                ID = match.group(2).strip()
                count = get_citations(ID)
                fptr.write('\\citeform{%s}%s%s\n'%(count,'%',ID))
                print('\\citeform{%s}%s%s'%(count,'%',ID))
            else:
                fptr.write(line)
    except:
        raise
    finally:
        fptr.close()



if __name__ == '__main__':
    verbose = False
    if len(sys.argv) > 1:
        print(sys.argv)
        if sys.argv[1] == "-v":
            verbose = True
    ref_loop('publist.tex',verbose)
