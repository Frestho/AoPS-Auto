# AoPS-Auto
This repo contains scripts that can help you automate the tedious task of saving every lesson transcript and homework page when your AoPS class ends. However, be warned that it is quite hard to set up.

Instructions:
This requires you to have the Keyboard library installed. It can be found here:
https://github.com/boppreh/keyboard

1. Open up the appropriate script (lesson transcripts or homework)
2. Look at line 4. You may need to change the number after "week < ..." depending on your class length. You should change it to your class length in weeks + 1. If you are saving transcripts, there is an extra step here. When you save the first transcript yourself, note the url. You should see a number like 25245 at the end. Subtract 1 from that number (assuming you are saving week 1's transcript) and replace it with the number at the end of line 7. This step is not necessary if you are saving homework pages.
3. Go to your first week's transcript or homework page. You need to save the first page manually so your computer knows where to save future pages.
4. Start the script. Make sure your browser window is focused.

Wonder how it works?

It's just a simple script that performs a series of keyboard clicks.

First, it uses Ctrl+L to focus the address bar (this shortcuts works on all modern browsers)
Then it enters the url of the page it wants to save (notice how the program avoids using mouse clicks, which makes it flexible across all screen resolutions and window sizes).
It uses Ctrl+P to save the page, waits for everything to load, then enters the file name and saves it.
Repeat.

Normally, doing this yourself would be very tedious (especially for a 24 week class). I find it very satisfying to see everything being done without me having to do anything.
