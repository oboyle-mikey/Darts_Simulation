# VERSION 7 - Loop through each day and click into each match and collect data reformatting leg wins

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver_location = "/Users/michaeloboyle/Documents/MSISS_Year_4/FYP/Chromedriver/chromedriver"  # chormedriver
# service_args = ['--proxy=ppwebsense3.inhouse.paddypower.com']
driver = webdriver.Chrome(driver_location)  # , service_args=service_args)

#url = """http://cs.betradar.com/sportcenter/darts"""

time.sleep(5)

#Start Date for Test
#url = """http://cs.betradar.com/sportcenter/darts#matchId=16494005"""

#Start Date for Test on 9 dart leg win
url = """http://cs.betradar.com/sportcenter/darts#matchId=16100676"""

driver.get(url)

# LOOP Structure

days = 0
day_limit = 5

time.sleep(5)

#Start Timer
start_time = time.time()

#yesterday = WebDriverWait(driver, 1).until((lambda driver: driver.find_elements_by_xpath(str(
#            """/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div"""))))

yesterday = WebDriverWait(driver, 10).until((lambda driver: driver.find_elements_by_xpath(str(
            """/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]"""))))
    
international_button = WebDriverWait(driver, 10).until((lambda driver: driver.find_elements_by_xpath(str(
        """/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div"""))))

international_button[0].click()

time.sleep(5)

