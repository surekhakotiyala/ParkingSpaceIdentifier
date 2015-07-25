import PIL
from PIL import Image
import sys
import pickle

#slots in the parking spaces
spaces = [
[(301,197),(325,207),(265,253),(289,262)],
[(332,211),(357,221),(321,278),(297,268)],
[(365,223),(390,234),(330,280),(355,290)],
[(399,238),(427,248),(388,305),(364,297)],
[(430,249),(455,262),(423,319),(400,313)],
[(465,266),(490,276),(455,335),(430,323)],
[(505,202),(529,213),(496,270),(469,258)],
[(471,190),(496,200),(462,255),(436,245)],
[(438,175),(462,186),(428,241),(403,231)],
[(405,162),(430,171),(369,218),(395,229)],
[(372,148),(398,157),(362,215),(336,203)],
[(340,133),(364,143),(329,201),(306,191)],
[(138,373),(171,387),(129,454),(95,439)],
[(105,359),(138,373),(95,439),(62,426)],
[(71,346),(105,359),(62,426),(28,412)],
[(618,245),(651,259),(613,323),(580,309)],
[(651,259),(686,273),(647,338),(613,323)],
[(686,273),(721,288),(682,353),(647,338)],
[(721,288),(756,301),(717,367),(682,353)],
[(756,301),(791,316),(752,382),(717,367)],
[(791,316),(827,330),(788,396),(752,382)],
[(827,330),(863,345),(824,411),(788,396)],
[(863,345),(899,360),(860,427),(824,411)],
[(899,360),(936,375),(897,442),(860,427)],
[(936,375),(973,390),(935,458),(897,442)],
[(935,458),(972,473),(934,542),(896,526)],
[(897,442),(935,458),(896,526),(859,510)],
[(860,427),(897,442),(859,510),(822,494)],
[(824,411),(860,427),(822,494),(785,479)],
[(788,396),(824,411),(785,478),(748,463)],
[(752,382),(788,396),(750,463),(713,448)],
[(717,367),(752,382),(713,448),(678,433)],
[(682,353),(717,367),(678,433),(643,418)],
[(647,338),(682,353),(643,418),(608,403)],
[(613,323),(647,338),(608,403),(575,389)],
[(580,309),(613,323),(575,389),(540,373)],
[(148,293),(180,308),(138,373),(105,359)],
[(180,308),(213,321),(171,387),(138,373)],
[(213,321),(247,335),(204,401),(171,387)],
[(247,335),(280,350),(238,416),(204,401)],
[(280,350),(313,363),(271,431),(238,416)],
[(313,363),(347,378),(305,444),(271,431)],
[(347,378),(380,393),(340,459),(305,444)],
[(380,393),(414,408),(373,474),(340,459)],
[(340,459),(373,474),(331,543),(298,528)],
[(305,444),(340,459),(298,528),(263,512)],
[(271,431),(305,444),(263,512),(229,498)],
[(238,416),(271,431),(229,498),(196,482)],
[(204,401),(238,416),(196,482),(162,469)],
[(171,387),(204,401),(162,469),(129,454)],
[(135,125),(167,138),(126,200),(93,187)],
[(102,112),(135,125),(93,187),(61,173)],
[(81,266),(114,280),(71,346),(38,331)],
[(114,280),(148,293),(105,359),(71,346)],
[(370,143),(402,156),(363,219),(330,204)],
[(402,156),(435,170),(395,232),(363,219)],
[(435,170),(469,183),(429,246),(395,232)],
[(469,183),(502,197),(462,261),(429,246)],
[(502,197),(535,211),(496,275),(467,261)],
[(462,261),(496,275),(456,338),(422,324)],
[(429,246),(462,261),(422,324),(390,311)],
[(395,232),(429,246),(390,311),(356,296)],
[(363,219),(395,232),(356,296),(322,282)],
[(330,204),(363,219),(322,282),(290,268)],
[(298,192),(330,204),(290,268),(257,255)],
[(265,179),(298,192),(257,255),(224,241)],
[(232,164),(265,179),(224,241),(191,227)],
[(199,151),(232,164),(191,227),(158,213)],
[(167,138),(199,151),(158,213),(126,200)],
[(175,63),(207,76),(167,138),(135,125)],
[(143,51),(175,63),(135,125),(102,112)],
[(110,37),(143,51),(102,112),(70,97)],
[(207,76),(240,90),(199,151),(167,138)],
[(240,90),(272,102),(232,164),(199,151)],
[(272,102),(304,115),(265,179),(232,164)],
[(304,115),(338,130),(298,192),(265,179)],
[(338,130),(370,143),(330,204),(298,192)],
[(836,171),(870,184),(832,248),(797,234)],
[(800,156),(836,171),(797,234),(762,220)],
[(765,143),(800,156),(762,220),(727,206)],
[(730,130),(765,143),(727,206),(693,192)],
[(697,116),(730,130),(693,192),(659,178)],
[(909,121),(945,134),(906,198),(870,184)],
[(945,134),(981,147),(943,212),(906,198)],
[(943,212),(979,226),(940,290),(904,276)],
[(906,198),(943,212),(904,276),(868,261)],
[(870,184),(906,198),(868,261),(832,248)],
[(735,57),(770,71),(730,130),(697,116)],
[(770,71),(805,83),(765,143),(730,130)],
[(805,83),(839,96),(800,156),(765,143)],
[(839,96),(874,111),(836,171),(800,156)],
[(874,111),(909,121),(870,184),(836,171)],
[(544,132),(575,144),(614,84),(582,72)],
[(515,44),(550,58),(585,1),(543,2)],
[(582,72),(550,58),(585,1),(619,11)],
[(582,72),(615,85),(653,24),(619,11)],
[(483,31),(515,44),(478,104),(444,90)],
[(515,44),(550,58),(512,118),(478,104)],
[(512,118),(544,132),(582,72),(550,58)],
[(381,3),(418,7),(383,64),(346,50)],
[(418,6),(451,19),(413,77),(380,64)],
[(451,19),(483,31),(444,90),(413,77)],
[(498,444),(532,458),(491,526),(457,511)],
[(532,458),(566,473),(527,542),(491,526)],
[(566,473),(601,489),(561,557),(527,542)],
[(80,29),(106,39),(69,94),(43,83)],
[(113,43),(140,52),(102,109),(76,97)],
[(104,117),(129,127),(92,183),(66,173)],
[(145,57),(171,66),(133,119),(108,111)],
[(72,101),(98,113),(59,168),(35,158)],
[(210,80),(236,90),(199,146),(173,137)],
[(136,129),(163,140),(125,197),(100,185)],
[(178,69),(203,78),(166,133),(142,124)],
[(202,156),(228,167),(190,221),(166,212)],
[(242,94),(269,103),(232,160),(204,149)],
[(170,143),(194,153),(158,209),(132,199)],
[(234,168),(260,181),(224,237),(198,227)],
[(276,107),(300,119),(262,174),(239,164)],
[(268,182),(290,192),(256,250),(229,240)],
[(307,119),(332,133),(295,185),(270,177)],
[(301,197),(325,207),(265,253),(289,262)],
[(332,211),(357,221),(321,278),(297,268)],
[(365,223),(390,234),(330,280),(355,290)],
[(399,238),(427,248),(388,305),(364,297)],
[(430,249),(455,262),(423,319),(400,313)],
[(465,266),(490,276),(455,335),(430,323)],
[(505,202),(529,213),(496,270),(469,258)],
[(471,190),(496,200),(462,255),(436,245)],
[(438,175),(462,186),(428,241),(403,231)],
[(405,162),(430,171),(369,218),(395,229)],
[(372,148),(398,157),(362,215),(336,203)],
[(340,133),(364,143),(329,201),(306,191)]
]

