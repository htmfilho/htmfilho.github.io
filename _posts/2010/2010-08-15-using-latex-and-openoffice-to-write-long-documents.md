---
layout: post
title: "Using Latex and OpenOffice to Write Long Documents"
date: 2010-08-15 18:53:00 +0200
categories: latex open source research
---

<a href="http://www.latex-project.org/">Latex</a> is a “_document preparation system for high-quality typesetting. It is most often used for medium-to-large technical or scientific documents but it can be used for almost any form of publishing_” (Latex project website). Latex compiles a script language into a formated document. This script language is not so easy to learn, but the effort may be worthwhile, since the resulting documents look more professional than their equivalent made using <a href="http://www.openoffice.org/">OpenOffice</a> or <a href="http://office.microsoft.com/">Microsoft Word</a>.

I wrote my PhD dissertation using Latex and the result was very satisfactory. The dissertation was gradually getting the shape of a book, which is pretty exciting for me, who admires authors but never intended to become one of them. To write Latex script, I use a tool called [Texmaker](http://www.xm1math.net/texmaker/), a Latex editor maintained by Pascal Brachet, a teacher of mathematics in a French secondary school. There are other interesting editors, but Texmaker’s simplicity is more attractive for me. The figure below depicts the source of my dissertation opened in Texmaker.

![thesis-texmaker-300x216.png](/images/posts/thesis-texmaker-300x216.png)

The problem of doing the whole work using exclusively Texmaker is its limitations in terms of language support and versioning. The spell check feature, for instance, is very limited (you cannot add new words to the dictionary), there is no grammar assistance and no versioning feature to highlight what was modified since the last revision. I consider these three features essential for those who are writing  important documents. No other tools can offer these features either.

To address some of these limitations, I decided to include OpenOffice in the process to fulfill the need for spell and grammar checking and versioning. The figure below depicts, step by step, the writing process.  It starts by writing the dissertation’s content in OpenOffice with the change control feature enabled. While writing, the editor automatically checks spelling and grammar. When finished, the added content is copied to Texmaker. Because Texmaker is a plain text editor, it doesn’t support rich formats coming from OpenOffice, such as tables, figures, bullets, enumerations, italic text and others. In these cases, the correspondent Latex formating script should be used after pasting OpenOffice’s contents. Once the format is done, we can finally compile and visualize the result.

![dissertation-writing-process-300x130.png](/images/posts/dissertation-writing-process-300x130.png)

After each transference of text from OpenOffice to Texmaker, we have to approve all changes in the OpenOffice document in order to identify all new and updated texts that should be transfered to Texmaker in the next iteration.

Two important details:

1. OpenOffice doesn’t support grammar checking by default. It is necessary to install the extension [Language Tool](http://extensions.services.openoffice.org/pt-br/project/languagetool) for that. Download the file “LanguageTool-[version].oxt” and import it to OpenOffice using the option “Tools – Extension Manager” in the menu. Click on “Add…” and select the file above. This extension starts working when you restart OpenOffice.

2. My intention is not to teach Latex here, but how to overcome some of its limitations by using OpenOffice as a complement.

You may ask: since you are writing everything in OpenOffice, why don’t you keep everything there and forget about Latex? Simply because it is very difficult to get the same results and quality that we get using Latex. You can fulfill the OpenOffice role using Microsoft Office. This one also doesn’t offer the same results as Latex, but the grammar checker is much better.
