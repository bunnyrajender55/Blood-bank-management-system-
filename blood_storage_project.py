import pickle
def blood_options():
	global dict
	global blood_opt
	global blood_grp
	
	while(1):
		print("Select blood group of the person plz Enter one option:")
		dict={1:"A+",2:"B+",3:"AB+",4:"O+",5:"A-",6:"B-",7:"AB-",8:"O-"}
		for i in dict.keys():
			print(" %d).%s"%(i,dict[i]))
		blood_opt=input("Enter blood number:")
		if(blood_opt.isdigit()):
					if(int(blood_opt)>0 and int(blood_opt)<9):
						break
					else:
						print("Enter only correct number")
		else:
				print("Enter only digits")
	blood_grp=dict[int(blood_opt)]
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
def unlock():
	xx=open("Blood_Encription","rb")
	yy=pickle.load(xx)
	i=3
	while(i>0):
		print("You have %d chances"%(i))
		i=i-1
		password=input("Enter possword to Unlock::")
		if(yy[0]==password):
			print("You successfully Unlocked\n*************************************")
			break
		else:
			print("Password is incorrect ...")
	else:
		print("If you forget your password Enter 1 else enter 0:")
		mmm=1
		while(1 and mmm):
			pass_forget=input("Enter your option:")
			if(pass_forget.isdigit()):
				pass_forget=int(pass_forget)
				if(pass_forget==1):
					nickname=input("Enter your nick name first to change password:")
					if(yy[1]==nickname):
						password1=input("Enter your new password:")
						mkm=open("Blood_Encription","wb")
						pickle.dump([password1,nickname],mkm)
						mkm.close()
						print("Successfully password seted\n****************************************")
						break
					else:
						print("Incorrect nick name")
						print("if you want to change password \nthen ur data will be deleted")
						print("if you want to change password then\n enter 1 else enter 0")
						while(1):
							po=input("Enter ur option:")
							if(po=='0'):
								assert not(po=='0'),"******************************************\n\n********PLZ TRY AGAIN ONCE*******"
								break
							elif(po=='1'):
								pass1=input("Enter new password:")
								nick2=input("Enter your nick name:")
								xxx=open("cse.dat","wb")
								a=[]
								b=["STATE","DISTRICT","MONDAL","VILLAGE","NAME","PHONE_NUMBER","Age","Blood_grp","Donar/Accepter","Blood_ml"]
								a.append(b)
								pickle.dump(a,xxx)
								xxx.close()
								aaa=[]
								bbb=["A+","B+","AB+","O+","A-","B-","AB-","O-","Donat/accepter","Name"]
								ccc=[0,0,0,0,0,0,0,0,"---","---"]
								aaa.append(bbb)
								aaa.append(ccc)
								xx123=open("Blood_amount.dat","wb")
								pickle.dump(aaa,xx123)
								xx123.close()
								xxyy=open("Blood_Encription","wb")
								pickle.dump([pass1,nick2],xxyy)
								xxyy.close()
								print("Data is deleted and password successfully changed\n**********************************************************")
								mmm=0
								break
							else:
								print("Enter correct option::")
						
								
						
				elif(pass_forget==0):
					print("Then ok")
					assert not(pass_forget==0),"****************************\n\n***************TRY AGAIN******************"
					break
				else:
					print("Enter correct option")
			else:
				print("Enter only digits")
try:
	xx=open("Blood_Encription","rb")
	xx.close()
except:
	print("First set your password")
	password2=input("Enter password:")
	print("Enter your nick name:")
	nick=input("Enter nick name :")
	xx=open("Blood_Encription","wb")
	pickle.dump([password2,nick],xx)
	xx.close()
	print("Successfully password Seted")
unlock()
try:
	xx123=open("Blood_amount.dat","rb")
	xx123.close()
except:
	aaa=[]
	bbb=["A+","B+","AB+","O+","A-","B-","AB-","O-","Donat/accepter","Name"]
	ccc=[0,0,0,0,0,0,0,0,"---","---"]
	aaa.append(bbb)
	aaa.append(ccc)
	xx123=open("Blood_amount.dat","wb")
	pickle.dump(aaa,xx123)
	xx123.close()
	
try:
	x=open("cse.dat","rb")
except:
	x=open("cse.dat","wb")
	a=[]
	b=["STATE","DISTRICT","MONDAL","VILLAGE","NAME","PHONE_NUMBER","Age","Blood_group","Donar/Accepter","Blood in ml"]
	a.append(b)
	pickle.dump(a,x)
x.close()
x=open("cse.dat","rb")
m=pickle.load(x)
x.close()
def deletelast():
	try:
		e=m[1]
		f=m.pop()
	except:
		print("There is no any record")
		return
	x=open("cse.dat","wb")
	pickle.dump(m,x)
	x.close()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print("Successfully deleted last record")
	print("-------That is-------")
	for i in f:
		print(i,end="  ")
