filename = "sample2.txt"
print "File content will be deleted. Are you sure?"
print "Type \"y\" to continue\nor \"n\" to cancel"
yes_no = raw_input(">")
if yes_no=="n":
    print "cancelled\n\n"
    quit()

target_file = open(filename,'w')
target_file.truncate()
target_file.write("well well well")
target_file.write("\n")
target_file.write("o la")
print "ok file contents changed"
# we must close file
target_file.close()
