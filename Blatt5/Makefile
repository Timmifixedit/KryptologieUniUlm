LATEXMK=latexmk
ZIP=zip

all:
	$(LATEXMK) -pdf  main.tex

Blatt5.zip:
	$(ZIP) $@ main.pdf *.py


release: Blatt5.zip


clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