def search_phone():
	while(1):
		phone=input("Enter phone Number:")
		if(phone.isdigit()):
			if(len(phone)==10):
				break
			else:
				print("Enter 10 digits number")
		else:
			print("Enter only digits")
	print("%s\t\t%s\t\t%s"%("VILLAGE","NAME","PH_NO"))
	for i in m:
		for j in i:
			if(j==phone):
				global f123
				global k
				global s123
				s123=1
				global full_d
				full_d=i
				f123=i
				k=1
				print("%s\t\t%s\t\t%s"%(i[3],i[4],i[5]))
def search_name():
	while(1):
		o=0
		name=input("Enter Name:")
		for b in range(10):
			if(name.startswith(str(b))):
				o=1
		if(o==1):
			print("Digits are not allowed at starting")
		else:
			break
	print("%s\t\t%s\t\t%s"%("VILLAGE","NAME","PH_NO"))
	name=name.capitalize()
	for i in m:
		e=i[4].find(".")
		if(e==-1):
			t=i[4]
		else:
			t=i[4][e+1:]
		if(name==i[4] or name==i[4][1:].capitalize() or name==t.capitalize()):
			global k
			k=1
			print("%s\t\t%s\t\t%s"%(i[3],i[4],i[5]))
def search_village():
	while(1):
		village=input("Enter Village Name:")
		if(village.isalpha()):
			break
		else:
			print("Enter aplhabets only")
	print("%s\t\t%s\t\t%s\t\t%s"%("MONDAL","VILLAGE","NAME","PH_NO"))
	village=village.capitalize()
	for i in m:
		if(village==i[3]):
			global k
			k=1
			print("%s\t\t%s\t\t%s\t\t%s"%(i[2],i[3],i[4],i[5]))
	
def search_mondal():
	district()
	mondal()
	print("%s\t\t-\t%s\t-\t%s\t-\t%s"%("Mondal","Village","Name","Ph_no"))
	for i in m:
			if(Mondal==i[2]):
				global k
				k=1
				print()
				print("%s\t-\t%s\t-\t%s\t-\t%s"%(i[2],i[3],i[4],i[5]))	
def search_district():
	district()
	print("%s\t- %s\t- %s\t- %s\t- %s"%("District","Mondal","Village","Name","Ph_no"))
	for i in m:
		if(District==i[1]):
			global k
			k=1
			print()
			print("%s\t- %s\t- %s\t- %s\t- %s"%(i[1],i[2],i[3],i[4],i[5]))
	
def district():
	global d
	d={1:"hanmakonda",2:"warangal",3:"karimnagar",4:"siddipeta",5:"khammam"}
	j=1
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	for i in d.values():
		print("%d-%s"%(j,i))
		j=j+1
	while(1):
		global district
		district=input("SELECT DISTRICT:")
		if(district.isdigit()):
			district=int(district)
			if(district<=5 and district>=1):
				break
			else:
				print("Enter correct option")
		else:
			print("Enter only digits")
	global District
	District=d[district]
