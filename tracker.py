import sys
import datetime
import os.path
from os import path



args = sys.argv

tasks = []
x = str(datetime.datetime.now().date())
num = 0

try:
	command = args[1]
except IndexError:
	print("Usage :-\n"
"$ ./todo add \"todo item\"  # Add a new todo\n"
"$ ./todo ls               # Show remaining todos\n"
"$ ./todo del NUMBER       # Delete a todo\n"
"$ ./todo done NUMBER      # Complete a todo\n"
"$ ./todo help             # Show usage\n"
"$ ./todo report           # Statistics")
	sys.exit()

if command not in ("help", "add", "del", "done","report", "ls"):
	print("Invalid command\n Use help/add/del/done/report/ls")
	sys.exit()

if command == "help":
	print("Usage :-\n"
"$ ./todo add \"todo item\"  # Add a new todo\n"
"$ ./todo ls               # Show remaining todos\n"
"$ ./todo del NUMBER       # Delete a todo\n"
"$ ./todo done NUMBER      # Complete a todo\n"
"$ ./todo help             # Show usage\n"
"$ ./todo report           # Statistics")
	sys.exit()

if command == "add":
	try:
		content = args[2]
	except IndexError:
		print("Error: Missing todo string. Nothing added!")
		sys.exit()
	file = open("todo.txt", "a")
	task = content
	file.write(task+"\n")
	file.close()
	print("Added todo: "+"\""+content+"\"")

elif command == "del":
	try:
		coll = args[2]
	except IndexError:
		print("Error: Missing NUMBER for deleting todo.")
		sys.exit()
	try:
		file = open("todo.txt", "r")
	except IOError as e:
		print(str(e))
		sys.exit()
		
	coll = int(coll)
	Counter = 1 
	with open("todo.txt", "r") as f:
		lines = f.readlines()
	with open("todo.txt", "w") as f:
		for line in lines:
			if Counter != coll:
				f.write(line)
			else:
				print("Deleted todo #"+str(coll))
			Counter += 1
		Counter -= 1
		if coll > Counter:
			print("Error: todo #"+str(coll)+" does not exist. Nothing deleted.")
		elif coll < 1:
			print("Error: todo #"+str(coll)+" does not exist. Nothing deleted.")
elif command == "done":
	try:
		file = open("todo.txt", "r")
	except IOError as e:
		print(str(e))
		sys.exit(1)
	try:
		coll = int(args[2])
	except IndexError:
		print("Error: Missing NUMBER for marking todo as done.")
		sys.exit()	

	Counter = 1 
	with open("todo.txt", "r") as f:
		lines = f.readlines()
	with open("done.txt", "a") as fa:
		for line in lines:
			if Counter == coll:
				fa.write(x +" "+ line)
				fa.close()
				print("Marked todo #"+str(coll)+" as done.")
			Counter += 1
		Counter -= 1
		if coll > Counter:
			print("Error: todo #"+str(coll)+" does not exist.")
		elif coll < 1:
			print("Error: todo #"+str(coll)+" does not exist.")
	coll = int(args[2])
	Counter = 1 
	with open("todo.txt", "r") as f:
		lines = f.readlines()
	with open("todo.txt", "w") as f:
		for line in lines:
			if Counter != coll:
				f.write(line)
			Counter += 1

elif command == "report":
	try:
		file = open("todo.txt", "r")
	except IOError as e:
		print(str(e))
		sys.exit(1)
	with open("todo.txt", "r") as f:
		todo = f.readlines()
	with open("done.txt", "r") as f:
		done = f.readlines()
	print(x+" Pending : "+str(len(todo))+" Completed : "+str(len(done)))	


elif command == "ls":
	if path.exists("todo.txt") == False:
		print("There are no pending todos!")
		sys.exit()
	else:	
		file = open("todo.txt", "r")
		tasks = file.readlines()
		Counter = len(tasks)
		content = []
		for i in range(len(tasks)):
			content.append(tasks[i])

		x = int(len(tasks))
		stripped_line = [s.rstrip() for s in content]	
		for i in range(len(tasks)):
			print('['+str(Counter)+'] '+str(stripped_line[x-1]))
			Counter -=1	
			x -=1
		file.close()
else:
	print("invalid command!")
