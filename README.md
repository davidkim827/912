# 912 by Katherine Holotko and David Kim

The current 911 system sucks. 

This repo is a PoC on how we plan to fix the system.

This system is designed to be implemented by the district 911 operating centers across the nation only in mass evac scenarios. It assumes that certain data can easily be obtained by the implementing operating centers such as cellphone tower data, evac points, danger/congestion points, etc.

The first part of our solution regards implementing an automated voice messaging where the dialer receives the following script:

"We’ll get you to an operator ASAP, however our lines are busy.
We noticed you’re located in zone _________.
We recommend that you head on over to the evac point associated with your zone: __________
If you are in need of immediate help, please hang on to the line and we will be with you shortly."

A text message will be sent with the same information above to the dialer for information redundancy (this is in conjunction with the second portion of our solution). This has been implemented rudimentally in our repo.

The second part of our solution (recommendation) regards implementing a text messaging system that is used by the 911 protocol (or a different one 912).

A person will be able to send text messages to 911/912 and receive text messages.

Analytics will be done with all messages and phone calls recorded (this is the privatization effort of our project).

In the future, utilizing datastore technologies like mongoDB and analytical tools that exist such as SpeechRecognition and NLP libraries, we can preprocess texts, videos, pictures, and postprocess voice data to be able to create smarter routes and deploy Real Time Data to emergency professionals as well as dialers who are in need of evac route assistance.