#For openning a image file
#test case one
#im = Image.open('parking_spaces.jpg')
#test case two
im = Image.open('parking_space(1).jpg')
#the image is converted to RGB
rgb_im = im.convert('RGB')

#initially there are zero empty slots
empty_slot = 0
    
#iterating for each slot in the parking space
for row in spaces:
    (x1,y1),(x2,y2),(x4,y4),(x3,y3) = row
    #print(x1,y1,x2,y2,x3,y3,x4,y4)
    xx = x1
    xz = x2
    r1 = r2 = r3 = 0
    sum_r=0
    sum_g=0
    sum_b=0
    offset = 0
    total_pixels = (y3-y1) * (x2-x1)
    
    for y in range(y1,y3):
	#print(x1,y1,x2,y2,x3,y3,x4,y4)
        listx = range(x1-offset,x2-offset)
        for x in listx:
            #print(x,y)
            temp = 0
            z0 = float(x2-x1)
            z1 = float(y2-y1)
            temp = float(z1/z0)
            #print temp
            #for calculating for every next point in y-axis
            # from bottom to top of the slot
            y = y + temp
            r, g, b = rgb_im.getpixel((x, y))
            sum_r = sum_r + r
            sum_b = sum_b + b
            sum_g = sum_g + g
	#print(r,g,b)
        #print sum_r
	#print total_pixels
        #print(sum_r/total_pixels,sum_g/total_pixels,sum_b/total_pixels)

        #for calculating for every next point in y-axis
        # from bottom to top of the slot           	
	offset += 1
        if y % 2 == 0:
            offset += 1
    print(sum_r/total_pixels,sum_g/total_pixels,sum_b/total_pixels)
  
    #some threshold ranges to calculate 
    # total number of empty slots in the parking space
    r = sum_r/total_pixels
    r0 = sum_g/total_pixels
    r1 = sum_b/total_pixels
    colrange = r - 10
    colrange0 = r + 5
    
    #above 104 it detects for white color cars
    if (r <= 105):
       # for checking with threshold ranges
       if (colrange <= r0 <=colrange0 or colrange <= r1 <= colrange0):
          #increamenting of each empty slot in the parking area
          empty_slot +=1
    print empty_slot

