spawncamping-tyrion -- 0.0.1 -- January 9, 2014
===================

* Updated Django backend

Sales / Logistics / Analytics Engine

If we want to go whole hog, let's build this using Scott Machinery as a base test case.

Interfaces
==========

* Customer = Static webpage that allows them to check orders, inventory, etc.  It'll be their lens through which to view the application.

* Employees = web/chrome app that includes the customer view, but includes ways to modify the databases -- primarily adding, modifying, adding images/video, descriptions, etc for products.

* Mobile = similar to the customer interface, but it sleek and streamlined down to be viewed from a mobile device/tablet.  This will be a webapp that we can package as a native application using PhoneGap and/or Apache Cordova.

Design
======

To minimize server needs, I believe that the websites should be built with AngularJS with the backends written in Python.  

**There are also files that will be useful to work with using Chrome's Dev Editor if we want to package it using Polymer.  The tech is good and the aesthetics are nice.**

Funcational Specifications
==========================

* SIC / NAICS Info integration (lead generation)
-- incorportated into Google Maps
* Sales (I believe the old db file is included in this repo already)

Definitely more to come later -- I believe I have old functional specs, and I know many of the things that George has said in the past that he wanted.

*****

Anyway, we could start building this framework and just append the databases and sites as we grow.  I think we could have a functional alpha (funcational version, but with no information) in Q1 2015.