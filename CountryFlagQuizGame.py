import tkinter as tk
from tkinter import messagebox
import random
from tkinter.simpledialog import askstring

#This dictionary contains pairs (country name, country flag png)
country_dict = {
"Afghanistan":"af.png",
"Aland Islands":"ax.png",
"Albania":"al.png",
"Algeria":"dz.png",
"American Samoa":"as.png",
"Andorra":"ad.png",
"Angola":"ao.png",
"Anguilla":"ai.png",
"Antarctica":"aq.png",
"Antigua and Barbuda":"ag.png",
"Argentina":"ar.png",
"Armenia":"am.png",
"Aruba":"aw.png",
"Australia":"au.png",
"Austria":"at.png",
"Azerbaijan":"az.png",
"Bahamas":"bs.png",
"Bahrain":"bh.png",
"Bangladesh":"bd.png",
"Barbados":"bb.png",
"Belarus":"by.png",
"Belgium":"be.png",
"Belize":"bz.png",
"Benin":"bj.png",
"Bermuda":"bm.png",
"Bhutan":"bt.png",
"Bolivia, Plurinational State of":"bo.png",
"Bonaire, Sint Eustatius and Saba":"bq.png",
"Bosnia and Herzegovina":"ba.png",
"Botswana":"bw.png",
"Bouvet Island":"bv.png",
"Brazil":"br.png",
"British Indian Ocean Territory":"io.png",
"Brunei Darussalam":"bn.png",
"Bulgaria":"bg.png",
"Burkina Faso":"bf.png",
"Burundi":"bi.png",
"Cabo Verde":"cv.png",
"Cambodia":"kh.png",
"Cameroon":"cm.png",
"Canada":"ca.png",
"Cayman Islands":"ky.png",
"Central African Republic":"cf.png",
"Chad":"td.png",
"Chile":"cl.png",
"China[b]":"cn.png",
"Christmas Island":"cx.png",
"Cocos (Keeling) Islands":"cc.png",
"Colombia":"co.png",
"Comoros":"km.png",
"Congo":"cg.png",
"Congo, Democratic Republic of the":"cd.png",
"Cook Islands":"ck.png",
"Costa Rica":"cr.png",
"Côte d'Ivoire":"ci.png",
"Croatia":"hr.png",
"Cuba":"cu.png",
"Curaçao":"cw.png",
"Cyprus[b]":"cy.png",
"Czechia":"cz.png",
"Denmark":"dk.png",
"Djibouti":"dj.png",
"Dominica":"dm.png",
"Dominican Republic":"do.png",
"Ecuador":"ec.png",
"Egypt":"eg.png",
"El Salvador":"sv.png",
"Equatorial Guinea":"gq.png",
"Eritrea":"er.png",
"Estonia":"ee.png",
"Eswatini":"sz.png",
"Ethiopia":"et.png",
"Falkland Islands (Malvinas)[b]":"fk.png",
"Faroe Islands":"fo.png",
"Fiji":"fj.png",
"Finland":"fi.png",
"France":"fr.png",
"French Guiana":"gf.png",
"French Polynesia":"pf.png",
"French Southern Territories":"tf.png",
"Gabon":"ga.png",
"Gambia":"gm.png",
"Georgia":"ge.png",
"Germany":"de.png",
"Ghana":"gh.png",
"Gibraltar":"gi.png",
"Greece":"gr.png",
"Greenland":"gl.png",
"Grenada":"gd.png",
"Guadeloupe":"gp.png",
"Guam":"gu.png",
"Guatemala":"gt.png",
"Guernsey":"gg.png",
"Guinea":"gn.png",
"Guinea-Bissau":"gw.png",
"Guyana":"gy.png",
"Haiti":"ht.png",
"Heard Island and McDonald Islands":"hm.png",
"Holy See":"va.png",
"Honduras":"hn.png",
"Hong Kong":"hk.png",
"Hungary":"hu.png",
"Iceland":"is.png",
"India":"in.png",
"Indonesia":"id.png",
"Iran, Islamic Republic of":"ir.png",
"Iraq":"iq.png",
"Ireland":"ie.png",
"Isle of Man":"im.png",
"Israel":"il.png",
"Italy":"it.png",
"Jamaica":"jm.png",
"Japan":"jp.png",
"Jersey":"je.png",
"Jordan":"jo.png",
"Kazakhstan":"kz.png",
"Kenya":"ke.png",
"Kiribati":"ki.png",
"Korea, Democratic People's Republic of":"kp.png",
"Korea, Republic of":"kr.png",
"Kuwait":"kw.png",
"Kyrgyzstan":"kg.png",
"Lao People's Democratic Republic":"la.png",
"Latvia":"lv.png",
"Lebanon":"lb.png",
"Lesotho":"ls.png",
"Liberia":"lr.png",
"Libya":"ly.png",
"Liechtenstein":"li.png",
"Lithuania":"lt.png",
"Luxembourg":"lu.png",
"Macao":"mo.png",
"Madagascar":"mg.png",
"Malawi":"mw.png",
"Malaysia":"my.png",
"Maldives":"mv.png",
"Mali":"ml.png",
"Malta":"mt.png",
"Marshall Islands":"mh.png",
"Martinique":"mq.png",
"Mauritania":"mr.png",
"Mauritius":"mu.png",
"Mayotte":"yt.png",
"Mexico":"mx.png",
"Micronesia, Federated States of":"fm.png",
"Moldova, Republic of":"md.png",
"Monaco":"mc.png",
"Mongolia":"mn.png",
"Montenegro":"me.png",
"Montserrat":"ms.png",
"Morocco":"ma.png",
"Mozambique":"mz.png",
"Myanmar":"mm.png",
"Namibia":"na.png",
"Nauru":"nr.png",
"Nepal":"np.png",
"Netherlands, Kingdom of the":"nl.png",
"New Caledonia":"nc.png",
"New Zealand":"nz.png",
"Nicaragua":"ni.png",
"Niger":"ne.png",
"Nigeria":"ng.png",
"Niue":"nu.png",
"Norfolk Island":"nf.png",
"North Macedonia":"mk.png",
"Northern Mariana Islands":"mp.png",
"Norway":"no.png",
"Oman":"om.png",
"Pakistan":"pk.png",
"Palau":"pw.png",
"Palestine, State of[b]":"ps.png",
"Panama":"pa.png",
"Papua New Guinea":"pg.png",
"Paraguay":"py.png",
"Peru":"pe.png",
"Philippines":"ph.png",
"Pitcairn":"pn.png",
"Poland":"pl.png",
"Portugal":"pt.png",
"Puerto Rico":"pr.png",
"Qatar":"qa.png",
"Réunion":"re.png",
"Romania":"ro.png",
"Russian Federation":"ru.png",
"Rwanda":"rw.png",
"Saint Barthélemy":"bl.png",
"Saint Helena, Ascension and Tristan da Cunha[d]":"sh.png",
"Saint Kitts and Nevis":"kn.png",
"Saint Lucia":"lc.png",
"Saint Martin (French part)":"mf.png",
"Saint Pierre and Miquelon":"pm.png",
"Saint Vincent and the Grenadines":"vc.png",
"Samoa":"ws.png",
"San Marino":"sm.png",
"Sao Tome and Principe":"st.png",
"Saudi Arabia":"sa.png",
"Senegal":"sn.png",
"Serbia":"rs.png",
"Seychelles":"sc.png",
"Sierra Leone":"sl.png",
"Singapore":"sg.png",
"Sint Maarten (Dutch part)":"sx.png",
"Slovakia":"sk.png",
"Slovenia":"si.png",
"Solomon Islands":"sb.png",
"Somalia":"so.png",
"South Africa":"za.png",
"South Georgia and the South Sandwich Islands":"gs.png",
"South Sudan":"ss.png",
"Spain":"es.png",
"Sri Lanka":"lk.png",
"Sudan":"sd.png",
"Suriname":"sr.png",
"Svalbard and Jan Mayen[e]":"sj.png",
"Sweden":"se.png",
"Switzerland":"ch.png",
"Syrian Arab Republic":"sy.png",
"Taiwan, Province of China[b]":"tw.png",
"Tajikistan":"tj.png",
"Tanzania, United Republic of":"tz.png",
"Thailand":"th.png",
"Timor-Leste":"tl.png",
"Togo":"tg.png",
"Tokelau":"tk.png",
"Tonga":"to.png",
"Trinidad and Tobago":"tt.png",
"Tunisia":"tn.png",
"Türkiye":"tr.png",
"Turkmenistan":"tm.png",
"Turks and Caicos Islands":"tc.png",
"Tuvalu":"tv.png",
"Uganda":"ug.png",
"Ukraine":"ua.png",
"United Arab Emirates":"ae.png",
"United Kingdom of Great Britain and Northern Ireland":"gb.png",
"United States of America":"us.png",
"United States Minor Outlying Islands[f]":"um.png",
"Uruguay":"uy.png",
"Uzbekistan":"uz.png",
"Vanuatu":"vu.png",
"Venezuela, Bolivarian Republic of":"ve.png",
"Viet Nam":"vn.png",
"Virgin Islands (British)":"vg.png",
"Virgin Islands (U.S.)":"vi.png",
"Wallis and Futuna":"wf.png",
"Western Sahara":"eh.png",
"Yemen":"ye.png",
"Zambia":"zm.png",
"Zimbabwe":"zw.png",
}

