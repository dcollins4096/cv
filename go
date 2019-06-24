#!/bin/csh

set name = "cv"
#set name = "timeline"
#set name = Development
#set name = publist_only

set this_latex = pdflatex
if( -e /usr/bin/acroread ) then
 set run = "acroread"
else
 set run = "open"
endif    
rm -f *.log *.out *.aux *.dvi *~ *.bbl *.blg
rm -f *.ps  *.bak *.toc *.lof *.lot
rm $name.pdf
if( $1 == "c" ) then
    exit
endif

if( $1 == "o" ) then
    $this_latex $name
else
    
    ls -l
    
    $this_latex $name
    if( $status != 0 ) then
	echo "done borked sompin. Exiting."
	exit
    endif

    if( $1 != "n" && ( -e $name.pdf ) ) $run $name.pdf &
	    

endif
# the end
