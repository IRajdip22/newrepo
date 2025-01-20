import pandas
import datetime
import csv


dict1 = {}
def takeUserDay():
    try:
        day = int(input('Enter the day : '))
        if day != str:
            if day <= 0 or day >= 31:
                print('Enter a valid day!') 
                return takeUserDay()
            else:
                return day
    except:
        print('ERROR: Enter numerical value only!')
        return takeUserDay()        
        
def takeUserMonth():
    month = input('Enter the month : ')
    if month == 'January' or month == 'january' or month == 'Jan' or month == 'jan' or month == '1' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month == 'February' or month == 'february' or month == 'Feb' or month == 'feb' or month == '2' or month == '02':
        monthNumber = 2
        return monthNumber
    elif month == 'March' or month == 'march' or month == 'Mar' or month == 'mar' or month == '3' or month == '03':
        monthNumber = 3
        return monthNumber
    elif month == 'April' or month == 'april' or month == 'Apr' or month == 'apr' or month == '4' or month == '04':
        monthNumber = 4
        return monthNumber
    elif month == 'May' or month == 'may' or month == '5' or month == '05':
        monthNumber = 5
        return monthNumber
    elif month == 'June' or month == 'june' or month == 'Jun' or month == 'jun' or month == '6' or month == '06':
        monthNumber = 6
        return monthNumber
    elif month == 'July' or month == 'july' or month == 'Jul' or month == 'jul' or month == '7' or month == '07':
        monthNumber = 7
        return monthNumber
    elif month == 'August' or month == 'august' or month == 'Aug' or month == 'aug' or month == '8' or month == '08':
        monthNumber = 8
        return monthNumber
    elif month == 'September' or month == 'september' or month == 'Sep' or month == 'sep' or month == '9' or month == '09':
        monthNumber = 9
        return monthNumber
    elif month == 'October' or month == 'october' or month == 'Oct' or month == 'oct' or month == '10':
        monthNumber = 10
        return monthNumber
    elif month == 'November' or month == 'november' or month == 'Nov' or month == 'nov' or month == '11':
        monthNumber = 11
        return monthNumber
    elif month == 'December' or month == 'december' or month == 'Dec' or month == 'dec' or month == '12':
        monthNumber = 12
        return monthNumber
    else:
        print('Enter a valid month!')
        return takeUserMonth()
    
def takeUserYear():
    try:
        year = int(input('Enter the year : '))
        if year != str:
            if year <= 0:
                print('Error: Enter a valid year!') 
                return takeUserYear()
            elif year%4 == 0:
                print('Leap year!')
                return year
            else:
                return year
    except:
        print('ERROR: Enter numerical value only')
        return takeUserYear()
    
def calculateSign(day,month):
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
        
    return astro_sign

def takeDate(year,month,day):
    date1=datetime.date(year,month,day)
    print('DOB: ',date1)
    return date1




def repeatQuestion():
    Finder=input('Do you want to find any other Zodiac sign(yes/no): ')
    if Finder =='yes':
        return True
    else:
        return False
 
def UserInput(count):
    userName = input('Enter your name : ')
    userYear = takeUserYear()
    userMonth = takeUserMonth()
    userDay = takeUserDay()
    fullDate = takeDate(userYear, userMonth, userDay)
    your_zodiac_sign = calculateSign(userDay, userMonth)
    print(userName,'Your Zodiac sign is : ',your_zodiac_sign)
    dict1[count] = {"FullName":"","DOB":"","ZodiacSign":""}
    dict1[count]["FullName"] = userName
    dict1[count]["DOB"] = fullDate
    dict1[count]["ZodiacSign"] = your_zodiac_sign

    print(dict1[count])

def Savetopandas():
    pass

if __name__=='__main__':
    Repeat = True
    Count = 1
    while Repeat == True:
        UserInput(Count)
        Count +=1
        Repeat = repeatQuestion()
    df = pandas.DataFrame(data=dict1)
    fileName = input('PLease enter file Name:   ')
    savedData = df.to_csv(fileName +'.csv', index = True)
    print(df)