#Defining global variables
button_text_country1 = None
button_text_country2 = None
button_text_country3 = None
button_text_country4 = None
country_png_name = None
image_gui_widget = None
answer_comparison = None #compares selected button text with right answer
score_count = 0 #increases per correct answer
question_count = 0 #increases per answer
question_limit = 5 #when question_count reaches limit, game ends

#Updates country selection
def update_country_selection():
    while True:
        #Countries selected
        country_correct = random.choice(list(country_dict.items()))
        country1 = random.choice(list(country_dict.keys()))
        country2 = random.choice(list(country_dict.keys()))
        country3 = random.choice(list(country_dict.keys()))

        #Checks for any duplicates by comparing countries selected
        if (country1 == country_correct[0] or
            country2 == country_correct[0] or
            country3 == country_correct[0] or
            country1 == country2 or
            country1 == country3 or
            country2 == country3):
            print("duplicates detected: rerun")


        else:
            #takes correct answer (country name for answer comparison and png file)
            global answer_comparison
            global country_png_name
            answer_comparison = country_correct[0]
            country_png_name = country_correct[1]

            #Order of countries is then randomized for text display
            country4 = country_correct[0]
            list_country = [country1, country2, country3, country4]
            global button_text_country1
            global button_text_country2
            global button_text_country3
            global button_text_country4

            random_number = random.randint(0, 3)
            button_text_country1 = list_country[random_number]
            del list_country[random_number]

            random_number = random.randint(0, 2)
            button_text_country2 = list_country[random_number]
            del list_country[random_number]

            random_number = random.randint(0, 1)
            button_text_country3 = list_country[random_number]
            del list_country[random_number]

            random_number = random.randint(0, 0)
            button_text_country4 = list_country[random_number]
            del list_country[random_number]

            #Countries are unique and random
            global question_count
            console_question_count = question_count + 1 #for readability of console
            print("Question " +str(console_question_count) + ":")
            print("Countries are unique and random")
            break

