# Exchange-Rates
Creating functions in python by accessing the data of currency exchange rates from the open source website ​https://api.exchangeratesapi.io/latest​.  
getLatestRates():Returns: a JSON string that is a response to a latest rates query.The JSON string will have the attributes: rates, base and date (yyyy-mm-dd).  
changeBase(amount, currency, desiredCurrency, date):Outputs: a float value f. If data for particular date is not mentioned then rates for the nearest date are used.<br />  printAscending(json):Output: the sorted order of the Rates .You don't have to return anything.(Parameter:json: a json string to parse).    
extremeFridays(startDate, endDate, currency):Output: on which friday was currency the strongest and on which was it the weakest.You don't have to return anything. Parameters: stardDate and endDate: strings of the form yyyy-mm-dd,currency: a string representing the currency those extremes you have to determine.<br />
findMissingDates(startDate, endDate):Output: the dates that are not present when you do a json query from startDate to endDate.You don't have to return anything.(Parameters: stardDate and endDate:strings of the form yyyy-mm-dd). <br />

  
   
 
