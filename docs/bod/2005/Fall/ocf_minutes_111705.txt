From: novakyu@OCF.Berkeley.EDU                                                  
To: bod@OCF.Berkeley.EDU                                                        
Subject: Minutes of BoD (11/17/2005)                                            
Date: Fri, 18 Nov 2005 04:24:22 -0800                                           
                                                                                
For those who were at the meeting, I apologize for my miscalculation:           
we did have quorum. Please feel free to email corrections/questions to          
bod@ocf.berkeley.edu, and please someone in group www post this minute          
on the website. The minutes follow:                                             
                                                                                
----                                                                            

Minutes of the OCF Board of Directors Meeting 11/17/2005                        

Board Members (13):                                                             
   brando                                                                       
   dima                                                                         
   elliot                                                                       
   ekashida(+)(*)                                                               
   frank                                                                        
   geo                                                                          
   griffin                                                                      
   jkit                                                                         
   joshk(*)                                                                     
   novakyu                                                                      
   sle                                                                          
   tdhock(+)                                                                    
   yury(*)                                                                      
                                                                                
(Note: (*) denotes the member who will be removed from BoD if not               
present at this meeting. (+) ekashida == eugene in previous BoD minutes,        
tdhock == toby in previous BoD minutes. The names used in these minutes         
are their OCF login and should be used in preference to their first name.)      
                                                                                
Board Members present (9): Quorum met                                           
   brando                                                                       
   dima                                                                         
   elliot                                                                       
   ekashida                                                                     
   frank                                                                        
   jkit                                                                         
   novakyu                                                                      
   sle                                                                          
   yury                                                                         
                                                                                
Meeting Opens at 7:20 p.m. in Dwinelle 230:                                     
                                                                                
Approved Discussion Topics:                                                     
   * Printer (10 min allocated, with one suggesting 7 min, instead)             
   * Quota (5 min)                                                              
   * "Sun Party" (5 min)                                                        
   * Other (end-of-semester) Food/Party (5 min)                                 
   * Winter Break: Project Madness (30 sec)
   * MCC                                                                        
   * Logging yury off                                                           
   * Pizza                                                                      
                                                                                
Announcements:                                                                  
   GM Message: None (or this note-taker missed it when it was announced)        
   SM Message: No SM message. elliot however laments, "We are basically         
      done and no one's showing up for BoD or project meetings any more.        
      We are getting close to finals."                                          
                                                                                
