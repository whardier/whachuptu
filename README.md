Whachuptu - Active Work/Project Logger
======================================

Whachuptu (Whatcha up to?) polls users at specified intervals to collect work related project information since the
last poll.  It can be rather annoying and aggressive, but incredibly valueable for both employeer, employee as well as
an amazing tool for contractors to use to keep on top of project history.

The user has a few decisions to make every polling period that help keep everybody informed.  New projects are simple to enter.  Incedental work between polling periods is simple to enter as well.

This program does not (currently) attempt to help with project management or syncronize with any project management software.  Adapters would be wonderfully welcomed.  Projects and tasks that are entered in can persist multiple polling periods and have notes attached to each period.

Polling periods are applied to groups and users.  A user can be part of several accounts and maintain their own polling periods and work logs as well.

Features
========

  - Available as a paid public site (Coming soon!)
  - Available as self installed and deployed solution
  - Simple REST API for client development
  - MongoDB backed infrastructure
  - Very simple server backend
  - Scalable backend infrastructure

Requirements
============

  - Python 2.7/3.2 or PyPy
  - Tornado 2.4 (Looking in to using Motor)
  - MongoDB 2.2 (TTL collection support)
  - At (Yes.. really!)
  - InetD (Also.. really!)

Client Applications
===================

  - Web Access (In development)
  - Google Integration
  - XMPP Integration
  - Mail Integration
  - SMS Integration (Through 3rd party services)

  - No plans yet for Android, iOS, etc.. etc.. etc.. 