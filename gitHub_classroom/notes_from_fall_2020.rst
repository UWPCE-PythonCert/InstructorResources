Notes / Suggestions from using gitHub classroom for the Fall 2020 intro class
#############################################################################

Incomplete import
=================

This has been a BIG problem:

Sometimes it fails altogether, which is annoying but not horrible, as the student knows it and can gereanlly repeat the process
(though sometime they have to try multipel times)

Sometimes it appears to work, and they get a functon repo but not all teh commits (and therefor not all teh files).
This is a mess, as teh student doesn't know what they should have gotten, so they don't know anytihng's wriong.
I had this a bunch with the ``.gitignore`` file not getting added, and then they end up adding a bunch of cruft
they shoudln't have :-(

It seems to be more reliable if you do a "Template" import, but still not totally reliable.

No "feedback" branch created
============================

classromm has this nifty feature where it creates a "feedback" branch automatically, and then a PR,
so there's one there right off the bat for the studetnes to use for feedback.
Seems like a great idea, but maybe 1/3 to 1/2 the time, it didn't get created, and it is not trivial to creat it by hand.
(You can't do a PR without a change).

So I turned this feature off, and have the students create a branch (and PR) for their work.

Too many repos!
===============

THe idea behind classroom is that you have a repo for each assignement.
THis is nice as it keeps things clean and separted. But they you have a lot of busiwork for each assignement.
Fine for a larager one, but a fair bit of overhead for studetns and instructors for small ones -- we can have
threee small assignemnts in a single week. THat means I have to look at three different PRs in three different
repos to grade them -- even one extra minute of point-and-clicking is 40 extra minutes a week for my class -- that's a lot!

If / when i do this again, I'll probably merge the smaller assignemtns into one per Lesson.

### mailroom with exceptions and mailroom wit unit tests

If they are in teh same lesseon, thwy -- should be one assignment!

