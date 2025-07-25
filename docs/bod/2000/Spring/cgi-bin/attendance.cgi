#!/usr/bin/env perl
# OCF attendance roster script
# Originally from ~smcc/public_html/attendance.cgi
# Interpreter path updated by kpengboy, 2017-09-05

use CGI;

%status =
  ('X' => ['Present', '666666', 'ffffff'],
   'E' => ['Elected (elections meeting)', '0000cc', 'ffffff'],
   'e' => ['Elected (after meeting)', '0000cc', 'ffffff'],
   '1' => ['First consecutive absence', 'dddddd', '000000'],
   'D' => ['Dropped by missing this meeting', 'ffff66', '000000'],
   'd' => ['Resigned before this meeting', 'ffff66', '000000'],
   '-' => ['Present but not on BoD', '999999', '000000'],
   '.' => ['Missed but not subject to dropping (GM, SM)', 'dddddd', '000000'],
   ',' => ['Missed GM/vacation meeting (no dropping)', 'dddddd', '000000'],
   ' ' => ['Neither present nor on BoD', 'ffffff', '000000'],
   '/' => ['Missed, status unknown because of missing info', 'ff9900',
	   '000000'],
   '?' => ['Information missing', 'cc0000', 'ffffff']);

sub color {
    my($hex) = @_;

    #return qq'background="solid.cgi?color=$hex"';
    return qq'bgcolor="$hex"';
}

sub semester {
    my($title, $people, $meetings) = @_;

    print "<h2>$title</h2>\n";
    print "<table>\n<tr><td></td><th>",
    join("</th><th>", @$people), "</th></tr>\n";
    #@$meetings = reverse @$meetings;
    for $row (@$meetings) {
	($name, $data) = @$row;
	if (substr($name, 0, 1) eq "G") {
	    print "<tr><td>", substr($name, 1), "</td>";
	} else {
	    print "<tr><td>", $name, "</td>";
	}
	for $i (0 .. $#$people) {
	    $char = substr($data, 2 * $i, 1);
	    print qq'<td ', color($status{$char}[1]), ' align=center>',
	    qq'<font color="$status{$char}[2]"><b>$char</b></font></td>\n';
	}
	print "</tr>\n";
    }
    print "</table>\n";
}

$q = CGI->new;
print $q->header;

print "<html><head><title>OCF BoD attendance</title></head>\n";
print "<body>\n";


semester("Fall 1999",
	 [qw(ajani akopps calman ceugene eek jentsoi jones kaliya
	     katster kenao skang smcc suztang tee wenhwang yosenl)],

#                                   AjAkCaCEEeJTJnKlKtKOSkSMSzTeWWYl
	 [["GSeptember 8th, 1999", "E   E E   E E   E E E E E E E E "],
	  ["September 18th, 1999", "1   X X   X X   X X 1 X X 1 1 X "],
	  ["September 22nd, 1999", "X   X X   X X   X X D X X X D X "],
	  ["September 29th, 1999", "X e X 1 e X X   X X   X X 1   1 "],
	  ["October 6th, 1999",    "X X 1 X 1 X X   X X   X X X   X "],
	  ["October 13th, 1999",   "X 1 X X X 1 X   . X   X X 1   X "],
	  ["October 20th, 1999",   "X X X X X D X   X X - X X X   1 "],
	  ["October 27th, 1999",   "X X X 1 1 e X e X X   X X X   X "],
	  ["November 3rd, 1999",   "X X 1 X X 1 X X . X   X 1 1   1 "],
	  ["November 10th, 1999",  "X X X X X D . 1 . X   X X D   D "],
	  ["November 17th, 1999",  "1 X 1 X X   X D X X   X X       "],
	  ["December 1st, 1999",   "? ? ? ? ? ? X ? ? X   X ? ?   ? "],
	  ["January 19th, 2000",   "X X X X X   X   X X   X X       "],
	  ["January 24th, 2000",   "1 X X X X   .   X X   X 1       "],
	 ]);

