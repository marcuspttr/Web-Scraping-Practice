# web-scraping-challenge
Next stop. Mars! (Website to scrape all the details and repost them on our own Flask api.)

This was a very hard assignment. I got a lot of work done at the beginning, but then grinded to a halt as I had to work on another project.

## Some issues:
- An early issue was when I had my browser path to a new website to get information but my soup wasn't finding any matches. Had some frustration double and triple checking different modifications on soup.find functions to no avail.  Realized that as I pathed to a website I had to update my parsing information.
- Had some issues using jinja to show my information. I'll admit I still haven't quite figured out how to have it produce my scraped table of Mars facts (had to hardcode the html code to get it to work.)
- Finally hunting down the appropriate links to access the full hemisphere photos without having to physically download them was a bit tricky. I'm not sure if I made this too complex but creating loops and successfully pathing to additional nested websites and links felt like a big success once it worked.

## Reflection and sample pictures:
I'd say I'm pretty happy with how it came out.  I need to work on my understanding of bootstrap to create a more controlled & polished lay out and work with jinja in general.

Here is a sample picture of the index before the scrape-ing populates it:
![Index Set-Up](https://github.com/marcuspttr/web-scraping-challenge/blob/main/Missions_to_Mars/assets/index_setup.PNG)

And an example of it after running the scrape:
![Top of the Page](https://github.com/marcuspttr/web-scraping-challenge/blob/main/Missions_to_Mars/assets/top_example.PNG)
![Middle of the Page](https://github.com/marcuspttr/web-scraping-challenge/blob/main/Missions_to_Mars/assets/middle_example.PNG)
![Bottom of the Page](https://github.com/marcuspttr/web-scraping-challenge/blob/main/Missions_to_Mars/assets/bottom_example.PNG)
