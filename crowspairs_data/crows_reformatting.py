with open("crows_reformatted.txt", "w") as o:
	with open("crows_pairs.txt", "r") as p:
		for line in p.readlines():
			o.write(line.split(",")[1] + "\n")
