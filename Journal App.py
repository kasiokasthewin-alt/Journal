File=open("Journal.txt","w")

File.write("""

October 28, 1994
The weather has become the only thing worth recording. It dictates the entire shape of the day.
This morning broke with a thick, yellow valley fog that swallowed the lime kilns entirely. You couldn't see five feet beyond the kitchen window. It felt heavy, like wet wool pressing against the glass. By noon, a sharp northern wind blew it all away, leaving the sky a brutal, clear blue that makes your eyes ache. The temperature dropped five degrees in an hour.

November 2, 1994
A day of relentless, gray drizzle—what the locals call "lazy rain" because it doesn’t bother going through your clothes, it just goes straight to the bone.
The wind is howling through the gaps in the kitchen door frame, making a sound like a low whistle. The ink takes twice as long to dry on the page today because the air in the cottage is so damp. I spent the afternoon watching the water pool in the ruts of the gravel track outside, turning the gravel into miniature, muddy rivers.
""")

File.close()

File=open("Journal.txt","r")

print(File.read())