#function to update photo
def update_photo():
    global image_country
    global image_gui_widget

    image_country = tk.PhotoImage(file="h240/" + country_png_name) #image country is defined to use this file
    print("This file name of country: ")
    print("h240/"+country_png_name+" ("+answer_comparison+")")
    print("")
    if image_gui_widget is None: #image widget made once to display first image
        print("image_gui_widget is null and needs to be made for first question but not for succeeding questions")
        print("")
        image_gui_widget = tk.Label(root, image=image_country)
    #Consecutive image are configured into the image widget
    #so garbage collection doesn't delete images if image_gui_widget is continously made
    image_gui_widget.configure(image=image_country)

def update_buttons(): #function to update buttons per question
    button1 =tk.Button(buttonframe, text=button_text_country1, font=("Arial", 18))
    button1.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10, pady=5)
    button1.config(command= lambda: click(button_text_country1))

    button2 =tk.Button(buttonframe, text=button_text_country2, font=("Arial", 18))
    button2.grid(row=1, column=0, sticky=tk.W+tk.E, padx=10,pady=5)
    button2.config(command= lambda: click(button_text_country2))

    button3 =tk.Button(buttonframe, text=button_text_country3, font=("Arial", 18))
    button3.grid(row=2, column=0, sticky=tk.W+tk.E, padx=10,pady=5)
    button3.config(command= lambda: click(button_text_country3))

    button4 =tk.Button(buttonframe, text=button_text_country4, font=("Arial", 18))
    button4.grid(row=3, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
    button4.config(command= lambda: click(button_text_country4))

    buttonframe.pack(fill='x')           #Buttons fill space, these are applied to all buttons


def click(country_guess_parameter): #function to see if answer to question is right or wrong
    # country_guess_parameter value comes from click(button_country#)
    global image_gui_widget
    global score_count
    global question_count
    question_count += 1

    if country_guess_parameter == answer_comparison:
        messagebox.showinfo("Result", "Correct! It was " + str(answer_comparison) + ".")
        update_country_selection()
        update_buttons()
        update_photo()
        score_count += 1
        score.config(text=score_count)
        label_counter.config(text="Question Counter: " + str(question_limit-question_count))


        if question_count == question_limit: #Ends program when no more questions are left
            root.withdraw()

            win = tk.Toplevel(height=300,width=500)
            win.wm_title("End of Game")

            l = tk.Label(win, text=username + "'s final score is:", font=18)
            l.pack()

            l2 = tk.Label(win, text=str(score_count) + " out of " +str(question_limit), font=18)
            l2.pack()

    else:
        messagebox.showinfo("Result", "Wrong! It was " + str(answer_comparison) + ".")
        update_country_selection()
        update_buttons()
        update_photo()
        label_counter.config(text="Question Counter: " + str(question_limit - question_count))


        if question_count == question_limit: #Ends program when no more questions are left
            root.withdraw()

            win = tk.Toplevel(height=300,width=500)
            win.wm_title("End of Game")

            l = tk.Label(win, text=username + "'s final score is:", font=18)
            l.pack()

            l2 = tk.Label(win, text=str(score_count) + " out of " +str(question_limit), font=18)
            l2.pack()


#User Interface
def initialize_gui(): #function to initialize GUI
    global root
    global entry
    global label
    global submit_button
    global style
    root = tk.Tk()                   #A new window for the interface is made
    root.title("Quiz Thing")         #interface is named
    root.geometry("500x700")         #interface is sized
    root.configure(background="lightgrey")

#Initializes first question
initialize_gui()
update_country_selection()
update_photo()

#adds image to gui
image_gui_widget.pack(padx=20, pady=50)

#Streches button to fit gui
buttonframe = tk.Frame(root, bg = "lightgrey")
buttonframe.columnconfigure(0,weight=1)
update_buttons() #also intitializes first question


#username prompt
global label
label = tk.simpledialog.askstring(title="Username", prompt="Enter Username")
username=label
while len(username) > 7 or len(username) == 0:
    label = tk.simpledialog.askstring(title="Username", prompt="Name has to be under 8 characters or have characters")
    username=label
print("Username inputted: " +(username))
print("")

#scoresheet
global score
label = tk.Label(root,text=username+"'s score:", font=("Arial",22), bg="lightgrey")
label.pack(padx=10,pady=20)
score = tk.Label(root, text=score_count, font=("Arial",20),bg="lightgrey")
score.pack(padx=10,pady=5)


#question counter
label_counter = tk.Label(root, text="Question Counter: " + str(question_limit-question_count), bg = "lightgrey")
label_counter.place(relx=0.7, rely=0.01)

root.mainloop()            #Application is ready to run

#click(), photos(), buttons(), countries() are the four repeating functions
#initialize gui() is the only function to not be repeating