semester("Spring 2000",
	 [qw(ajani akopps calman castello ceugene darin eddylu eek gmg 
	     ivan jeffe jjlin jones justine kaow kasian katster kenao
	     rbashar smcc suztang wyc)],
#                           AjAkCaCsCEDaEdEkGGIvJeJJJnJuKwKsKaKeRbSMSzWy
 [["GJanuary 31st, 2000",  "E E   E E           E       E   E     E     "],
  ["GFebruary 8th, 2000",  "X X   X X   E E     X   E   X E X E   X E   "],
  ["February 15th, 2000",  "X X   1 X   X X     1   X   X X X X   X 1   "],
  ["February 22nd, 2000",  "X X e X 1   1 X   e X   X   X 1 X X   X X   "],
  ["February 29th, 2000",  "X X 1 X X   X X   X X   X   X D 1 X   X X   "],
  ["March 7th, 2000",      "X X X 1 X e X X e X X   X   X   D X   X X   "],
  ["March 14th, 2000",     "X X X X X 1 1 X X X 1   1 e X     1   X X   "],
  ["March 21st, 2000",     "X X X X X D X X X X X   X 1 X     D   X X   "],
  ["April 4th, 2000",      "X X X 1 X   X X 1 X 1   X D X     e   X X   "],
  ["April 18th, 2000",     "X X 1 X X   1 1 X 1 X   X   X     X   . X   "],
  ["April 25th, 2000",     "X X X 1 X   X D X X X   1   X     X   X X   "],
  ["August 22nd, 2000",    "X X , X X   , - X , X e ,   ,     X   X ,   "],
  ["August 30th, 2000",    "X X X 1 X   1 - X X 1 X X   X     1 e X X e "],
  ["September 5th, 2000",  "X X X D X   X - 1 X D X X   X     D 1 X X X "],
 ]);

semester("Fall 2000",
	 [qw(ajani akopps bac calman ceugene cpefyh drew eddylu eek gmg ivan
	     jeffe jjlin jshen jtsai kaow kenao michaelj pboynton smcc
	     stephhou suztang wyc)],
#                             AjAkBaCaCECPDrEdEkGGIvJeJjJsJTKwKeMJPBSMSHSzWy
  [["GSeptember 14th, 2000", "E E E   E E E E E E   E     E E     E E   E E "],
   ["September 21st, 2000",  "X X X e X . 1 1 X X   X   e X X     X X   1 X "],
   ["GSeptember 28th, 2000", ", X , , X X , , , X   X   X , X     , X e , , "],
   ["October 5th, 2000",     "X X X X X X X D X X   1   X X 1     X X X D X "],
   ["October 12th, 2000",    "1 X X 1 X X X   X X   X   X X D e   1 X 1 e 1 "],
   ["October 19th, 2000",    "D X X X X X X   X X   X   1 X   X e D X X X X "],
   ["October 26th, 2000",    "e X X X X X X   X X e X e X 1   X 1 e X X X 1 "],
   ["November 2nd, 2000",    "1 X 1 1 X X X   1 X X 1 1 X X   X D 1 X 1 X X "],
   ["November 9th, 2000",    "X X X X X X X   D X X D X X X   1   X X X X 1 "],
   ["November 16th, 2000",   "X X X X X . X   e X 1 e X 1 X   X   X X 1 X X "],
   ["GNovember 30th, 2000",  "X X X , X X X   X X X X , X X   ,   d X X X , "],
   ["December 7th, 2000",    "X X X X X X X   X X 1 1 d 1 X   1     X X X X "],
   ["January 18th, 2001",    "1 X X X X X X   X X D X - D X   X   - X 1 X X "],
   ["January 24th, 2001",    "X X X X X X X   X X - X -   X   1     X X 1 1 "],
 ]);

