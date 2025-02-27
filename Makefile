all:
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

review:
	pdflatex review.tex
	bibtex review
	pdflatex review.tex
	pdflatex review.tex

clean:
	rm -f *.aux *.bbl *.blg *.out *.log
