FILE=report
2
​
3
all:
4
        pdflatex ${FILE}
5
        bibtex ${FILE}
6
        pdflatex ${FILE}
7
        pdflatex ${FILE}
8
​
9
pack:
10
        rm -rf ${FILE}
11
        mkdir ${FILE}
12
        mkdir ${FILE}/tex
13
        mkdir ${FILE}/images
14
        cp ${FILE}.tex ${FILE}
15
        cp ${FILE}.bib ${FILE}
16
        cp ${FILE}.pdf ${FILE}
17
        cp tex/sig-alternate-2013.cls ${FILE}/tex
18
        cp -r images/*.pdf ${FILE}/images
19
        tar cvf ${FILE}.tar ${FILE}
20
​
21
clean:
22
        rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut
23
        rm -rf _region_.*
24
​
25
view:
26
        open ${FILE}.pdf
27
​
28
# all dependce tracking taking care of by Latexmk
29
fast:
30
        latexmk -pdf ${FILE}
31
​
32
watch:
33
        latexmk -pvc -view=pdf ${FILE}
34
​
35
.PHONY: all clean view fast watch
36
​
37
pull:
38
        git pull
39
​
40
up:
41
        git commit -a
42
        git push
43
​
44
publish:
45
        @echo "==============================================================="
46
        @echo "publish ${FILE}.pdf -> http://cyberaide.github.io/papers/${FILE}.pdf" 
47
        @echo "==============================================================="
48
        cp ${FILE}.pdf /tmp
49
        cd ..; git checkout gh-pages
