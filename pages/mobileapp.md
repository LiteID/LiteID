---
title: Mobile App
menu: | 
 <a href="#background" style="margin-bottom:1px">Background</a><br>
 <a href="#compatibility" style="margin-bottom:1px">Compatibility</a><br>
 <a href="#implementation" style="margin-bottom:1px">Implementation</a><br>
 <a href="#interface" style="margin-bottom:1px">Interface</a><br>
 <a href="#demos" style="margin-bottom:1px">Demos</a><br>
 <a href="#what's-next-for-the-app" style="margin-bottom:1px">What's Next for the App</a><br>
---



# LiteID Mobile App

The mobile application is based on the cross platform Xamarin framework, allowing us to target a broad range
of devices, including iOS, Android, and Windows Mobile. We took care in developing our application to ensure
it is able to run on very early versions of Android (down to API 9/Gingerbread), which are prevalent in the
regions we are targeting.

Currently, we are only targeting smartphones with Android 2.3 (Gingerbread) or later. However, the core code
of the application is cross-platform compatible, and so it would be relatively easy to create versions for
iOS and the Universal Windows Platform.

### Background
---
While Android has the majority of the smartphone market share in most of the world, including Africa, we
wanted to create an app that had the potential to expand to iOS, as while it only represents 5% of the
smartphone market in Africa, it's not an insignificant platform in other parts of the world. I (James) had
previously heard about Xamarin, which is a cross-platform app development framework, written in C#. Since
I have more experience with C/C++ than with Java, and since we wanted to target multiple platforms, I
decided to use Xamarin to develop the LiteID mobile app. We chose not to target iOS at this time both due
to time constraints and due to the fact that we don't own Apple hardware.

#### Compatibility
We determined that while Android comprised [57.7%](http://stats.areppim.com/stats/stats_mobiosxtime_afr.htm)
of the African mobile OS market, gaining access to those users would not be as simple as haphazardly
developing an app using more recent features of Android. Android 4.3 and lower comprises [12.6%](https://deviceatlas.com/blog/android-versions-market-share-2016)
of the market in Africa, so I took care to develop the app not only to be technically compatible with
versions of Android as low as 2.3 (API 9/Gingerbread), but to have just as good of a user experience on
those devices as on the latest flagship phones. Because of this, LiteID is just as usable on a low-end
phone I got for 30 bucks (the BLU Dash Jr) as on my Galaxy Note 4.

### Implementation
---
The current implementation only supports Android, and due to time constraints and other factors is not
directly capable of interfacing with the blockchain. However, core business logic in the app is written
as cross-platform and has all the necessary interfaces to work with the blockchain, so expanding both
the platform support and the functionality would be fairly easy. You can [view the code on GitHub](https://github.com/LiteID/LiteID-Android).


#### Interface
While many apps developed today use design languages such as Material Design, or fancy gestures for
basic features, I chose to stick with a simple yet intuitive UI both to exepedite development and to
maintain compatibility and usability with older versions of Android. As such, there are currently five
interfaces: The main screen, which presents a list of documents, a button to go to the options scree,
and a button to add a new document; the options screen, which lets you set up your identity; the new
document screen, which lets you create a document from a file or just with plain text; the import
document screen, which lets you import and verify a document that has been shared (like via email), and
the view document screen, which shows details of each document, and allows the user to open it in an
external app for viewing, export it via email, delete it, and re-verify it if it was not created from
the current identity.

### Demos
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/G5a2RuFd_QM" frameborder="0" allowfullscreen></iframe>

<br>

### What's Next for the App
---
While the app has pretty much all the features I envisioned it having, aside from interacting directly
with the blockchain, the items on my development wishlist are: Dropbox/OneDrive/Google Drive sync (since
the actual documents are only stored locally), selecting some documents to be shared with every document
you share (such as name, ID card, since those are not inherently part of your identity), and the ability
to work through an RPC server (so an organization can sponsor the operation of the contracts).