all: *.py *.txt
	python pb$(PROG).py < pb$(PROG).txt

create:
	touch pb$(PROG).py
	touch pb$(PROG).txt
