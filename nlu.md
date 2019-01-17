nlu_md = """
## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:informCntTime
- [five fifteen](time)
- [5:15](time)
- [5 minutes ago](time)

## intent:informPartyPeople
- [three](number)
- we are [10](number) people
- [two](number) of us

## intent:informPartyVehicles
- [two](number)
- we drove in [2](number) cars

## intent:informInVsOut
- Just [returning](revenant) and will lose coverage.
- As I have a PhD from U of Guelph I do appreciate need for accurate data.
- [returning](revenant) 
- 11:30 am sunday august 5th
- 2 cars @3.40pm
- Already got home from the day hike yesterday 
Already returned.
At home
At that time I was leaving from my hike
body.InVsOut
Both
Camped to begin a hike early tomorrow
Cars not cats, of course!
Count taken when I returned from my hike 
Count taken when leaving for hike 
Count was just before we hiked. Time was 7:10am today
Count was taken when we were leaving for our hike 
Counted the vehicles around noon today. Returning from hike 
Day 2 of 3
Driving by
Driving up higher
Dropping off hikers.
Finished hiking.
From 
Have left
Heading up the hike
Home from hike
I am leaving for my hike. 
I am returning from my hike
I counted them when we left for our hike. When we returned at 6pm there were only 5 cars in the lot.
I did the hike on Tuesday 8/28/18 so done already. 
I gave the stats for both
I have returned. 
I was just returning from our hike to the ridge overlooking Snow Lake. We did not go down to the lake for lack of time.
I was leaving
I was leaving 
I was leaving and I counted, and counted again when I returned a few hours later
I was leaving at 11
I was leaving for my hike
I was leaving for. 
I was leaving. When I got there at 8 a.m. there was only 3 cars
I was returning from my hike 
I wasn't hiking, I was camping 
I'm home now.
I'm on my way.
I'm returning.
Ieaving
July 10th at 12 pm
Just got home. 
Just got started
Just returned home from day hike.
Just starting
Just starting.
Leaving

## intent:thankyou
- thanks!
- thank you
- thx
- thanks very much
"""
%store nlu_md > nlu.md
