FILE=report
2
2
3
•
4
3
5
all:
6
4
7
        pdflatex ${FILE}
8
5
9
        bibtex ${FILE}
10
6
11
        pdflatex ${FILE}
12
7
13
        pdflatex ${FILE}
14
8
15
•
16
9
17
pack:
18
10
19
        rm -rf ${FILE}
20
11
21
        mkdir ${FILE}
22
12
23
        mkdir ${FILE}/tex
24
13
25
        mkdir ${FILE}/images
26
14
27
        cp ${FILE}.tex ${FILE}
28
15
29
        cp ${FILE}.bib ${FILE}
30
16
31
        cp ${FILE}.pdf ${FILE}
32
17
33
        cp tex/sig-alternate-2013.cls ${FILE}/tex
34
18
35
        cp -r images/*.pdf ${FILE}/images
36
19
37
        tar cvf ${FILE}.tar ${FILE}
38
20
39
•
40
21
41
clean:
42
22
43
        rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut
44
23
45
        rm -rf _region_.*
46
24
47
•
48
25
49
view:
