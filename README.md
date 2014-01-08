[![Build Status](https://travis-ci.org/holzenburg/feedshare.png?branch=master)](https://travis-ci.org/holzenburg/feedshare)


feedshare
=========

__[feedshare.net](http://feedshare.net)__ is a service to share and discover OPML feed lists.

Features
--------

- Upload or link to OPML files
- Automatic updating linked sources
- Publishing with user defined slug  
	(feedshare.net/user-defined-slug)
- Basic list search (author, title, tags)
- Tagged feeds and lists


Quick start
-----------

1. Clone repository  
> git clone http://github.com/holzenburg/feedshare  

2. Install dependencies (you might want a [virtualenv](http://www.virtualenv.org))
> pip install -r requirements.txt  

3. Initialize database  
> python manage.py syncdb  
> python manage.py migrate  

4. Run Django  
> manage.py runserver  


Contribute
----------
These features would be quite nice to have. If somebody wants to work on them, please get in touch:

- __Search__: Implement a scalable search engine
- __Discovery__: Enhanced discovery features


Dependencies
------------
For a list of python libraries, feedshare builds upon, see [requirements.txt](https://github.com/holzenburg/feedshare/blob/master/requirements.txt).

These Javascript libraries are included in this codebase for convenience:

- [bootstrap-tagsinput](https://github.com/timschlechter/bootstrap-tagsinput)
- [typeahead.js](http://twitter.github.io/typeahead.js/)


Origin
======
[Brent Simmons](http://inessential.com), Author of NetNewsWire, MarsEdit, Glassboard and Vesper [posted his OPML file](http://inessential.com/2014/01/04/my_feeds), lamenting the lack of an OPML sharing service. That drove me to spend a weekend on Feedshare. Seemingly [there](https://twitter.com/search?q=feedshare.net) [is](http://blog.louisgray.com/2014/01/feedshareforrssopml.html) [some](http://inessential.com/2014/01/06/feedshare_net) [interest](http://rumproarious.com/2014/01/06/feedshare-an-opml-sharing-service/) in such a service. [Alex Kessinger](http://alexkessinger.net) encouraged me to open source the code. I think that's a great idea and hope that others might want to help improving it and adding features.

Arne Holzenburg / [@holzenburg](https://twitter.com/holzenburg)  
January 2014


License
=======
This project is licensed under [MIT](https://github.com/holzenburg/feedshare/blob/master/LICENSE).


