# See README.txt file for project4 description

# MCS 260 Fall 2021 Project 4
# Umar Chaudhry
# I attest that all the work done in this program has been done following the policies of the syllabus and project description.
"Create functions to analyze 'videogames.csv' for possible correlations of video game sales and other factors"

import csv

def highestsales(year=2016):
    "print the highest selling game of a given year"
    
    reading = open("videogames.csv","r",encoding="UTF-8",newline="")
    reader = csv.DictReader(reading)
    # assuming 'year' year is an integer
    # make 'year' into a string to compare it to csv data
    year = str(year)
    # make 'large_sale' as initial value to be changed in the following for loop
    large_sale = 0
    for game in reader:
        # if a game released in the specified year and it has the largest global selling
        # add the game's data to 'large_sale' and 'title'
        if game["Year_of_Release"] == year and float(game["Global_Sales"]) > float(large_sale):
            large_sale = game["Global_Sales"]
            title = game["Name"]
    print("{} was the best global selling game of {} with {} million copies sold".format(title,year,large_sale))
    reading.close()


def highestgenres():
    "Order genres from having the highest selling games to lowest"

    reading = open("videogames.csv","r",encoding="UTF-8",newline="")
    reader = csv.DictReader(reading)

    genres = {}
    for game in reader:
        if game["Genre"] not in genres:
            genres[game["Genre"]] = float(game["Global_Sales"])
        elif game["Genre"] in genres:
            genres[game["Genre"]] += float(game["Global_Sales"])
    print("From Highest")
    print()
    # 'gen_list' will be used similarly as a stack
    gen_list = [genres[key] for key in genres]
    # 'maxVal' will be used to print data and remove list indices of 'gen_list'
    maxVal = max(gen_list)
    for i in genres:
        # no more genres to be printed
        if len(gen_list) == 0:
            break
        else:
            for genre in genres:
                if genres[genre] == maxVal:
                    if genre == "":
                        # many games in the csv file aren't given a genre 
                        genre = "Not available genre"
                    print("{} games have {} million games sold".format(genre,maxVal))
                    # remove the previously printed sales count from 'gen_list' so 'max()' will return 
                    # the desired value for the next iteration
                    gen_list.remove(maxVal)
                    try:
                        maxVal = max(gen_list)
                    except:
                        # no more genres to be printed
                        break
    print()
    print("To lowest")
    reading.close()

def highestplatforms():
    "Order Video Game Platforms by highest to lowest based on total game sales"

    reading = open("videogames.csv","r",encoding="UTF-8",newline="")
    reader = csv.DictReader(reading)

    platforms = {}
    for game in reader:
        if game["Platform"] not in platforms:
            platforms[game["Platform"]] = float(game["Global_Sales"])
        else:
            platforms[game["Platform"]] += float(game["Global_Sales"])

    print("From Highest")
    print()
    # 'plat_list' will be used similarly as a stack
    plat_list = [platforms[key] for key in platforms]
    maxVal = max(plat_list)
    for i in platforms:
        # no more platforms to print
        if len(plat_list) == 0:
            break
        else:
            for platform in platforms:
                if platforms[platform] == maxVal:
                    print("The {} console has sold {} million games".format(platform,maxVal))
                    plat_list.remove(maxVal)
                    try:
                        maxVal = max(plat_list)
                    except:
                        # no more platforms
                        break
    print()
    print("To lowest")
    reading.close()

def highestESRB():
    "Order ESRB ratings from highest to lowest based on game sales from each respective rating"

    reading = open("videogames.csv","r",encoding="UTF-8",newline="")
    reader = csv.DictReader(reading)

    ratings = {}
    for game in reader:
        if game["Rating"] not in ratings:
            ratings[game["Rating"]] = float(game["Global_Sales"])
        else:
            ratings[game["Rating"]] += float(game["Global_Sales"])

    print("From Highest")
    print()
    # 'rate_list' will be used similarly as a stack
    rate_list = [ratings[key] for key in ratings]
    maxVal = max(rate_list)
    for i in ratings:
        if len(rate_list) == 0:
            # no more ESRB ratings to print
            break
        else:
            for rating in ratings:
                if ratings[rating] == maxVal:
                    if rating == "":
                        # many games in the csv file aren't given a rating 
                        rating = "a not given rating"
                    print("{} million games with the ESRB rating of {} have been sold.".format(maxVal,rating))
                    rate_list.remove(maxVal)
                    try:
                        maxVal = max(rate_list)
                    except:
                        # no more ESRB ratings
                        break
    print()
    print("To lowest")
    reading.close()

def highestdeveloper():
    """Order the top ten Game Developers from highest to lowest based on total respective game 
    sales of games they've worked on"""

    reading = open("videogames.csv","r",encoding="UTF-8",newline="")
    reader = csv.DictReader(reading)

    developers = {}
    for game in reader:
        if game["Developer"] not in developers:
            developers[game["Developer"]] = float(game["Global_Sales"])
        else:
            developers[game["Developer"]] += float(game["Global_Sales"])

    print("From Highest")
    print()
    # 'dev_list' will be used similarly as a stack
    dev_list = [developers[key] for key in developers]
    maxVal = max(dev_list)
    for i in range(5):
        if len(dev_list) == 0:
            break
        else:
            for developer in developers:
                if developers[developer] == maxVal:
                    if developer == "":
                        # games in the dataset are missing developer info
                        print("Not given developing companys have helped to sell {} million game copies".format(maxVal))
                        dev_list.remove(maxVal)
                        try:
                            maxVal = max(dev_list)
                        except:
                            break
                    else:
                        print("The developing company {} has sold {} million games.".format(developer,maxVal))
                        dev_list.remove(maxVal)
                        try:
                            maxVal = max(dev_list)
                        except:
                            break
    print()
    print("To lowest")
    reading.close()