def mondal():
	global mo
	if(district==1):
		mo={1:"Hanamkonda",2:"Khaazipet",3:"Inavole",4:"Hasanparthy",5:"Velair",6:"Dharmasagar",7:"Elkathurthi",8:"Bheemadevarapalli",9:"Kamalapur",10:"Parkal",11:"Nadikuda",12:"Athmakur",13:"Damera",14:"Shayampet"}
	elif(district==2):
		mo={1:"Chennaraopet",2:"Duggondi",3:"Anantharam",4:"Khanapur",5:"Khila Warangal",6:"Nallabelly",7:"Narsampet",8:"Nekkonda",9:"Parvathagiri",10:"Raiparthy",11:"Sangem",12:"Warangal",13:"Wardhannapet"}
	elif(district==3):
		mo={1:"karimnagar",2:"kothapally",3:"karimnagar Rural",4:"Manakondur",5:"Thimmapur",6:"Ganneruvaram",7:"Gangadhara",8:"Ramadugu",9:"Choppadandi",10:"Chigurumamidi",11:"Huzurabad",12:"Veenavanka",13:"V.Saidapur",14:"Jammikunta",15:"Ellandakunta",16:"Shankarapatnam"}
	elif(district==4):
		mo={1:"Siddipet Rural",2:"Siddipet Urban",3:"Narayanaraopet",4:"Chinnakodur",5:"Nangnoor",6:"Dubbak",7:"Mirdoddi",8:"Thoguta",9:"Doulthabad",10:"Raipole",11:"Kondapak",12:"Gajwel",13:"Jagadevapur",14:"Markook",15:"Wargal",16:"Mulugu",17:"Cherial",18:"Komuravelly",19:"Maddur",20:"Husnabad Urban",21:"Akkannapeta",22:"Koheda",23:"Bejjenki",24:"Dhoolmitta",25:"Akbarpet-Bhoompally",26:"Kukunoorpally"}
	elif(district==5):
		mo={1:"Vemsoor",2:"Yerrupalem",3:"Madhira",4:"Bonakal",5:"Wyra",6:"Thallada",7:"Chinthakani",8:"Nelakondapalle",9:"Mudigonda",10:"Khammam Rural",11:"Kusumanchi",12:"Thirumalayapalem",13:"Penuballi",14:"Sathupalle",15:"Dammapeta",16:"Aswaraopeta",17:"Mulakalapalle",18:"Chandrugonda",19:"Julurpad",20:"Singareni",21:"Garla",22:"Bayyaram",23:"Gundala",24:"Yellandu",25:"Tekulapalle",26:"Kothagudem",27:"Palawancha",28:"Burgampadu",29:"Kukunoor",30:"Vararamachandrapuram",31:"Chintur",32:"Kunavaram",33:"Bhadrachalam",34:"Dummugudem",35:"Aswapuram",36:"Manuguru",37:"Cherla",38:"Venkatapuram",39:"Khammam",40:"Kalluru",41:"Kamepalle"}
	
	j=1
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	for i in mo.values():
		print("%d-%s"%(j,i))
		j=j+1
	while(1):
		global mondal
		mondal=input("SELECT MONDAL:")
		if(mondal.isdigit()):
			mondal=int(mondal)
			try:
				global Mondal
				Mondal=mo[mondal]
			except:
				print("Enter correct option")
			else:
				break
		else:
			print("Enter only digits")
def add():
	while(1):
			state=input("ENTER STATE:")
			if(state.isalpha()):
				break
			else:
				print("Enter only Alphabets")
	district()
	mondal()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		village=input("ENTER VILLAGE:")
		if(village.isalpha()):
			break
		else:
			print("Enter only Alphabets")
	village=village.capitalize()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		o=0
		name=input("ENTER NAME:")
		for b in range(10):
			if(name.startswith(str(b))):
				o=1
		if(o==1):
			print("Digits are not allowed at Starting")
		else:
			break
	name=name.capitalize()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		ph_no=input("ENTER PH_NO:")
		if(ph_no.isdigit()):
			if(len(ph_no)==10):
				if(int(ph_no[0])<=5):
					print("Must be first digit is greatet than 5")
				else:
					break
			else:
				print("Enter 10 digits number")
		else:
			print("Enter only digits")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	if(s123==1):
		pass
	else:
		for i in m:
			for j in i:
				if(ph_no==j):
					print("*-*-*-*-*-*-*-*-*-*-*-*-*")
					print("The Record/Ph_no already exits")
					return
	while(1):
		age=input("Enter age of the Person:")
		if(age.isdigit()):
			if(int(age)>18 and int(age)<150):
				break
			else:
				print("Enter a proper age")
		else:
			print("Enter only digits")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	
	blood_options()
	while(1):
				DA={1:"Donater",2:"Accepter"}
				print("PlZ  select one option")
				print("1-Donater")
				print("2-Accepter")
				type=input("Enter your option:")
				if(type.isdigit()):
					if(int(type)==1 or int(type)==2):
						break
					else:
						print("Enter correct option")
				else:
					print("Enter only digits")
	types=DA[int(type)]
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
			blood_ml=input("Enter how much amount of blood in ML is doneting/Accepting:")
			if(blood_ml.isdigit()):
				if(int(blood_ml)>0):
					break
				else:
					print("Enter properly")
			else:
				print("Enter digits only")
	xx123=open("blood_amount.dat","rb")
	mmm=pickle.load(xx123)
	xx123.close()
	nnn=mmm
	nn=(len(mmm))-1
	ma=mmm[nn]
	ma[8]=types
	ma[9]=name
	if(int(type)==2):
		if(ma[int(blood_opt)-1]<int(blood_ml)):
			print("PLZ CHECK BLOOD AVAILABILITY FIRST ")
			print("BLOOD IS NOT SUFFIEANT")
			return
		ma[int(blood_opt)-1]-=int(blood_ml)
	elif(int(type)==1):
		ma[int(blood_opt)-1]+=int(blood_ml)
	nnn.append(ma)
	xx123=open("blood_amount.dat","wb")
	pickle.dump(nnn,xx123)
	xx123.close()
		
		
	print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
	a=[state,District,Mondal,village,name,ph_no,age,blood_grp,types,blood_ml]
	global v123
	v123=a
	m.append(a)
	x=open("cse.dat","wb")
	pickle.dump(m,x)
	x.close()
	print("successfully added\n")
	print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
