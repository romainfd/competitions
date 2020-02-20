all: *.py
	mkdir -p results/$(PROG)
	for NB in 1 2 3 4 5 6 ; do \
		touch results/$(PROG)/$$NB.txt ; \
		python $(PROG).py < data/$$NB.txt > results/$(PROG)/$$NB.txt ; \
	done
