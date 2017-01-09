---
title: SIM Apps
menu: | 
---

# SIM Card Applications

SIM applications run on the SIM cards in your phone. In fact, what we normally call SIM cards 
are actually a [Smart Card](https://en.wikipedia.org/wiki/Smart_card) running an application to
interact with the cell network. 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/SIM_Card.jpg/320px-SIM_Card.jpg" height="100px">

We created our SIM app with Oracle's [Java Card](https://en.wikipedia.org/wiki/Java_Card), one
of the smallest java implementations, allowing it to run on Smart Cards (such as SIM cards). Due
to the highly secure nature of SIM cards, we want to extend our SIM app to enable secure storing
of Ethereum private keys and other information in the secure enclave of the SIM card.