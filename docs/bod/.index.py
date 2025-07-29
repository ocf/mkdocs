#!/usr/bin/env python

import datetime
import os

def get_years():
    first_year = 1989
    current_year = datetime.datetime.today().year
    years = range(current_year + 1, first_year - 2, -1)
    return zip(years[1:], years)

def year_has_semester(year, semester):
    return os.path.isdir("%s/%s" % (year, semester))

#if __name__ == "__main__":
if True:
    print "Content-type: text/html\n"
    print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <title>Open Computing Facility: Meeting Minutes Archive</title>
        <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
        <style type="text/css">
            @import url("/bleuice.css");
        </style>
        <link rel="stylesheet" type="text/css" href="/bleuice.css" title="bleuice" />
        <link rel="alternate stylesheet" type="text/css" href="/bleuarctic.css" title="bleuarctic" />
        <script type="text/javascript" src="/styleswitcher.js"></script>
        <link rel="shortcut icon" href="/favicon.png" type="image/png" />
     </head>
    <body>
        <!--#include virtual="/header.html"-->
        <div id="mothercontainer">
            <div id="container">

            <!--#include virtual="/skinpicker.html"-->

            <h2><a href="/">Open Computing Facility</a> Meeting Minutes Archive</h2>

            <div class="tabulated">

            <table>
                <thead>
                    <tr>
                        <th>Year</th>
                        <th>Fall</th>
                        <th>Spring</th>
                    </tr>
                </thead>
"""
    for (fall_year, spring_year) in get_years():
        print """\n<tr><td class="year">%s - %s</td>""" % (fall_year, spring_year)
        for (year, semester) in [(fall_year, "Fall"), (spring_year, "Spring")]:
            if year_has_semester(year, semester):
                print """<td><a href="%s/%s">%s %s Minutes</a></td>""" % (year,
                                                                        semester,
                                                                        year,
                                                                        semester)
            else:
                print """<td></td>"""

    print """
</tbody>
</table>
</div>
</div></div> <!-- end div container and mothercontainer -->
<!--#include virtual="/footer.html"-->
<!--#include virtual="/tracker.html"-->
</body>
</html>
"""
