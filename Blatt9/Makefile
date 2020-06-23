LATEXMK=latexmk
ZIP=zip

all:
	$(LATEXMK) -pdf  main.tex

Blatt9: all
	mv main.pdf Blatt9TimLuchterhand.pdf


release: Blatt9

clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
