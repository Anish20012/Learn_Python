import sys

full_name="".join(sys.argv[1:])

email = full_name.lower().replace(" ",".") + "@ak.com"

print("generated emailid:", email)
print("name:", full_name)
print ()