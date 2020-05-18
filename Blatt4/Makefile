LATEXMK=latexmk
ZIP=zip

all:
	$(LATEXMK) -pdf  main.tex

Blatt4.zip:
	$(ZIP) $@ main.pdf *.py


release: Blatt4.zip


clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
