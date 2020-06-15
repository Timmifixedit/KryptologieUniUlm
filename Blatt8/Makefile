LATEXMK=latexmk
ZIP=zip

all: output.txt
	$(LATEXMK) -pdf  main.tex

Blatt8: all
	mv main.pdf Blatt8TimLuchterhand.pdf


release: Blatt8

output.txt:
	python blindSignature.py >> output.txt

clean:
	$(LATEXMK) -c
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
