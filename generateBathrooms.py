from mapRate.models import Rating, Bathroom, Pin
import random

bathrooms = [["Aldrich Hall", 33.64854669998156, -117.84122589999998, True],
["Anteater Recreation Center", 33.64359764777621, -117.82791864452422, True],
["Art, Culture, and Technology", 33.65099393675353, -117.8449827846549, True],
["Art Studio", 33.650243641775035, -117.84494303069015, True],
["Arts Annex", 33.647315512499304, -117.8468036153451, True],
["Science Library", 33.646145957369725, -117.8463845751314, True],
["Berk Hall", 33.6464010731517, -117.84945452909629, True],
["Cross Cultural Center	", 33.64796140694652, -117.84183937327744, True],
["Croul Hall", 33.64386465195876, -117.84468073095017, True],
["Enginnering Tower", 33.6449489030145, -117.84109704629527, True],
["Gateway Study Center", 33.64756405097313, -117.84165041560507, True],
["Gavin Herbert Eye Institute", 33.641875719575665, -117.85219551560516, True],
["Hewitt Hall", 33.64349284800469, -117.8518024021139, True],
["Humanities Hall", 33.647454982511945, -117.84400124444137, True],
["ICS II", 33.644151665089346, -117.84160521506875, True],
["Krieger Hall", 33.647942608266554, -117.84354618862262, True],
["Medical Education Bldg.", 33.644796250218846, -117.85218980211381, True],
["Medical Sciences C", 33.64579592694056, -117.8505027597864, True],
["Medical Surge II", 33.64714200286829, -117.85042987698527, True],
["Music & Media Building", 33.64950783420398, -117.84447327667768, True],
["Rockwell Engr. Center", 33.64405762471028, -117.84059998862271, True],
["Rowland Hall", 33.64476107186335, -117.84422225978636, True],
["Schneiderman Lecture Hall", 33.645798537622944, -117.8447573039678, True],
["Social & Behavioral Sciences Gateway", 33.64758536453718, -117.83906630211386, True],
["Social Science Plaza B", 33.6472138340985, -117.83912613095008, True],
["Steinhaus Hall", 33.64641757311412, -117.84489568862256, True],
["Student Center", 33.64909423653421, -117.84223294730018, True]]
names = []
for b in bathrooms:
    names.append(b[0])

rCounter = 0
bCounter = 0
for b in bathrooms:
    bathroomT = []
    iter = 'MFI'
    if b[3] == False:
        iter = 'MF'
    for c in 'MFI':
        r1 = Rating(name=str(rCounter))
        r1.save()
        r2 = Rating(name=str(rCounter+1))
        r2.save()
        r3 = Rating(name=str(rCounter+2))
        r3.save()
        r4 = Rating(name=str(rCounter+3))
        r4.save()
        
        b1 = Bathroom(name=str(bCounter), gender=c, freePeriodProducts=False, paidPeriodProducts=False, cleanliness=r1, hygiene=r2, safety = r3, accessiblity = r4, avg = 0)
        b1.save()
        bathroomT.append(b1)
        rCounter += 4
        bCounter += 1
    if iter == 'MFI':
        p = Pin(name=b[0], bathroom_male=bathroomT[0], bathroom_female=bathroomT[1], bathroom_inclusive=bathroomT[2], latitude = b[1], longitude=b[2])
        p.save()
    else: 
        p = Pin(name=b[0], bathroom_male=bathroomT[0], bathroom_female=bathroomT[1], latitude = b[1], longitude=b[2])
        p.save()

def pseduoRate(name):
    p = Pin.objects.get(name=name)
    for b in [p.bathroom_male, p.bathroom_female, p.bathroom_inclusive]:
        b.cleanliness.total += random.randint(1, 5)
        b.cleanliness.count += 1
        b.hygiene.total += random.randint(1, 5)
        b.hygiene.count += 1
        b.accessiblity.total += random.randint(1, 5)
        b.accessiblity.count += 1
        b.safety.total += random.randint(1, 5)
        b.safety.count += 1
        b.freeperiodProducts=bool(random.randint(0, 1))
        b.paidperiodProducts=bool(random.randint(0, 1))
        b.update()
        b.save()

for n in names:
    for i in range(0, random.randint(10, 20)):
        pseduoRate(n)

