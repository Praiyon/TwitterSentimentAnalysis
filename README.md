This is a rest-api that takes an input and performs a sentiment analysis on tweets regarding the input.

Whats a sentiment analysis?
A sentiment analysis is essentially a computational analysis of a persons emotions behind whatever they wrote.

Two values are of interest here: Polarity and Subjectivity.
Polarity is a number between -1 and 1 indicating the persons emotions (negative or positive)

Subjectivity uses the sames scale... but indicates subjectivity

Example json payload

{
"obama": {
"0": {
"tweet": "RT @Iilackingdom: Remember when Halsey was a little secret you had and when people asked you who you listened to you would be like “it’s Ha…",
"polarity": 0.6,
"subjectivity": -0.29375
},
"1": {
"tweet": "RT @AdamParkhomenko: Barack Obama is perfect  https://t.co/3OcLCuorc8",
"polarity": 1,
"subjectivity": 1
},
"2": {
"tweet": "RT @TomFitton: .@JudicialWatch sued for Dossier info. 7 months ago--STILL getting stonewalled by FBI/DOJ. Now we know why--protecting Clint…",
"polarity": 0,
"subjectivity": 0
},
"3": {
"tweet": "RT @hotfunkytown: The way I see it....if Chris Matthews was going to sexually harass anyone, I would have thought it would have been Barack…",
"polarity": 0.8333333333333334,
"subjectivity": 0.5
},
"4": {
"tweet": "RT @owillis: weird thing about net neutrality is that there's not a strong reason for the right to oppose it other than obama was for it. i…",
"polarity": 0.5288095238095238,
"subjectivity": -0.1111904761904762
},
"5": {
"tweet": "This what Obamacare did... he told you he’d transform America https://t.co/032p59W8Xt",
"polarity": 0,
"subjectivity": 0
},
"6": {
"tweet": "MORE OF BARRY OBAMA WORKING WITH HIS FAVORITE KIND OF PEOPLE, TERRORISTS!!! Obama administration undermined anti-He… https://t.co/vEYlijPj7U",
"polarity": 0.7999999999999999,
"subjectivity": 0.6666666666666666
},
"7": {
"tweet": "RT @JohnJHarwood: for the record, Dow Jones average more than doubled under Obama and rose more, in percentage terms during his first 11 mo…",
"polarity": 0.5366666666666666,
"subjectivity": 0.33999999999999997
},
"8": {
"tweet": "RT @TomFitton: Mueller illegally/dishonestly obtains @RealDonaldTrump docs? Not surprising. @JudicialWatch uncovered how Mueller FBI illega…",
"polarity": 0.5,
"subjectivity": -0.35
},
"9": {
"tweet": "RT @bfraser747: My question to @jeffsessions is how can you sit bye recussibg yourself from the Trump #RussianCollusion Mueller investigati…",
"polarity": 0,
"subjectivity": 0
},
"10": {
"tweet": "RT @SebGorka: I give you the Obama Administration. https://t.co/W3xEhQJaTs",
"polarity": 0,
"subjectivity": 0
},
"11": {
"tweet": "RT @GenRickDeMarco: WOW! Obama let Hezbollah off the hook to broker the failed #IranDeal Which allowed drugs(cocaine) in our country to fun…",
"polarity": 0.65,
"subjectivity": -0.1875
},
"12": {
"tweet": "@highsteaksgames “Thanks, Obama.” https://t.co/TyQlbUsVod",
"polarity": 0.2,
"subjectivity": 0.2
},
"13": {
"tweet": "RT @Jali_Cat: @TIME What red line is that @EricHolder?? The one Obama drew that countries, leaders and every living breathing human crossed…",
"polarity": 0.05,
"subjectivity": 0
},
"14": {
"tweet": "RT @edgecrusher23: HANNITY *A Must See* Final Verdict: Obama Uses Intelligence Services to Create ((FAKE)) Russian Emails sent to DNC \"Pret…",
"polarity": 0.6666666666666666,
"subjectivity": -0.16666666666666666
}
}
}
