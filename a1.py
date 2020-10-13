# Name :Manasvi Singh 
# Roll No : 2019369
# Group :1

import datetime
import urllib.request

def getLatestRates():
    """ Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
    """
    url = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
    data = url.read()
    b=data.decode('utf-8')
    return b


def changeBase(amount, currency, desiredCurrency, date):
    """ Outputs: a float value f. If data for particular date is not mentioned then rates for the nearest date are used"""
    m=urllib.request.urlopen("https://api.exchangeratesapi.io/"+date)
    
    data=m.read()
    b=data.decode('utf-8')
    
    
    currency=currency.upper()
    desiredCurrency=desiredCurrency.upper()
    if(b.find(currency)==-1):
        return "THIS CURRENCY IS NOT IN DATABASE"
    if(b.find(desiredCurrency)==-1):
        return "THIS CURRENCY IS NOT IN DATABASE"
    
    if(currency!="EUR" and desiredCurrency!="EUR"):
        Desired=float(b[b.index(desiredCurrency)+5:b.index(",",b.index(desiredCurrency)+5)])
        given_currency=float(b[b.index(currency)+5:b.index(",",b.index(currency)+5)])
        one_currency=Desired/given_currency
        desired_currency_amount=amount*one_currency
        return(desired_currency_amount)
    else:
        if(currency=="EUR" and desiredCurrency!="EUR" ):
            Desired=float(b[b.index(desiredCurrency)+5:b.index(",",b.index(desiredCurrency)+5)])
            
            return amount*Desired
        elif(desiredCurrency=="EUR" and currency!="EUR" ):
            given_currency=float(b[b.index(currency)+5:b.index(",",b.index(currency)+5)])
            return amount/given_currency
        else:
            return float(amount)
            
   

def printAscending(json):
    """ Output: the sorted order of the Rates 
		You don't have to return anything.
	
    Parameter:json: a json string to parse
    """
    a=json.index(":")
    b=json.rindex("base")
    string=json[a+2:b-3]
    LIST=list(string.split(","))
    for i in range(len(LIST)):
        for j in range(0,len(LIST)-i-1):
            
            if float(LIST[j][6:])>float(LIST[j+1][6:]):
                LIST[j],LIST[j+1]=  LIST[j+1],LIST[j]
    for i in range(len(LIST)):
        
        print("1"+json[b+7:b+10],"=",LIST[i][6:],LIST[i][1:4])





def extremeFridays(startDate, endDate, currency):
    """ Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
    """
    m=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)

    data=m.read()
    b=data.decode('utf-8')
    c=b[:b.rindex("start_at")]
    LIST=[]
    LIST1=[]
    start =datetime.datetime.strptime(startDate, "%Y-%m-%d")
    end = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    date_array =(start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
    list
                
    for i in date_array:
        a=i.strftime("%Y-%m-%d")

        if  str(a) in c:
    
            e=b.index(str(a))
            f=b.index("}",e)
            d=b[e+12:f]
    
            INDEX=d.index(currency)
            f=d.index(",",INDEX)
            p=int(str(a)[0:4])
            q=int(str(a)[5:7])
            r=int(str(a)[8:])
            date = datetime.datetime(p,q,r)
            if date.weekday()==4:
                LIST=LIST+[str(a)+d[INDEX:f]]

    for i in range(len(LIST)):
            LIST1=LIST1+[float(LIST[i][15:])]
    NEWSTRING=""
    NEWSTRING=NEWSTRING.join(LIST)
    
    MAX=max(LIST1)
    MIN=min(LIST1)
    FIND_MAX=NEWSTRING.index(str(MAX))
    FIND_MIN=NEWSTRING.index(str(MIN))
    DATE_MAX=NEWSTRING[FIND_MAX-15:FIND_MAX-5]
    DATE_MIN=NEWSTRING[FIND_MIN-15:FIND_MIN-5]

    print(currency+" was strongest on "+str(DATE_MIN)+"."+"1 Euro was equal to "+str((MIN))+" "+currency)
    print(currency+" was weakest on "+str(DATE_MAX)+"."+"1 Euro was equal to "+str((MAX))+" "+currency)



def findMissingDates(startDate, endDate):
    """ Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
    """
    m=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
            
    data=m.read()
    b=data.decode('utf-8')
    LIST=[]


    start =datetime.datetime.strptime(startDate, "%Y-%m-%d")
    end = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    date_array =(start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
            
    for i in date_array:
        a=i.strftime("%Y-%m-%d")

        if str(a) not in b:
            LIST=[a]+[]
            print(a)
    
    if len(LIST)==0:
        print("NO MISSING DATES")

