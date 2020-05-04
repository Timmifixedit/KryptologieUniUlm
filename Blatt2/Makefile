LATEXMK=latexmk
ZIP=zip

all:
	$(LATEXMK) -pdf  main.tex

Blatt1.zip:
	$(ZIP) $@ main.pdf *.py


release: Blatt2.zip


clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
