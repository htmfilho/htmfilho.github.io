---
layout: page
title: About
permalink: /about/
---

## The Author

My name is Hildeberto Mendonca, father of two amazing kids and husband of a wonderful woman. I'm a proactive, result-driven, disciplined professional with decades of experience on the IT industry. Across a variety of roles, I provide value through my skills in programming, software design, architecture, and training. I'm a highly flexible professional, in [permanent state of learning][projects], and driven towards exceeding expectations.

I have a Ph.D. in applied sciences on the field of electrical engineering. I took this degree as a challenge, which I achieved with great honour, but I decided to follow a different path from research to pursuit my passion for software engineering. The reason was simple: research has a long Time-To-Market cycle and I wanted to solve real world problems sooner, feeling myself useful as often as possible. But I have to recognize that my time as a scientist gave me three skills that I'm proud of:

1. **Resilience** - I don't quit, I have no fear, I do not hesitate. My Ph.D. was one of the hardest things I ever did. Everything else feels comfortable to deal with, which explains my permanent state of optimism.

2. **Reading and Writing** - I've read and wrote so much that I feel immense pleasure during my reading and writing sessions. By the way, I strongly disagree with a statement in the [agile manifesto][agilemanifesto] that says: "_Working software over comprehensive documentation_". All libraries and frameworks you use are heavily documented. Why wouldn't your applications be too?

3. **Problem Solving Oriented** - problems keep me motivated. Part of the solution for every problem is to influence our peers to feel the same.

### Permanent Goals

Inspired by the book [Deep Work](/books/2017/10/deep-work.html), here are my permanent goals:

#### Personal Goals

- Keep family in harmony by taking actions to improve union, resilience and health.
- Educate kids intellectually, physically, economically and with humanitarian values.
- Run an organized, simplified, and cost-efficient household.

#### Professional Goals

- Craft well-written and organized programs that serves their purpose for a long time.
- Make sure the organization has enough information about my work so they don't become dependent on me.
- Be well informed and educated to make the best technical decisions for every business context.
- Be kind, professional, honest, and positive with everybody in the office.

### Values

Inspired by military principles, here are my personal values:

- **Loyalty**: Support the leadership and stand up for the fellow colleagues by believing and devoting myself to the team.

- **Duty**: Fulfill my obligations and accomplish tasks as part of a team. Never take shortcuts that might undermine the integrity of the final product. Go a little further, endure a little longer, and look a tittle closer.

- **Respect**: Treat people with respect and dignity while expecting them to do the same. Self-respect by putting forth my best effort and preserving mental and physical health.

- **Selfless Service**: Put the welfare of the team and the company before my own without thoughts of recognition or gain.

- **Integrity**: Do what is right, legally and morally. Do and say nothing that deceives others.

- **Personal Courage**: Face fear and adversity, enduring mental and physical stress out of the comfort zone. Continue forward on the right path, especially if taking unpopular actions.

## The Blog

In this blog I write about personal experiences and software engineering. I've been maintaining this since 2007, with ups and downs overtime. I don't write as frequent as before, but I still invest time here.

<canvas id="myChart" width="400" height="200"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2020', '2021', '2022'],
        datasets: [{
            label: 'Posts over the years',
            data: [8, 34, 42, 29, 8, 9, 7, 2, 6, 4, 11, 15, 9, 14, 5],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(153, 102, 255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
</script>

Coincidentally, my most productive years were the ones of my Ph.D. Then it felt considerably down when I went back to the industry after finishing my studies.

My posts are long, but I do my best to keep your interest across the content. Sometimes, I write posts in the past to keep historical accuracy, but even though they are new they do not necessarily appear in the front page.

This is a static site managed by [Jekyll], versioned by [Git], and hosted by [GitHub]. I appreciate any feedback you may have. Please, create an issue in the website's [repository], describing what you think can be improved. Thank you for your visit!

[agilemanifesto]: https://agilemanifesto.org
[Jekyll]: https://jekyllrb.com
[Git]: https://git-scm.com
[GitHub]: https://github.com
[projects]: /projects
[repository]: https://github.com/htmfilho/htmfilho.github.io/issues
