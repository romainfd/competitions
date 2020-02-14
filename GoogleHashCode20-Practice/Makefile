all: *.py
	mkdir -p results/$(PROG)
	for NB in 1 2 3 4 5 ; do \
		touch results/$(PROG)/$$NB.txt ; \
		python $(PROG).py < data/$$NB.in > results/$(PROG)/$$NB.txt ;  \
	done

target:
	for number in 1 2 3 4 ; do \
        echo $$number ; \
    done

line: *.py *.txt
	python line.py < ex$(NB)_$(TYPE).txt

create:
	touch pb$(PROG).py
	touch pb$(PROG).txt