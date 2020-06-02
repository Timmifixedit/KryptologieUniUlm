LATEXMK=latexmk
ZIP=zip

all: output.txt
	$(LATEXMK) -pdf  main.tex

Blatt6.zip: all
	$(ZIP) $@ main.pdf *.py


release: Blatt6.zip

output.txt:
	python primeTest.py >> output.txt

clean:
	$(LATEXMK) -c
	rm output.txt
	rm main*.pdf
	rm *.bbl
	rm *.run.xml
