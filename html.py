import re
import sys

def ref_loop(ref_file,verbose):
    if verbose:
        print "open", ref_file
    fptr = open(ref_file,'r')
    lines=fptr.readlines()
    fptr.close()

    Output=[]

    count_re = re.compile(r'\\citeform{(.*)}%(.*)')

    fptr = open("publist.html",'w')
    fptr.write("<ul>\n")
    html_temp = ''
    try:
        for line in lines:
            if line[0] not in ['\\','<',"%"] and len(line[:-1]):
                html_temp += line+"<br>"
            if verbose:
                print line[:-1]
            match= count_re.match(line)
            if match != None:
                PresentCount=match.group(1)
                ID = match.group(2).strip()
                url = 'http://adsabs.harvard.edu/abs/%s'%ID

                output = "<li><a href=%s>%s</a></li>"%(url,html_temp)
                fptr.write(output)
                html_temp=''
                #count = get_citations(ID)
                #fptr.write('\\citeform{%s}%s%s\n'%(count,'%',ID))
                #print '\\citeform{%s}%s%s'%(count,'%',ID)

    except:
        raise
    finally:
        fptr.write("</ul>")
        fptr.close()



if __name__ == '__main__':
    verbose = False
    if len(sys.argv) > 1:
        print sys.argv
        if sys.argv[1] == "-v":
            verbose = True
    ref_loop('publist.tex',verbose)
