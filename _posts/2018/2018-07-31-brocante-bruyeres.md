---
layout: post
title:  "La Brocante Bruyeres: A Year Later"
date: 2018-07-31 12:00:00 +0200
image: /images/posts/brocante-bruyeres.jpg
categories: volunteering process application
---

![Flea Market](/images/posts/brocante-bruyeres.jpg)

It has been a year since the first [flea market][flea-market] I helped to organize in my former Belgian neighborhood. I contributed with an web application to streamline the enrolment of exhibitors, making the assignment of spots more efficient. Since then, the application became more mature for this year's edition, but this time I'm helping remotely, from Toronto, Canada.

<!-- more -->

I first reported my experience in [a post last year][simple-application-fallacy], when I worked with two sweet lades on the project. Then I resumed the work two months ago in preparation for this year's edition. The application is slowly evolving, improving the original process at every iteration. The following processes illustrates how it looks today.

The enrolment process starts during enrolment period. The enrolment form becomes available the first day of the period, allowing applicants to fill in the form and submit it. Given the number of spots requested by the exhibitor, the application checks if there is enough spots available. If yes, it saves the form with a "Non Confirmed" status and sends a submission notification. Otherwise, it sends a waiting list notification and sets the form with the "Waiting List" status. For enrolments with the "Non Confirmed" status, the organizer can "Confirm" them, triggering a notification to exhibitors indicating they will have a spot soon. Confirmed enrolments can be assigned to spots, which also triggers a notification to exhibitors with the rules and instructions to follow during the flea market.

![Enrollment Process](/images/posts/enrollment-process.png)

 The submitted form contains personal data, leading us to be compliant with the European [GDPR] (General Data Protection Regulation). So, we have to explain to the exhibitors what we are doing with their data. The message, put on the top of the form, says:

 > "For the sake of security, and to better organize its annual event, La Brocante des Bruyères needs to know some of your personal data. Your last name and first name are necessary to be able to identify you correctly during each communication. Your email address and phone are essential to the clarity and understanding of our exchanges. Your mailing address helps us to assign locations. These data will be sent to the police service that ensures the security of the event and will be deleted after 2 months the event occurred."

![GDPR Notice](/images/posts/form-gdpr-notice.png)

In the event of someone giving up a spot, it triggers the process of assigning the available spot to someone in the waiting list. The organizer takes the first person in the list and assigns a spot. The assignment triggers an notification to the exhibitor, completing the process.

![Waiting List Process](/images/posts/waiting-list-process.png)

The application has been proven useful, but there are many opportunities for improvements:

 - A enrolment can be cancelled but no notification is sent to the exhibitor.
 - The assignment to spots is still done one by one. A better user interface is desirable to streamline the assignment.
 - Confirming someone from the waiting list is not clear for new organizers. It requires familiarity with the application.

Improvements are done every year, but not everything is done at once because there is [only one contributor][contributors] at the moment: myself ;-) As people [get involved][github-brocante], we will certainly get all improvements out sooner. [Let me know][github-issues] if you have a flea market to automate.

Helping the organization of a flea market makes me happy because it promotes the culture of a sustainable world. Instead of throwing things away, people try to pass those on to other people who may have better use for them. Everything is available in a very affordable price and it is also an opportunity to gather the community. No doubt I will continue supporting it remotely for a long time.

[contributors]: https://github.com/htmfilho/brocante/graphs/contributors
[flea-market]: https://en.wikipedia.org/wiki/Flea_market
[GDPR]: https://eugdpr.org
[github-brocante]: https://github.com/htmfilho/brocante
[github-issues]: https://github.com/htmfilho/brocante/issues
[simple-application-fallacy]: /2017/08/simple-application-fallacy.html
