LATEXMK=latexmk
ZIP=zip

all: output.txt
	$(LATEXMK) -pdf  main.tex

Blatt6: all
	mv main.pdf Blatt6TimLuchterhand.pdf


release: Blatt6

output.txt:
	python primeTest.py >> output.txt

clean:
	$(LATEXMK) -c
	rm output.txt
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
