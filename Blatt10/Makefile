LATEXMK=latexmk
ZIP=zip

all:
	$(LATEXMK) -pdf  main.tex

Blatt10: all
	mv main.pdf Blatt10TimLuchterhand.pdf


release: Blatt10

clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