semester("Spring 2001",
	 [qw(ajani akopps bac calman ceugene cpfeyh drew dsrogers fho gmg ivan
	     jeffe jones kenao mchen mgoodman mwong nkang sasfaw smcc stephhou
	     suztang tiv wyc)],
#                           AjAkBaCaCECPDrDSFHGGIvJeJnKeMCMGNMwKSaSMSHSzTRWy
  [["GJanuary 31st, 2001", "E E E E E E E E   E E E E   E E       E E E   E "],
   ["February 8th, 2001",  "1 X X X X 1 X 1   X X X 1   1 d e   e X X X   X "],
   ["February 14th, 2001", "D X X 1 X X X d   X X 1 X   D   1   1 X 1 1   1 "],
   ["February 21st, 2001", "- X X X X 1 X     X X X 1       D   X X D X   X "],
   ["February 28th, 2001", "e X X X X X X     X X X X e         1 X   1   X "],
   ["March 7th, 2001",     "X X X X X X X     X X X 1 X         D X   X   X "],
   ["March 14th, 2001",    "X X X X X 1 X     X X X D 1         e X e X   X "],
   ["March 21st, 2001",    "X X X 1 X X X     X X X             1 X 1 X   1 "],
   ["April 4th, 2001",     "X X X D X X X     X X X   -         D X D X   D "],
   ["April 11th, 2001",    "X X X X X e 1   e . X X             X X   X   X "],
   ["April 18th, 2001",    "X X X X X X X   X X 1 X           e 1 X   X e 1 "],
   ["April 25th, 2001",    "X X X 1 X X 1   X X X X -         1 D X   X X X "],
   ["GMay 2nd, 2001",      "? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? "],
   ["September 6th, 2001", "X 1 X X 1 X X - X X 1 X             X X   X X 1 "],
  ]);


semester("Fall 2001",
	 [qw(ajani akopps bac calman carissay cpfeyh drew eek fho gmg jeffe
	     karthik kevin? remlluf sasfaw skam smcc stephhou suztang
	     tiv wyc)],
#                             AjAkBCCaCYCPDrEkFHGGJeKaKvDFSaSKSMSHSzTRWy
  [["GSeptember 13th, 2001", "E E E E   E E E E E     E E E   E E E E E "],
   ["September 20th, 2001",  "X X X X   X X 1 ? X e   ? 1 ?   X X ? X X "],
   ["October 4th, 2001",     ". ? ? X   1 ? D ? X X - ? D ?   X X X X X "],
   ["October 18th, 2001",    "X X 1 X e X X   / . X e /   / e X X X X X "],
   ["November 1st, 2001",    "X X X X 1 X X   X . 1 X D e D 1 X X 1 X X "],
  ]);

semester("Spring 2002",
	 [qw(ajani akopps bac calman cpfeyh dsrogers dwc eek fho jeffe
	     jhs rchopra smacian smcc stephhou suztang tiv wyc)],
#                             AjAkBCCaCPDRDCEkFHJeJSRCSISMSHSzTRWy
  [["GFebruary 7th, 2002",   "- E E E E E E E E E     - E - E E E "],
   ["February 14th, 2002",   "- 1 X X 1 ? 1 1 X 1     - X - ? 1 X "],
   ["February 21st, 2002",   "  D 1 X D / X X X D     - X   / X X "],
   ["March 14th, 2002",      "  e X X   D X 1 X - e   - X e X X X "],
   ["March 21st, 2002",      "  1 X X e   X   X   X   - , X X X X "],
   ["April 4th, 2002",       "  X 1 X X   1   X - 1 E   X X 1 X X "],
   ["April 11th, 2002",      "  X X X X - X   X   X 1   X 1 X X X "],
   ["April 18th, 2002",      "  1 1 X 1   X   X   1 D - X X X X X "],
   ["April 25th, 2002",      "  X X X X   X   X - X     X X X X X "],
  ]);

print "<p><table border=1>\n";
for $k (keys %status) {
    print qq'<tr><td ', color($status{$k}[1]), ' align=center>',
          qq'<font color="$status{$k}[2]"><b>$k</b></font></td>\n';
    print "<td>$status{$k}[0]</td></tr>\n";
}
print "</table>\n";
print "</body></html>\n";