while days < day_limit:
    
    z = 1
    
    z_text = str(z)
    
    leave = False
    
    while not leave:
        
        z_text = str(z)
        
        try:
            
            print("a")
            
            #----- Select Match From Dropdown
            match = WebDriverWait(driver, 1).until((lambda driver: driver.find_elements_by_xpath(str(
                    """/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[""" + z_text + """]"""))))
            
            match[0].click()
            
            time.sleep(5)
            
            #----- Collect Basic Match Information
            
            home = WebDriverWait(driver, 10).until((lambda driver: driver.find_elements_by_xpath(str(
                    """//td[@class="sr-cl sr-half sr-home"]"""))))

            away = WebDriverWait(driver, 10).until((lambda driver: driver.find_elements_by_xpath(str(
                    """//td[@class="sr-cl sr-half sr-event-text sr-away"]"""))))
            
            score = WebDriverWait(driver, 10).until((lambda driver: driver.find_elements_by_xpath(str(
                    """//td[@class="sr-cl sr-score sr-score-change sr-wide"]""")))) 
            
            print("b")
            
            #----- Set Initial Variable States
            i = 0
            k = len(home)
            l = len(away)
            
            if k >= l:
                i = k
            else:
                i = l
            
            leg = 1
            sets = 1
            visit = 0
            counter = 0
            
            data_frame = pd.DataFrame()
            dtf = ""
            
            print("c")
            
            #Initialise Variable Fields
            Competition = []
            Date = []
            Format = []
            Player = []
            Opponent = []
            Set = []
            Leg = []
            Visit = []
            Score_Remaining = []
            Score_Thrown = []
            Dart_Scores = []
            Checkout = []
            Leg_Won = []
            Match_Average = []
            Match_Checkout = []
            Match_180 = []
            DTF = []
            
            #----- Loop through each match event ------

            while i > 1:
                
                
                        #----- Date and Competition -----
                
                        competition = WebDriverWait(driver, 20).until((lambda driver: driver.find_elements_by_xpath(str(
                                """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[6]/div[1]/div[1]"""))))
                        
                        Competition.append(competition[0].text)
                        
                       
                        date = WebDriverWait(driver, 20).until((lambda driver: driver.find_elements_by_xpath(str(
                                """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[6]/div[1]/div[2]/div[1]"""))))
                        
                        Date.append(date[0].text.split(", ")[1])
                        
                        print("d")
                        
            
                        #----- Player A Stats -----
                        player_a = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/table/tbody/tr[""" + str(i) + """]/td[1]/div[1]/div[2]""")))
                        
                        player_a_name = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/span[1]""")))
                        
                        player_a_match_avg = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]""")))
                        
                        player_a_match_co = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/div[1]/div[1]/div[1]""")))
                        
                        player_a_180 = WebDriverWait(driver, 100).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/div[1]/div[1]/div[1]""")))
            
                        #----- Player B Stats ------
                        player_b = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/table/tbody/tr[""" + str(i) + """]/td[5]""")))
                        
                        player_b_name = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/span[1]""")))
                        
                        player_b_match_avg = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]""")))
             
                        player_b_match_co = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/div[1]/div[2]/div[1]""")))
                        
                        player_b_180 = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/div[1]/div[2]/div[1]""")))
            
                        #----- Match Format ------
                        format_test = WebDriverWait(driver, 10).until((lambda driver: driver.find_element_by_xpath(
                            """/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div[5]/div[2]/span""")))
                        
                        print("e")
                        
                        #----- Increment set counter ------
                        if player_a.text[0:7] == "Set won":
                            sets += 1
                            leg = 1
                            i -= 1
                            continue
                        elif player_b.text[0:7] == "Set won":
                            sets += 1
                            leg = 1
                            i -= 1
                            continue
                        else:
                            pass
                        

                        print("f")
                        
                        #----- Set format for the match -----
                        if format_test.text == " - ":
                            fmt = "Legs"
                        elif format_test.text == "-":
                            fmt = "Legs"
                        else:
                            fmt = "Sets"
            
                        Format.append(fmt)
                        
                        print("g")
            
                        #----- Counter of loop -----
                        if counter == 0:
                            visit += 1
                        else:
                            pass
                        
            
                        #----- Append set, leg, and visit to database -----
                        Set.append(sets)
                        Leg.append(leg)
                        Visit.append(visit)
                        
                        print("h")
                        
                        #----- Extract previous scores -----
                        if player_a.text[0:7] == "Leg won":
                            previous_score_a = player_a.text.split(". ")[1][0:3]
                            a_dtf = player_a.text.split("Leg won")[1][2:4]
                            previous_score_b = "501"
                        elif player_b.text[0:7] == "Leg won":
                            previous_score_b = player_b.text.split(". ")[1][0:3]
                            b_dtf = player_b.text.split("Leg won")[1][2:4]
                            previous_score_a = "501"
                        else:
                            try:
                                previous_score = str(score[i].text).split("-", 1)
                                previous_score_a = str(previous_score[0])
                                previous_score_b = str(previous_score[1])
                                a_dtf = ""
                                b_dtf = ""
                            except:
                                previous_score_a = "501"
                                previous_score_b = "501"
            
                        print("i")
                        #----- Visit record for player b -----
                        if player_a.text == "":
            
                            counter += 1
                            # print player_b_name.text + ": " + previous_score_b + ": " + player_b.text.split(" points")[0] + " :" + player_b.text.split(" points")[1]
                            Player.append(player_b_name.text)
                            Opponent.append(player_a_name.text)
                            # print player_a_name.text
                            if visit == 1:
                                previous_score_a = "501"
                                previous_score_b = "501"
                            else:
                                pass
            
                            print("j")
                            
                            # ************* Issue with score_remaining when the leg is won, previous_score_b contains #Darts To Win
                            Score_Remaining.append(previous_score_b.strip())
                            
                            
                            if player_b.text.split(" points")[0][0:9] == "Leg won":
                                dtf = (player_b.text[9:11])
                                st = ((player_b.text.split(" points")[0][9:])[-3:]).strip()
                            elif (player_b.text[0:4]).strip() == "Bust":
                                st = 0
                            elif ' ' in ((player_a.text.split(" points")[0])[-3:]).strip():
                                ((player_a.text.split(" points")[0])[-2:]).strip()
                            else:
                                st = ((player_b.text.split(" points")[0])[-3:]).strip()
                            
                            print("k")
                            
                            Score_Thrown.append(st)
                            DTF.append(b_dtf.strip())
                            
                            try:
                                Dart_Scores.append(player_b.text.split(" points")[1])
                            except:
                                Dart_Scores.append(" ")
                                
                            print("l")
                            
                            Match_Average.append(player_b_match_avg.text)
                            Match_Checkout.append(player_b_match_co.text)
                            Match_180.append(player_b_180.text)
            
                        #----- Visit record for player a -----
                        elif player_b.text == "":
            
                            counter += 1
                            # print player_a_name.text + ": " + previous_score_a + ": " + player_a.text.split(" points")[0] + " :" + player_a.text.split(" points")[1]
                            Player.append(player_a_name.text)
                            Opponent.append(player_b_name.text)
                            # print player_b_name.text
                            if visit == 1:
                                previous_score_a = "501"
                                previous_score_b = "501"
                            else:
                                pass
                            
                            print("m")
                            
                            # ************* Issue with score_remaining when the leg is won, previous_score_b contains #Darts To Win
                            Score_Remaining.append(previous_score_a.strip())
                            
                            print("n")
                            
                            
                            
                            print("o")
                            
                            if player_a.text.split(" points")[0][0:9] == "Leg won":
                                dtf = (player_a.text[9:11])
                                st = ((player_a.text.split(" points")[0][9:])[-3:]).strip()
                            elif (player_a.text[0:4]).strip() == "Bust":
                                st = 0
                            elif ' ' in ((player_a.text.split(" points")[0])[-3:]).strip():
                                ((player_a.text.split(" points")[0])[-2:]).strip()
                            else:
                                st = ((player_a.text.split(" points")[0])[-3:]).strip()
            
             
                            Score_Thrown.append(st)
                            DTF.append(a_dtf.strip())
                                
                            try:
                                Dart_Scores.append(player_a.text.split(" points")[1])
                            except:
                                Dart_Scores.append(" ")
                                
                            print("o")
                            
                            Match_Average.append(player_a_match_avg.text)
                            Match_Checkout.append(player_a_match_co.text)
                            Match_180.append(player_a_180.text)
            
                        else:
                            pass
            
                        print("j")
                        
                        if counter == 2:
                            counter = 0
                        else:
                            pass

            
                        #----- Checkout if leg finished -----
                        if player_a.text[0:7] == "Leg won":
                            leg += 1
                            visit = 0
                            counter = 0
                            Checkout.append("Y")
                            previous_score_a = "501"
                            previous_score_b = "501"
                            # print " "
                        elif player_b.text[0:7] == "Leg won":
                            leg += 1
                            visit = 0
                            counter = 0
                            Checkout.append("Y")
                            previous_score_a = "501"
                            previous_score_b = "501"
                            # print " "
                        else:
                            Checkout.append("N") 
            
                        i -= 1
                        
                        print("Record")
                            
                        print("k")
                
            #----- Create dataframe from appended lists -----
            data_frame['Competition'] = pd.Series(Competition)
            data_frame['Date'] = pd.Series(Date)
            data_frame['Player'] = pd.Series(Player)
            data_frame['Opponent'] = pd.Series(Opponent)
            data_frame['Format'] = pd.Series(Format)
            data_frame['Set'] = pd.Series(Set)
            data_frame['Leg'] = pd.Series(Leg)
            data_frame['Visit'] = pd.Series(Visit)
            data_frame['Score_Remaining'] = pd.Series(Score_Remaining)
            data_frame['Score_Thrown'] = pd.Series(Score_Thrown)
            data_frame['Dart_Scores'] = pd.Series(Dart_Scores)
            data_frame['Checkout'] = pd.Series(Checkout)
            data_frame['Match_Average'] = pd.Series(Match_Average)
            data_frame['Match_Checkout'] = pd.Series(Match_Checkout)
            data_frame['Match_180'] = pd.Series(Match_180)
            data_frame['DTF'] = pd.Series(DTF)
            
            #----- Write dataframe to csv
            fileStr = str("/Users/michaeloboyle/Documents/MSISS_Year_4/FYP/European_Champs_2018/" + Player[0]) + " v " + str(Opponent[0]) + ".csv"
            data_frame.to_csv(
                fileStr,
                encoding='cp1252', index=False, header=False)
            
            
            #----- Print Succesful Collection
            
            print("Collected " + fileStr)
            
            z += 1
            
        except:
            leave = True
            pass
        
    yesterday[0].click()
    
    time.sleep(10)
    
    print("---- %s seconds day ----" % (time.time() - start_time))
    
    days += 1

print("---- %s seconds ----" % (time.time() - start_time))
