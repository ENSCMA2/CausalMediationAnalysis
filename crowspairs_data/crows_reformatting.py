with open("crows_reformatted.txt", "w") as o:
	with open("crows_pairs.txt", "r") as p:
		for line in p.readlines():
			if "race-color" in line:
				o.write(",".join(line.split(",")[1:]).split("stereo")[0] + "\n")