def search():
	print("1-SEARCH BY DISTRICT")
	print("2-SEARCH BY MONDAL")
	print("3-SEARCH BY VILLAGE")
	print("4-SEARCH BY NAME")
	print("5-SEARCH BY NUMBER")
	print("6-SEARCH VIA RANDOM")
	global k
	k=0
	while(1):
		search=input("SELECT OPTION:")
		if(search.isdigit()):
			search=int(search)
			if(search>=1 and search<=6):
				break
			else:
				print("Enter correct option")
		else:
			print("Enter only digits")
	if(search==1):
		search_district()
	if(search==2):
		search_mondal()
	if(search==3):
		search_village()
	if(search==4):
		search_name()
	if(search==5):
		search_phone()
	if(search==6):
		while(1):
			random=input("Enter random one:")
			if(random.isdigit()):
				if(len(random)==10):
					break
				else:
					print("Enter 10 digits Number")
			elif(random.isalpha()):
				break
			else:
				print("Enter properly")	
		print("VILLAGE\t\t\tNAME\t\t\tPH_NO")
		for i in m:
			for j in i:
				if(random.capitalize()==j):
					k=1
					print(i[3],"\t\t",i[4],"\t\t",i[5])
	print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
	if(k==0):
		print("No record is founded")
	print("Searching ended")
def full_details():
	search_phone()
	if(s123==1):
		print("Full details are----")
		iii=["STATE","DISTRICT","MONDAL","VILLAGE","NAME","PHONE_NUMBER","Age","Blood_group","Donar/Accepter","Blood in ml"]
		for iiii in range(len(iii)):
			print("  %s            \t       :: %s"%(iii[iiii],full_d[iiii]))
	else:
		print("No record is founded")
def edit():
	search_phone()
	if(s123==1):
		q=open("cse.dat","rb")
		r=pickle.load(q)
		for t in range(len(r)):
			if(r[t]==f123):
				global i123
				i123=t
				print("Enter now updated details")
				add()
				r[t]=v123
				ff=r
				q=open("cse.dat","wb")
				pickle.dump(ff,q)
				break
		q.close()
		print("Sussessfully edited")
	else:
		print("No record Founded")
def statement():
		xx123=open("blood_amount.dat","rb")
		mmm=pickle.load(xx123)
		xx123.close()
		nn=len(mmm)-1
		kkk=0
		while(1):
			sta=input("Enter how many last records statement you want:")
			if(sta.isdigit()):
				if(int(sta)>0):
					if(nn>int(sta)):
						kkk+=(nn-int(sta))
					break
				else:
					print("Enter proper number...")
			else:
				print("Enter only digits")
		rrr=1
		for i in range(nn,kkk,-1):
			print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
			print("now showing last %d th record...."%(rrr))
			print("%s   - %s"%("BLOOD TYPE","AVAILABILITY in ML"))
			for j in range(10):
				print("%s   \t\t-\t %s"%(mmm[0][j],str(mmm[i][j])))
			rrr=rrr+1
			
			
		
		
def blood_available():
		blood_options()
		xx123=open("blood_amount.dat","rb")
		mmm=pickle.load(xx123)
		xx123.close()
		nn=len(mmm)-1
		print("Availabulity of %s blood now is--%d ml"%(blood_grp,mmm[nn][int(blood_opt)-1]))
def all_bloods():
		xx123=open("blood_amount.dat","rb")
		mmm=pickle.load(xx123)
		xx123.close()
		nn=len(mmm)-1
		print("   %s    - %s"%("BLOOD TYPE","AVAILABILITY in ML"))
		for i in range(8):
			print("   %s    \t - %d"%(mmm[0][i],mmm[nn][i]))
		
		
		
print("For add a Donater/Accepter details enter 1")
print("For Search a Doneted person enter 2")
print("For delete last record enter 3")
print("For edit a record enter 4 ")
print("For Get Full details of the of the person enter 5")
print("For check availability of one blood group enter 6")
print("For check availability of All blood groups enter 7")
print("For get the statement enter 8")
f123=[]
v123=[]
s123=0
i123=0
dict={}
blood_grp=" "
blood_opt=" "

full_d=[]
def enter():
   while(1):
    n=input("enter your option:")
    if(n.isdigit()):
    	break
    else:
    	print("enter only digits")
   n=int(n)
   if(n==1):
   	add()
   elif(n==2):
   	search()
   elif(n==3):
   	deletelast()
   elif(n==4):
   	edit()
   elif(n==5):
   	full_details()
   elif(n==6):
   	blood_available()
   elif(n==7):
   	all_bloods()
   elif(n==8):
   	statement()
   else:
   	print("enter correct option")
   	enter()
enter()