Project Team Reports:                                                           
   LDAP/Kerberos (report by yury):                                              
      Current State: It works on Linux and Solaris 10. We still need            
         tools (approve, sorry, etc.) and need to work on Windows.              
      Work Done: sluo worked on getting Kerberos working on Solaris 10.         
         yury wrote a working version of krb_migrate pam module, which          
         is necessary for transparent (from users' point of view)               
         migration (of password hash, essentially) from NIS+ to Kerberos.       
      Additional notes: yury: "We are ready to roll things out, but we          
         need to test it." We might need to set it up on one or two             
         login server (possibly sandstorm, which has been taken out of          
         commission to be Solaris 8 test client) and do a small-scale           
         migration and test for some time before moving completely over.        
                                                                                
   Security (report by frank):                                                  
      Current State: frank says hmogri emailed him saying that: He's            
         working on a large document which analyzes OCF's security              
         situation and discusses what can be done to improve it.                
                                                                                
   Web: elliot mentions it briefly, but jkit reminds everyone that              
      it's been canceled.                                                       
                                                                                
   Eshleman (report by jkit):                                                   
      Current State: Same as last week---stuck because the key to the           
         locks cannot be found. jkit will cut the locks very soon and           
         replace it with the red-color-coded locks in the server room           
         that we do have the keys for.                                          
      Additional notes: In case the reason Dell computers aren't booting        
         is due to power supply problem, jkit asks, "How long until we          
         can get the power supply?" brando answers, "Two to three days."        
         Also, yury asks, "Is there any chance of getting permanent             
         internet connection" as opposed to Airbears? jkit answers,             
         "No".                                                                  
                                                                                
   This concludes team reports                                                  
                                                                                
Discussion Items:                                                               
(I might not have gotten down everything important that was said. Please        
feel free to email outrageous emendations^W^Wcorrections to BoD.)               
   Printer:                                                                     
      elliot: The printer looks good, other than not having tabloid size        
         printing, and W&MF uses it, some other people from staff,              
         though elliot won't speak for them, have looked at it and found
         nothing wrong. He likes it.                                            
      brando: What's the dimension of the printer?                              
      frank: About the same as our current one, but not as tall.                
      elliot: The cost of the printer comes out around $2200.                   
      frank: It might be higher than $2200, after we get the other              
         "optional" items, such as RAM, etc.                                    
      brando,yury: Why do we need RAM? --jkit mentions something about          
         larger print jobs being possible.                                      
      elliot: We already passed the alloted time to discuss this so we          
         should move on.                                                        
      But the discussion continues a while...                                   
      yury: One problem is that it doesn't hold as much paper, without          
         the extension tray.                                                    
      frank: But it has higher multivolume <something> duty cycle, so           
         it's better.                                                           
      jkit, and others: Is it possible to use the current Tray 4?               
      In conclusion, as to how much it would cost (as jkit and others           
      asked), frank answers: $3646 (sorry, I missed the details of what         
      went in but there was RAM upgrade, extra trays, and no hard drives        
      as well as no HP care packs).                                             
                                                                                
      Seeing the cost, it was decided to table this issue until we have         
      quorum as the BoD was under the impression that the quorum was not        
      met.                                                                      
      novakyu makes a side comment about the printer not breaking down          
      as much lately (i.e. no fuser error), but dima is skeptical.              
                                                                                
   Quota: in summary, elliot sent out email to admin@ocf, and there was         
      support for more conservative quota than starting value of 500MB          
      (labeled Plan A), at a starting value of 400MB (labeled Plan B).          
      Plan C was also proposed as compromise at 450MB. elliot briefly           
      mentioned the mail quota, but it was agreed that it was a separate        
      issue and that we should focus on disk array for home and                 
      services. Some parts of discussion follows:                               
      jkit: He says to go with more conservative option, Plan B.                
      dima: Why?                                                                
      brando: We are screwed if people start using their quota more.            
      dima: They are not going to use quota.                                    
      novakyu said something that I forgot.                                     
      novakyu moves to eliminate Plan C as a wimpy compromise.                  
      dima: 500MB is helping users, we should help our users.                   
      jkit, novakyu: People don't need more disk space as it is, and            
         those who do already have more disk space. Besides, higher disk        
         quota will only encourage people not to conserve space and keep        
         more of their useless old files around. And if we run out of           
         space because we increased the quota too much, it's not helping        
         users.                                                                 
      Some mentions were made as to OCF's ability to even support 1GB           
      quota for 5 years, and novakyu raises objection by repeating              
      jjlin's argument against tdhock's analysis from memory: i) the            
      analysis is valid only if we assume that 1000 new users we get            
      this year will use only about 40MB of their quota, and assuming           
      that existing users do not use any more space---clearly some
      factor was neglected in the analysis.                                     
      yury: Let's move the Windows profiles to old disk array, and              
         higher quota will put OCF in better light in comparison to             
         other services.                                                        
      jkit and novakyu speaks against having found a marvelous reason           
      which the scantiness of BoD members' inbox quota cannot contain.          
      Informal poll is taken by elliot with the result, yury, sle, and          
      dima for Plan A, jkit and novakyu for Plan B, no one for Plan C           
      and the rest abstain.                                                     
      In conclusion: elliot will decide one way or the other some time          
      soon by the power vested in him as the SM.                                
                                                                                
   Sun Party:                                                                   
      No news on the Sun Party, and no definite dates set. Mentions             
      were made that it would be difficult near the finals.                     
                                                                                
   Other Food/Party:                                                            
      Should we go out (to restaurants) or stay in (potluck, party at           
      lab, etc.)? jkit mentions that someone should set us up a calendar        
      and find out when everyone (or as many as possible) can make it.          
                                                                                
   Winter Break: Project Madness                                                
      Some of the stuffs we can/should do over the winter break, as             
      proposed by elliot:                                                       
        1) automate account approval/creation                                   
        2) automate answering of stock questions                                
        3) automate... stuffs ('sorry, I missed other details. :( )             
                                                                                
   at this point, geo, who is here with us in spirit, asserts on #ocf,          
   19:57 <+geo> erm                                                             
   19:57 <+geo> there's never anything good in the minutes                      
   19:57 <+geo> unless you promise to transcribe EVERYTHING said                
   19:57 <+geo> including all the stuff that doesn't go in the minutes =]       
                                                                                
   Logging yury off:                                                            
      yury goes to log himself off OCF on elliot's laptop so that he            
      cannot access yury's secret stash of pr0n.                                
                                                                                
   Pizza:                                                                       
      Yes, we will have pizza next BoD, and no, novakyu, we are not             
      having pizza this BoD. :(                                                 
                                                                                
Elect new BoD:                                                                  
   We thought that we didn't have quorum so we skipped it, but in any           
   case everyone was on BoD (and if anyone wasn't, well, we didn't have         
   quorum, then. =] ).                                                          
                                                                                
Meeting closes at 8:15 p.m., as judged by the time frank logged off #ocf        
when he hibernated his laptop without quitting his IRC client.                  
                                                                                
End of the Official BoD meeting on 11/17/2005 which was formerly thought        
unofficial.                                                                     
