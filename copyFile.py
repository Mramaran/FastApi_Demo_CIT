from_file="textFile1.txt"
to_file="textFile3.txt"
print(F"Copying from {from_file} to {to_file}")
in_file=open(from_file)
indata=in_file.read()

print(f"The input file is {len(indata)} bytes long")
out_file=open(to_file,'w')
out_file.write(indata)
print("All done")
out_file.close()
in_file.close()