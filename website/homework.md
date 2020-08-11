---
layout: page
title: Homework
permalink: /homework/
---

Clicking the title of the homework will open the assignment pdf in a new tab.

<i class="fab fa-github"></i> = Github directory for lecture; <i class="fab fa-r-project"></i> = source Rmarkdown document for homework; <i class="fas fa-share-square"></i> = link to Canvas submission.

{% assign num = site.url | size | minus: 1 %}

<ul id="archive">
{% for homework in site.data.homework %}
      <li class="archiveposturl">
        <span><a href="{{ site.url | slice: 0, num}}{{ site.baseurl }}/homework/{{ homework.dirname }}/{{ homework.filename }}.pdf" target="_blank">{{ homework.title }}</a></span><br>
<span class = "postlower">
<strong>due date:</strong> {{ homework.due }}</span>
<strong style="font-size:100%; font-family: 'DM Sans', sans-serif; float:right; padding-right: .5em">
	<a href="https://github.com/{{ site.githubdir}}/tree/master/homework/{{ homework.dirname }}"><i class="fab fa-github"></i></a>&nbsp;&nbsp;
	<a href="https://github.com/{{ site.githubdir}}/tree/master/homework/{{ homework.dirname }}/{{ homework.filename}}.Rmd"><i class="fab fa-r-project"></i></a>&nbsp;&nbsp;
	<a href="{{ homework.submit }}"><i class="fas fa-share-square"></i></a>
</strong>
      </li>
{% endfor %}
</ul>
