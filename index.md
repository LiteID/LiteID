---
title: Home
menu: | 
 <a href="#inspiration" style="margin-bottom:1px">Inspiration</a><br>
 <a href="#research-we-did" style="margin-bottom:1px">Research we did</a><br>
 <a href="#what-it-does" style="margin-bottom:1px">What It Does</a><br>
 <a href="#mobile-app" style="margin-bottom:1px">Mobile App</a><br>
 <a href="#sim-app" style="margin-bottom:1px">SIM App</a><br>
 <a href="#text-interface" style="margin-bottom:1px">Text Interface</a><br>
 <a href="#who-did-what" style="margin-bottom:1px">Who Did What</a><br>
 <a href="#how-we-built-it" style="margin-bottom:1px">How We Built It</a><br>
 <a href="#challenges-we-ran-into" style="margin-bottom:1px">Challenges We Ran Into</a><br>
 <a href="#things-that-we're-proud-of" style="margin-bottom:1px">Things That We're Proud Of</a><br>
 <a href="#what-we-learned" style="margin-bottom:1px">What We Learned</a><br>
 <a href="#what's-next-for-liteid" style="margin-bottom:1px">What's Next for LiteID</a><br>
---



# LiteID

LiteID is an identity system based on Ethereum Contracts. It allows people who don’t 
have access to normal forms of ID to identify themselves, in order to access resources 
that would be otherwise unavaliable to them.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uBBDMqZKagY" frameborder="0" allowfullscreen></iframe>

<br>

### Inspiration
---
Currently, there are over three billion people in the world who lack an official form of identification.
This is such an important problem holding back the devloping world that the World Bank has created a progam
specifically to address this: [Identification for Development](http://www.worldbank.org/en/programs/id4d)
We wanted to make a difference, and so we chose to develop an easily accessible identification system.

#### Research we did
The first thing we did was look to at what others had done in the past. We found many projects that tried to
solve this problem by leveraging the blockchain, most of which were webapps. However, we wanted somthing that
would be accessible to as many people as possible.

We found that while only around [15.5%](http://www.itu.int/en/ITU-D/Statistics/Documents/facts/ICTFactsFigures2016.pdf)
of African households have access to the Internet, more than [80%](http://www.pewglobal.org/files/2015/04/Pew-Research-Center-Africa-Cell-Phone-Report-FINAL-April-15-2015.pdf)
have a cellphone or smartphone. We wanted to find a way to reach out to thease people, and connect them to a
secure, scalable, and flexable identity system.

### What It Does
---
LiteID is an identity ecosystem based around a core Ethereum contract, which contains only a few simple
functions. It stores only salted hashes, their associated salts, and a timestamp, allowing the utmost
flexibility for the documents being stored. This allows us to have selective disclosure, where a user only
reveals the documents that they choose. Additionally, the salted hashes dramatically slow down attackers,
such as tyrannical regimes, from brute-force searching the block chain for names or other information.

#### Mobile App
The mobile application is based on the cross platform Xamarin framework, allowing us to target a broad range
of devices, including iOS, Android, and Windows Mobile. We took care in developing our application to ensure
it is able to run on very early versions of Android (down to API 9/Gingerbread), which are prevalent in the
regions we are targeting.

#### SIM App
The SIM application is based on Oracle's JavaCard, and is intended to include most of the functionality
of the Mobile App. However, because of the limitations of SIM cards and MMS, we are not be able to process 
document files larger than 300KB.

#### Text Interface

The text interface is designed to be easy to use and accessible to anyone with a texting-capable phone, in
order to enable as many people as possible to interface with LiteID and therefore be able to create a
secure identity for themselves. While it is not as fully featured as the app, it has the greatest reach of
the current interfaces. It is also designed to be easy for governments or other sponsoring organizations to
run their own nodes with a texting interface. Using this system, an entire country could be able to use
LiteID at a fraction of the cost of a traditional eID system.

### Who Did What

<hr style="height:2px;">

Mark Omo: I worked on the SIM App and the Text Interface
<br><br>
James Rowley: I worked on the Mobile App
<br><br>
Daniel Werth: I helped shoot and compose the video

### How We Built It
---
The SMS server is built using Python 2.7 and the Twillo API.

The Ethereum integration is accomplished through a Python module we devloped called [LiteID Contract Tools](https://github.com/LiteID/LiteID-Contract-Tools),
based on a custom version of [ethjsonrpc](https://github.com/LiteID/ethjsonrpc) that we modified to allow
for better cross platform support.

The Mobile App itself is built on a cross platform mobile devloment framework called [Xamarin](https://www.xamarin.com/),
which allows us to target the vast majority of mobile devices in use in the world today. 


### Challenges We Ran Into
---
We originally set out to write a lightweight client implementation of Ethereum in Xamarin, however
unfortunately due to a lack of documentation on the behind-the-scenes protocols used, and a creeping
deadline, we were not able to reimplement it from the source of geth like we had planned.

### Things That We're Proud Of
---
Mark Omo: The implementation of the text server and ethereum interface, as it was my first published pypi package.
<br><br>
James Rowley: I'm very proud of how the app turned out, since it is my first.
<br><br>
Daniel Werth: The project video.

### What We Learned
---
Mark Omo: Much more about the inner workings of the JavaCard implementation, as well as the intricacies of how Ethereum nodes communicate with one another.

James Rowley: I learned quite a bit about app development, as this was my first experience with mobile apps, as well as more about the blockchain.

Daniel Werth: How subtle differences in video production can make huge differences in the outcome.

### What's Next for LiteID
---
We want to continue to expand the implementation of the Mobile, SIM, and Text applications in order to get
LiteID in the hands of those who need it most, and so that we can get feedback about what we're doing
right or wrong. We would also like to work with African mobile carriers to get the SIM app rolled out to
their clients, which would greatly accelerate adoption.
