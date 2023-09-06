#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import tkinter as tk

def loadNameFile(filep):
	nameFile = dict()
	
	#read csv file, only use first two columns
	with open(filep) as thefile:
		for line in thefile:
			nameFile.update({line.split("\t")[0] : line.split("\t")[1].replace("\"","").replace(",","")})
	
	return nameFile

#Load names database files
efternamn = loadNameFile("scbnamn2022/efternamn.tsv")
tilltalsnamn_kvinnor = loadNameFile("scbnamn2022/Tilltalsnamn_kvinnor.tsv")
tilltalsnamn_man = loadNameFile("scbnamn2022/Tilltalsnamn_män.tsv")
fornamn_man = loadNameFile("scbnamn2022/förnamn_män.tsv")
fornamn_kvinnor = loadNameFile("scbnamn2022/förnamn_kvinnor.tsv")

def afunction(item):
	nonamefound = True;
	item = item.upper().strip()
	out = ""
	if efternamn.get(item):
		out += "Efternamn: " +  "\t\t" + efternamn.get(item).replace("\"","")  + "\n"
		nonamefound = False;
	if tilltalsnamn_kvinnor.get(item):
		out += "Tilltalsnamn kvinnor: " +  "\t" + tilltalsnamn_kvinnor.get(item) + "\n"
		nonamefound = False;
	if tilltalsnamn_man.get(item):
		out += "Tilltalsnamn män: " +  "\t\t" + tilltalsnamn_man.get(item) + "\n"
		nonamefound = False;
	if fornamn_man.get(item):
		out += "Förnamn män: " +  "\t\t" + fornamn_man.get(item) + "\n"
		nonamefound = False;
	if fornamn_kvinnor.get(item):
		out += "Förnamn kvinnor: " +  "\t\t" + fornamn_kvinnor.get(item) + "\n"
		nonamefound = False;
	if (nonamefound):
		out +=  "Ingen med det namnet i databasen."
	return out

if __name__ == '__main__':	
	def search_action(position=0):
	    query = entry.get()
	    result_label.config(text=query + "\n" + afunction(query))
	
	# Create the main application window
	app = tk.Tk()
	app.title("Namnsök")
	app.geometry("600x400")
	
	# Create and place the search field
	entry = tk.Entry(app)
	entry.pack(pady=20)
	entry.bind("<Return>", search_action)
	entry.bind("<KP_Enter>", search_action)
	
	# Create and place the search button
	search_button = tk.Button(app, text="Search", command=search_action)
	search_button.pack()
	
	# Create and place the result label
	result_label = tk.Label(app, text="", font=("Helvetica", 14), justify="left")
	result_label.pack(pady=20)
	
	# Start the Tkinter main loop
	app.mainloop()

