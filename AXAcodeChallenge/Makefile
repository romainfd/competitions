all: *.py
	mkdir -p results/$(PROG)
	for NB in 1 2 3 4 5 6 ; do \
		touch results/$(PROG)/$$NB.json ; \
		NB=$$NB python $(PROG).py < data/$$NB.json > results/$(PROG)/$$NB.json & \
	done
