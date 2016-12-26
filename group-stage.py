#coding: utf-8
from random import randint

class Team(object):
	def __init__(self, name):
		self.name = name
	
	pts = 0
	v = 0
	d = 0
	l = 0

	gs = 0
	gd = 0

def match(team1, team2):
	print "MATCH:"
	print team1.name + " v " + team2.name
	gh = input("Insert the goals scored by " + team1.name + ": ")
	gv = input("Insert the goals scored by " + team2.name + ": ")

	team1.gs += gh
	team2.gs += gv
	team1.gd += gh - gv
	team2.gd += gv - gh
	
	if gh > gv:
		team1.pts += 3
		team1.v += 1
		team2.l += 1
	elif gv > gh:
		team2.pts += 3
		team2.v += 1
		team1.l += 1
	elif gv == gh:
		team1.pts += 1
		team1.d += 1
		team2.pts += 1
		team2.d += 1
	print

def teamname(t):
	tname = raw_input("Team name: ")
	t.name = tname
	tname = ' '

def addTeam(quant):
	teamlist = []
	
	#Cria lista de objetos
	for i in range(quant):
		teamlist.append(Team(i))
		teamname(teamlist[i])
	
	return teamlist

def schedule(teamlist):
	for i in range(len(teamlist)):
		pv = teamlist[i]
		for j in range(len(teamlist)):
			if teamlist[i] == teamlist[j]:
				pass
			else:
				match(teamlist[i], teamlist[j])

def sortTable(teamlist):
	#Organiza os times de acordo com os pontos conquistados
	newlist = sorted(teamlist, key=lambda team: team.pts, reverse=True)

	for i in range(len(newlist) - 1):
		temp = Team(' ')
		newlist.append(temp)
		if newlist[i].pts == newlist[i + 1].pts:
			if newlist[i + 1].gd > newlist[i].gd:
				aux = newlist[i]
				newlist[i] = newlist[i + 1]
				newlist[i + 1] = aux
			elif newlist[i + 1].gd < newlist[i].gd:
				pass
			elif newlist[i + 1].gd == newlist[i].gd:
				if newlist[i + 1].gs > newlist[i].gs:
					aux = newlist[i]
					newlist[i] = newlist[i + 1]
					newlist[i + 1] = aux
				elif newlist[i + 1].gs < newlist[i].gs:
					pass
				elif newlist[i + 1].gs == newlist[i].gs:
					luck = randint(0, 1)
					if luck == 1:
						aux = newlist[i]
						newlist[i] = newlist[i + 1]
						newlist[i + 1] = aux
		newlist.remove(temp)
				
	return newlist

def showTable(n):
	print "TABLE: "
	print "Team \t\t Pts \t W \t D \t L \t GS \t GD"
	for i in range(n):
		print newlist[i].name + ": \t" + str(newlist[i].pts) + "\t" + str(newlist[i].v) + "\t" + str(newlist[i].d) + "\t" + str(newlist[i].l) + "\t" + str(newlist[i].gs) + "\t" + str(newlist[i].gd)


group = addTeam(4)
schedule(group)
newlist = sortTable(group)
showTable(len(newlist))

