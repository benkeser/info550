---
layout: page
title: Lectures
permalink: /lectures/
---

Clicking the title of the lecture will open the slides in your browser. The icons navigate to relevant material for each lecture: 

<i class="fab fa-github"></i> = Github directory for lecture; <i class="fab fa-r-project"></i> = source Rmarkdown document for lecture; <i class="fas fa-book"></i> = additional readings; and <i class="fas fa-video"></i> = video recording. If video is not available, the icon will show as <i class="fas fa-video-slash"></i>. 

The lectures are produced using [xaringan slides](https://slides.yihui.org/xaringan/#1). Presentation notes are available by pressing "p". Slides can be printed to pdf by first scrolling through all slides (to ensure all content renders) and printing to pdf from your browser. [Allegedly](https://bookdown.org/yihui/rmarkdown/ioslides-presentation.html#printing-and-pdf-output) Google Chrome has the best support for this.

{% assign num = site.url | size | minus: 1 %}

<ul id="archive">
{% for lectures in site.data.lectures %}
      <li class="archiveposturl">
        <span><a href="{{ site.url | slice: 0, num }}{{ site.baseurl }}/lectures/{{ lectures.dirname }}/{{ lectures.filename }}.html" target="_blank">{{ lectures.title }}</a></span><br>
<span class = "postlower">
<strong>tl;dr:</strong> {{ lectures.tldr }}</span>
<strong style="font-size:100%; font-family: 'DM Sans', sans-serif; float:right; padding-right: .5em">
{% if lectures.breakoutsoln != "" %}
<a href="{{ site.url | slice: 0, num }}{{ site.baseurl }}/lectures/{{ lectures.dirname }}/breakoutsoln/{{ lectures.breakoutsoln }}"><i class="fas fa-lightbulb"></i></a>
{% endif %}
	<a href="https://github.com/{{ site.githubdir}}/tree/master/lectures/{{ lectures.dirname }}"><i class="fab fa-github"></i></a>&nbsp;&nbsp;
<a href="https://github.com/{{ site.githubdir}}/tree/master/lectures/{{ lectures.dirname }}/{{ lectures.filename}}.Rmd"><i class="fab fa-r-project"></i></a>&nbsp;&nbsp;
<a href="{{ site.url | slice: 0, num }}{{ site.baseurl }}/readings#{{ lectures.reading }}"><i class="fas fa-book"></i></a>&nbsp;&nbsp;
{% if lectures.recording == "" %}
<i class="fas fa-video-slash"></i>
{% else %}
<a href="{{ site.url | slice: 0, num }}{{ site.baseurl }}/recordings/{{ lectures.recording_url }}"><i class="fas fa-video"></i></a>
{% endif %}

</strong> 
      </li>
{% endfor %}
</ul>
