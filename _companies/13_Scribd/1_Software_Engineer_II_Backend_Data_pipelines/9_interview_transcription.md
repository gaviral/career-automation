# Interview Transcription - Scribd
## Software Engineer II (Backend + Data pipelines)
## Date: October 15, 2025
## Interviewer: Sachin (Senior Engineering Manager)

---

So the interview is just about to start.
Hey, Hey, Sachin. How are you doing? Good. Good. How are you?
Very good.
Okay. Aviral. Right? Yes. You're saying it right.
Thanks for taking the time to talk to me. You based up in Vancouver? I am.
Awesome. Okay. I used to live in Vancouver, by the and now I live in Toronto.
Oh, okay. Where about in Vancouver?
I was in Downtown.
Oh. Dan Danville and what was it? A break?
The Greater Vancouver or, like, Granville Island? Down down down
Oh, downtown like, Granville Island or something? No. Like, downtown. Like,
Oh, okay. Granville And Frank. 0, I see. You would name naming the
street. Okay. Got it. I thought you were saying Granville Island. I would just got a little bit confused there.
No. Yeah. Yeah. Yeah. It's it's a long time back, but yeah.
Okay. Let's get started. So so we have half an hour. What I would like to
do is to start a with a round of introduction, then would like to
get to know your work experience a little bit more, so we'll dive to you over a similar level.
And then
understand what you like to work on. And then last few minutes, we'll leave for any questions here.
Sounds great. Okay. Awesome. So I can kick us off
So my name is Sachin. I live in Toronto, being at Scripps for about
three years now. I'm a leader in my data engineering team.
Team primarily works on metadata extraction, so you could think about it as
extracting metadata from PDFs, basically.
Or unstructured documents that use to upload on ScriptDocs. Most of them are PDFs. We take this
PDF and then we try to run multiple tools on top of it. So
these are Python libraries. I see you've written some library which is
pretty cool to see. But, yeah, we we sometimes run Python libraries. Sometimes it's our
open source machine learning models. Sometimes these are, like,
custom machine learning models that are applied to search team develop.
And then LLMs are being something we've been focusing on off rate. So
use one of our tools at disposal and then
experiment it and make it available to downstream systems. So we expose it
via various interfaces to our downstream team. So
high level, that's what the team does. We are a team of 10 engineers.
We kind of spread it around. Like we've got a few folks in Toronto.
We have got two folks in Vancouver. Vancouver, we have a hub
it's a small hub. I think we have got
probably like 15 ish people there.
But I've got two people from the team there. And then we've
few folks in The US as well, so kind of spread around that sense.
Yeah. That's sort of. Sorry.
To dive into as we have questions and all, but maybe you could start with the introvert.
Absolutely. There was just, a quick, like, understand, like, in between you were saying, like, extracting the
metadata. Is that what you were saying? Like like, the getting the PDFs
extracting metadata, and then, like, letting it open for downstream
like, other teams to consume? Oh, okay. As I said, what we do. Yes.
Perfect. Perfect. Yeah. Just wanted to get a good idea of, like, making sure that I understood that correctly.
But, yeah, I can certainly go into a little bit of my background.
I'm I'm. I am a software development engineer.
I've worked quite a bit in
full stack AIML, like software engineering overall and majority in back
end. And some of the projects that I've been, like, quite proud of is
dealt with a lot of data pipelining. And, yeah, I I would say
like, at Amazon itself, I have like, I worked on one of
like, this project called, like, VTO, which is virtual try on.
To give you a tiny bit of context, I'd say it's something that
like, if you were to open the Amazon app right now with like, in
like, in the Amazon app, if you go to a specific lipstick, like, as as
specifically lipsticks, and you click on the virtual try on button, you can see some of my work
there where you would see that, you can try on different,
lipsticks virtually in the augmented environment, like, where they would
like, you can see the in the camera itself, your face, and whatnot.
And the data pipelining work that I did in that particular case would be
I'd say, extracting colors
Sorry. Extracting colors,
and other visual properties and so that we could create the three d assets
of, like, the three d models of lips so that they could be rendered.
So, yeah, that's one of the, like, big projects that I worked on. Like, I'd led
that project with two two engine a
junior software engineers, like one machine learning engineer,
and some data scientists and applied scientists. And
this is just one of the, like, big projects that I've worked on at Amazon and
think
like, I also worked at Prime Pantry where I worked at, like, big
scale and, learned about the Amazon way of doing things.
And going a slightly bit back, it would be like, I got my soft
engineering degree from University of British Columbia where I
learned about the foundation. So kind of going backward from
like, a very brief bird eye view,
of, a little bit about my technical experience and the places that I've worked.
Cool. Awesome. Yeah. That's great to hear. You do I think one of
the engineers who is actually based on RemindCode is from UBC as well. So
Nice. Probably probably a different batch. But yeah. We have
so many people for working at Amazon, like,
UBC and then, like, moving to different companies as well.
So yeah. So maybe, you know, if you could maybe talk
about one specific product where you actually had to work on
something like large scale data processing. It doesn't even have to be data
It's something like back end heavy
where you what was the point about it? What was your particular contribution?
Definitely. So in Amazon beauty tech team,
we had, like, this project where I'll I led the design
and build of the beauty tech
data lake and even the virtual try on. Like so, basically,
we process, like, more than 40 terabytes of data coming in daily
from the Amazon's, like, product catalog.
And we served, like, their we served, like,
more than, I would say, like, 40,000,000 customers monthly.
And they were spread across, like, 15 different countries.
So we had the worldwide expansion pro like, project happening in there too.
So this, I would say, is like a culmination of, two projects
But, like, I can go more into details of that.
But, like, it became essentially the data lake that we ended up creating. It became the
data source for multiple downstream teams, like the recommendation team,
the customer experience team, then product managers, even
for them to be able to do, like, natural language queries,
on our, like, beauty tech dataset. I
go a little bit more details about the core components of this.
So it's Yeah. Yeah. Yeah. We can. I agree. Yeah. Absolutely.
So, like, the the three d asset model creation, that was one of the downstreams.
As I mentioned, like, you know, like, where you could get the visual properties about different products.
So this data lake that we created, one of the
I I I like, I treated this as the whole, like,
creation of the data lake where we'd had the virtual try on discovery.
Where we discovered all of our we got 40 terabytes of
sorry. I'm I'm having, a
a cough. Yeah. Yeah.
Sorry. I'm just, like, having a bad throat day one of those days.
Where I've talked a lot.
Alright. So what I was saying was we
there there was beauty product discovery.
Where we created the pipeline that would get notifications
through as an everything was on AWS. So we would get notifications
on SNS and SQS services. And then
like, our new data is ready. Today, these are the changes that happened
and we would have, like, 40 terabytes of, like, these parquet format.
Like, files that would we would get in s three buckets.
And then our what what I created was essentially
these distributed serverless pipelines. We used AWS step functions for orchestration, which had spark like patterns
And then Lambda, we used for, like, a lot of that for data process
and auto scaling. And there are interesting decisions
that were made here that we can certainly get into later. But,
essentially, we use step functions, lambdas,
then DynamoDB for metadata storage, like, with which because it provided good
high throughput. And, we had Athena, as a good wrapper
for, like, s q doing SQL queries on s three.
Because we had, like, really massive, like,
queryable large dataset in parquet format.
And a big focus in all of this was, like, infrastructure as code
not only in this project, but, like, all the projects that I have used before.
AWS CDK, which is very equivalent to, like, Terraform.
We use that at, like like, in this project
And, like, all of this like, this project that I'm describing, it was
like, all led by me where we took it all the way from requirements engineering and
requirements, take like, once we have finalized those going
into the design phase, then implementation. And then even after that, we then
it for any other team. We created the infrastructure
and the implementation and every testing and operational readiness around it.
And maintained it for, like,
like, many months after that. Right?
And we yeah. Like, we own it all the way to the end.
And it was, like, a four stage CICD pipeline.
We had, like, very many things, like,
CloudWatch, X rays for distributed tracing
of our whole data pipeline. And, yeah, I'll
I can go a little bit into the data flow as well. We had the
transforming it and enriching it so that we could
serve it to the visual property extraction tool.
That extracted the visual properties. There were other things like metadata
We had, like, ML models integrated into it.
There there are so many more things that I can go into. I'm just curious if there's something
specific you'd like to dive deeper into. Yeah. Maybe maybe
since you mentioned ML model, can you maybe talk about that part? Like, you know, what was the ML model? Where did they
deploy it? And what was
who who dubbed the models? Absolutely.
So the situation essentially was we had
right now, we were getting a vast variety of data
when you want to render a lipstick, like, you want to create that three d model.
We were getting things like unicorn red is the name of the color of a lipstick.
Right? What do we what do we do with that?
We looked at product images that were there. And in that,
there's lighting and different kinds of images there. So lighting
we if we go and look at certain pixels, they're yellow even though it's a pink clip
Right? So to start off, one thing that we move forward with in the design
was essentially we would create a modular pipeline a modular data pipeline
we can use during our data collection phase. And then after that,
once we have enough data to create the models, use
use that same pipeline to now instead of sending ground truth labeling.
In either instead of that or in parallel, we would now host
SageMaker endpoints, like like
host our models on SageMaker endpoints and, like, essentially call those
while getting some verification being done at the same time.
What do I really mean about this is in the beginning, we had these images
in categorized. We did detail transforms and
like, create one standardized format for all different product types.
And then we send those to ground truth labeling data
like, as a a ground truth service, which would send it, like, worldwide where
would take those jobs and do, like, bounding boxes
in different areas of the image. And we did use this
pipeline itself for for data scientists and applied scientists to have a look at the data, see what kind of
models that we can come up with. So a lot the work
for the ML models itself was done quite a bit, like, in
collaboration with our data scientists and applied scientists. But, like, all the data provided to them was
this pipeline itself where they had the flexibility of changing experiments, doing different
kinds of experiments. And once they had the data, enough data to
create those machine learning models, which were hosted on the
as I said, like, the AWS SageMaker endpoints. We had, like, batch
batch transform jobs and even, the real time endpoints.
Right? So we use leverage both of those
and from step function itself, we would call those models
that were, like, raised in their SageMaker registry and then
like, get our data and even be able to create comparisons because sometimes in parallel, we would send
them to labelers. And we started off with, like, you know, just as a a
fun prototype, see if we can do the average of the pixels
and compare like, that was our baseline, like, the first baseline.
And it helped with, like, the modularity of this whole pipeline being able to
work with massive data distributed in, like, so many different places.
And, like, all of that kinda came together with
step functions, orchestration. Nice.
It's good to hear you all. They have some experience on SageMaker, Basham,
that's something that we heavily use as well.
Have you worked on LLMs before? Like,
or do you use LLMs? I've like like, life
would right now, I think, like, as a engineer, life would be, like, like, very
different without LLMs or it like, LLMs has
made it very different. So
essentially, I've had the chance to, like, go into into depth
just for own personal, like, interest and projects.
I did create, like, my own, like, GPT, like, the mini basic
GPT where, trained it with, like, four sentences
obviously. It was only able to respond to that. But, in terms of, like, going
pretty foundational, I've had a chance to deal with them that way.
Applying them, applying LLMs at, like, at my
own personal projects. Like, I've, like, done API calls and whatnot.
Now at work, like, at work level scale, like, what our experience has been
as we did try, like, for the same, you know, how we were having the unicorn red
problem, like, getting the exact colors and getting
like, always, like, customer reviews where they would say,
hey. Your, like, the video like, it's it's looking very different. Like and I
purchased it. It's a lot lighter. So extracting details, we did experiment with that.
And trying to customize and fine tune our own models to to do this kind of thing.
One thing we learned is every day or, like, more like every month,
we are having better models coming in that are have reduced
costs and whatnot. So biggest principle that we kind of, like, kept in
is let us not be that good
to dive deep dive into this issue, at least at our level. In our case, we realized
because there were a lot of out of the box thinking we could do.
Where even we contacted our clients, please submit the photos in this particular
if you can. So that improved our data. Working on, like, like,
even text extraction, we asked them, here's a new standardized way of
like, giving r RGB values
Let's work on that. And LLM side, we still continue to use that.
But we remain model agnostic so that
we leverage, like, better we use better cost savings
and newer models to extract things out of customer reviews.
And applied those in this particular project. Got it. Yeah. What kind of a
use? Like, was that, like, a
standard LLM? Oh, like, the the latest
and greatest models that we were having and during that time.
But, like, one experiment with that we enjoyed was with, like, Olama as well. Like,
locally using Olama. We would serve our own smaller models.
And kinda split the queries and split everything, like, kinda do reasoning on our own.
Then again, we saw reasoning coming in from
other different models, but the ones specifically that we use in, like, voice
like, the GPT four model that we had, like, in our early days.
Then the four o. And then from the anthropic side,
got a chance to deal with, like, like, the clot three and then three point was it? No. It was three point five first and then later on seven.
At seven, we did get to use it because it wasn't released then. But Like, it was
fun to experiment with these. Yeah. I mean, we we've been playing around with all all of these. I mean,
I think we used to use Anthropic before, but we do it anymore.
But we're pretty
we've been experiencing a lot with open animals and also, like,
actually been pivoting to Gemini quite a bit because it's
it's Large context. It's stupid. Large context is also very cheap. Like,
surprisingly Yes. Very cheap.
So yes, I mean, each has its own challenge
I would say. Kind of. So that's the fun part that we're dealing with all
this all this in terms of Prompt engineering is the key as cliche, and a lot of would
say, like, yeah, like, oh, yeah, like, it's everyone is kinda doing that.
But it definitely comes in handy as cliche as it may sound. Yeah. No. I think for
the journey for us has not been that I mean, it it there's definitely, you know, a
tricks and tips on problem engineering. But I think we've
got to a stage where we kind of figured most of that stuff
out. Mhmm. But it's just the scaling part, which is which I'm thinking, like, because we're running with, you
like, two hundred two hundred fifty million documents. That's
just where we are trying to sort of run it. And we we ran recently with 25,000,000, which
we were able to do it, but we're 10x ing the capacity now.
That brings all kinds of challenges. It's fun stuff to work on. 100%.
Maybe a couple of quick questions. I know you're very
familiar with Python. Have you worked with Scala before?
I have not. I haven't had the chance to work with Scala, but Python is
definitely my go to, I'd say.
Okay. What about Spark? Have you done anything on Spark?
So Spark was something, like, we did consider during the design review. Like, we would always have,
some internal design review before we actually move forward. Spark was one of the big options in there of
obvious reasons. But then there were some cons
to Spark. So we I have had a chance to just have
like, review it as, like, very early stage, like, having having having
learned about it, but we use the spark patterns, like the benefits that we were getting
from using, like, Spark in our pipeline, we actually were getting those
through, like, our infrastructure that we ended up, like, that I ended up recommending
and actually even using with, like, step functions, combination
of Lambda and Athena and various many other tools.
It let us have, like, biggest quick reason if I were to say would be, like,
like, modularity and being able to switch things very quickly in between and having
like, build the whole pipeline in a way where it was
like, being able to go outside just the the environment that
like, we we are working in and be able to call things easily,
like SageMaker and everywhere outside. Of course, it wasn't that big of a deal, to be honest,
like, later as we learned more about it. But, definitely, it turned out that
like, our all the patterns that we that I saw in Spark, we were able to just
replicate that and get some more advantages from our step function pipeline instead.
Cool. Awesome. Are you are you interested in learning Spark?
Oh, absolutely. It almost felt like a natural, like, next step.
Because one of the other reason in, not going for the Spark route was all
junior developers and everything. And with the timeline that we had, we wanted to kind of keep things
with the experience the prior experience that our entire team has
had before, which was with step functions. It kinda made it simple, but
interested, 100%. It it feels like the next
graduation level. Okay. I mean, the reason I asked is because we've got two different
setups on the team. So we've got, like, you know, a lot of things that the router and spark
I'd say most of them are in Scala.
The team likes to work or write as or use Scala for Spark.
So we've got some of these pipelines that's actually set up
in Spark running off thirty day airflow.
Then we've got all the newer stuff we're building on AWS. So we are AWS shop. Everything is sort of like
we've started using stuff from most of it is Lambda, Sqa,
that we have built, sort of like a framework around it as well.
So just wanted to sort of highlight that. I mean, it's not a deal breaker that
you don't know Spark based as long as you're running
Oh, 100%. Like, we have picked, so many languages and everything that, like,
so many new technologies at like Amazon. So I
don't see that as an issue at all, to be honest. Unfortunately, our job
requires us to learn all the time. So Of exactly. This is worth given. So
in terms of, like, know, you in your work with some of step
function Lambdas I had to work with.
40 terabytes per day. Did you want to do any
scaling changes? Was there any sort of scaling changes? Maybe two maybe a minute. Okay. And we'll see. Yeah.
Absolutely. Like, we had, like, the the trade offs we had to always
make, and we had, like, things, like, like, always on infrastructure and the serverless infrastructure.
So we went towards that, like, where we had the auto scaling and pay per use.
So, like, the challenge itself in initially was
like, when we put like, did a prediction of how much it's going to cost.
Like, right then and there is where we decided, like, when we went for serverless,
because we didn't want always on servers. We wanted batch transform. That's why we
went for, like, more of batch transform jobs even on the machine learning side.
We would get everyday data and then so essentially, the the
the challenge was the cost escalating during the early design stages.
And we dealt with that by using the serverless sides, which was the Lambda and step functions.
We had auto scaling set up in there. We had it configured
The paper use pricing came in handy, and we actually that resulted in $3,030,000 more more than that projected savings annually had begun
with the like, always on infrastructure, we would have
to have paid that and hand yeah.
Whereas we essentially dealt with it automatically. Cool. Awesome.
Can you maybe it's gonna be last question, and you know, I'll open up for any visits here.
Can you talk about a project where you had to deal with ambiguity, like
the requirements were already
not not clear. Mhmm. You had to take it, set goals, and then had to
drive towards that goal. 100%. I think it would be the project Scott that I may have mentioned to Neha earlier.
Where we essentially like, the problem was
our documentation. We did not have a great time. A lot of complaints were, like, we
being escalated, and we had lots of issues with new people joining the
team. We didn't have, like, a good infrastructure there
to keep on maintaining documentation and, like,
it was a mess. Right? But and that happens with a lot of teams. Mhmm.
There, we had so much ambiguity in terms of how do we deal with that. Like,
like, sure, we can have we can talk about, like, mechanisms and whatnot.
I essentially came up with, like, as as a side project,
that started off as a side project at at work. It became something big, was the project
Scott, which was the AI documentation agent where we had, like, rack pipelines with vector
databases, metadata, like, extraction from internal docs
and essentially, like, you know, like,
there we had to it it was so easy for this to become too big
of a project and, like, could go, like, experiment with a lot of directions.
But dealing with that, figuring out exactly what needs to be done,
So I kind of, like, proposed this project with a prototype to them and that
kinda actually became one of the big things at the company itself.
So, like, dealing with ambiguity is something that just, like,
we even do it for fun. So
like, it's it's something that I've always enjoyed. Like, okay, like, working backward
Like, if I were to summarize it in now, like, one last sentence, it would be
working backward from what exactly is the problem. Let's prioritize the the right things in there.
And then, like, tackle it, like, in a modular way.
So that's something that I've had a lot of experience with, and I think
it would be fun to tackle more such things.
Cool. Awesome. That's great to hear.
And we only have four minutes. I have a couple more questions, but let's
let's go to your questions.
Happy to answer anything. Yeah? We can go into more questions from your side. If you have
or or maybe I can have one quick one if you'd like, whichever you prefer. I think think I think I'm good.
Like, I just wanted to sort of understand a bit more about the
documentation agent. Like you mentioned, you set up the RAC pipeline, made data extraction, like
how did you do that? Like, what was the what was the
what was the setup? Oh, so the setup essentially, like, we had, like,
the Slack integration that would ask the questions.
Right? And then in the Rag pipeline itself, we would have, like,
FAISS, like, the PHYs, and, like, we even experimented with, like,
like, Pineco and ChromaDB. Like, it was a very in prototype
stage, like, when I actually had to leave, like, Amazon, like, when we when I left Amazon. So
like, the prototype stage that we built there was essentially
like, we we would have, like, vector database that would essentially
find the best, like, top documents that that, would be closest to the
query that's being matched. And we had more experimentations into, like,
whatever query there is, we would, like, split it into multiple smaller queries.
And then we had agents dealing with all of those
split agents, like, separately. And then we would essentially, like,
I I know I'm going back and forth, but there's the vector databases would help
get the right documents. We would send that to all our agents.
And, to, like, to with
to attach the context and get back the response, and then we would have, like, further
dynamic agent creations where we created, like, new agents on the fly if needed.
If something wasn't already there. So it was some good experimentation fun
for some project kind of situation. So it was all local, but then we had like like, I had
like, the plan ready for how this would scale on to, like, AWS.
Like, all the Lambdas and and whatnot. Yeah.
So when made you leave Amazon? So it was in March,
'25. We were like, me and my team, like, we were laid off.
It was essentially, like, me, my manager, my manager's manager, we were all
affected by it because we had, like like, the our team was being merged
into a different team. That's why, like yeah. Got it.
Yeah. Okay. Yeah. Awesome. Yeah. I know. If you have any questions, happy to
even stay back a few minutes as well to answer. I I have a
question about like Neha, remember mentioned about like this
ascribe ascribe ever end and slideshow Right. Script. Sorry. Yeah.
It'll come handy for you next round. So Sure thing.
Scribd, Iran, and Slideshare are like the different three different products
types? Like, you you know, like, the ebooks, audiobooks, and presentations
So that was something that I was intrigued by.
I mean, good question. So
just some history there. So script started off as a white
Combinator startup. It was one of those first batches, I think,
along with Sam Altman's Lutt, I think, if you know the history there.
But it's been around for a long time. So script has been our primary brand.
In February, I think maybe
five years back or six years back, we bought Slideshare from LinkedIn.
It's a completely sort of like a separate platform. We haven't integrated
slideshow into script yet. And then on our end, we actually split
some of our premium business, which is, you know, ebook, audiobooks Mhmm.
From script into Everland plan. So Everland essentially is actually having the script
back end, sort of like a different sprint end. So just how the data pipeline is set up,
Script and slides are, I would say, share a lot of things together because they have been
sort of primary same pack. And Slideshow, on the other hand, is
kind of separate. This platform is separate. But as a data engineering team, we have been sort of
trying to sort of
consolidate all of that stuff. So the way we are doing that is we're sort of setting up these data pipelines that
serves all brands, which is very important.
Because you don't want to replicate the whole thing. But we've been setting up these
sort of like brand agnostic pipelines where you sort of feed in like
kind of things in it. So it could be a script document ID versus a slideshow document ID.
And then we sort of pull data from different S3 buckets, for example. And then
do the processing and then push data to different data. So
we are trying to move to a place where we don't replicate a lot of
this work, where some of this stuff is sort of duplicated right now, and there's some efforts to sort of consolidate
of that stuff. Maybe a 2026 product, but yes, that's sort of
how it's also. Perfect. That sounds great, Lavin. It very much sounds like because, like, in our case, I only
showcase showcase, like, VTO project, which was one of the downstream things.
But later on, like, the the essential initial pipeline that I had built,
it served pretty much every sister team that we had
where you want recommendations. You kinda, like, have it all consolidate one place.
Not just images, but even, like, text and any kind of data
We almost, like, became the go to people instead of people having to
create tickets with other teams to get catalog data or images
or, like, customer reviews. So it does sound like something that would be
like, very interesting dealing with different kinds of data all put together and data
massive scales. Yeah. Yeah. I mean, we would I mean, we would so much
data. We are trying to sort of figure out how to actually reduce it because it's just like
it just at some point, it becomes more of a liability than, you know,
for numbers. 100%. So so, yeah, I mean, there's some stuff we are doing right now, but
mean, it's to give you a little bit more background in terms of what the team works on. So
primarily, the team works in two sort of initiatives. One is
content moderation. So you could think about it's called content trust, but it's mostly moderation. So
any document that are uploaded on script or any of this platform, we want make sure it
addresses our policy. So there's a bunch of tools that we use for that. We put some collaboration
with Google to use some of their tools. We have in house
built tools using fingerprints and all that. So there's one another set.
And then we started to use LLMs quite a bit as well. So we prompt
LLM to see if it actually violates our policy. So that's one set of
domain that we work on. The second set of domain is content enrichment. So it's basically made at
extraction, what I spoke about before. But also,
generation metadata as well. So for example, one of the bigger projects that we worked on this year is
to generate titles for your documents. So users upload these documents, titles are pretty crappy.
So what we do is we throw a LLM and then generate a title for it. So
it's got various benefits into the SEO and
that. The second set of project or second product
which has been pretty big product that we have worked on is to generate table of content for a documentary
document plan have table of contents where we generate one. We also
are working on a planet where we take these high popular documents on
script in a particular language, for example, English, and then we translate it into Portuguese or
other languages where the document is not available. We just
it sounds pretty straightforward because translation is around for a while.
But the hard part there is to sort of keep
the structure of document as it is. So we keep the fonts, we keep the
image asset. So it's basically just translating the entire document assets, keeping the structure
and the format assets, which is
generally a lot more challenging problem than what we thought, but we have got around it, like we have
already started pushing things, but that's sort of like the
of product that's going on, I think. Nice. That that is very insightful. That was very helpful.
To understand and get more insights into, like, exactly how
but not exactly, but more like like one level deeper into
what's happening at at Script. Cool. Yeah. If you have any other questions,
happy to take it. If not, we can end it there. I mean, I was
I have actually many questions, but, like, I think I would, like, be No. Go for it. Yeah.
One thing like, I I I wanted to ask,
give me one second. Let me is it okay if I pull that up, the the questions?
Because that one I had remembered. Now I'm, like, so I I learned so many things, and I'm
a little bit flustered into oh, wait. Give me one moment.
This one, let me see if I you've already answered that, but
Like, you have actually answered quite a few of the questions. But
yeah, LLM for data enrichment, you've already talked about that.
Actually, this would be very helpful. I think, like, the
what what is the biggest challenge? Like, you have mentioned one of the like, a few of the challenges
but you have talked about, like, how two of the challenges
you'd already tackled and, like, about keeping the structure and you tackled that and even
prompt engineering things earlier, much earlier you mentioned you've tackled
that part. What is the current biggest data engineering challenge at the
team is facing? And, like, is it scale data quality
integration with complexity or something else? Yeah. So from a
I mean, part of the reason why we're hiring more is because
there's a lot of demand coming in for the team to actually work on some of these things. And
And to just give you some ideas there,
script as a whole is sort of focusing on some of these
as a research platform, so where users can come and do research.
And obviously, with the advancement of LLMs, can imagine there's sort of
so much you can actually care of it. And part of the problem that we have right now is
like we don't have enough
capacity to produce whatever the company needs, so that's why we are hiring. And
in terms of challenges, scalability is a
challenge. Like some of these projects that I mentioned, we ran into the scaling issues that
we did not anticipate that, for example, OpenAI did not
know there would be a challenge because we're hitting some of these limits.
So working with teams, like some of teams, sort of figure some of these things out.
But scalability is a challenge, and we are using now
multiple LLL, which just brings another level of complexity for us
because sometimes you have to for example, some of these models
example, if you want to use OpenAI and if you want multi model capabilities, you have to take
screenshot of images or pages to actually send it
them. And we've got two fifty million documents into like 27 pages per document. You're looking at 6,500,000,000 images and then sending that over the
network for every single inference. Adds to the complexity
there. So we're working on some of those challenges, and like I do expect a lot more demand
coming in for some of these LM infirms next year, which also means we need to
mean, we can't keep building the same pipeline every single time. We have to sort of generalize some of that
stuff like how can someone come up with a prompt to the team and then sort of
do the prompt engineering, pick the right model, and then run inference
and then export the data all pretty seamlessly and
quickly. We can make it self serving, great, right? So
that's the stuff that that's sort of like the vision as well where someone comes up with a prompt,
select budget doc in the few thousand to like few millions to hundreds of millions.
Then being able to export the data. So that's the part that we
are sort of focusing on right now, and that's going to be a challenge that we will work on in 2026.
Nice. That that is very like, like, it's it's a very common problem, and it's
something that I myself, like, experimented with was
like, how how do you break those things down? And can we use, like because, like, the cost
scale. Like, LLMs are great. They're doing you have created the you've used the
four four point one Opus, and you have put in a great prompt, like,
I'm getting the best possible answer and there's a big hole in
my pocket because of the costs. Right? So or it's
the speed. Right? There's so many aspects of it. How do you find that right balance?
Myself, like, I've I've been intrigued by this exact problem, and we
all like I'm like, what how I've tried to solve it, attempted to solve it,
and been very successful as well would be, like, the breaking down
where Mhmm. Wherever like, not just by prompt caching the prompts,
but even by, like, can we, on the fly, do certain learnings
that these are common steps, three steps that I'm always doing
if we were to break something down. Can we
like, create some, like, Python code that would literally like, the
minor points in there, they actually aggregate to a point
where
almost 40% of the entire task is now being done with
some Python code. It's returning back, like, doing cleanups. And then
what what happens is, like, we keep try to keep on increasing that 40% number.
Further and reduce the work, whichever is the
dynamic part, what's new in the query only working
sending that to LLM because it was seemed very waste
for, like, exact same thing. You're asking, like, at because when when you scale things,
these thing add up, like, either the speed or the time.
With with both those things, think the these are one of the
few things that, like, we we learn from our experimentation phase.
And, like, tried having to deliver not just
having fun experiments. I think combining the two things together
was something, like, I I personally myself enjoyed as well.
Nice. Yeah. Yeah. I know. I'm glad to hear you've got the experience on all those things.
And and these are stuff that, you know, like, the team is sort of looking into right now, and I'm sure, know, there's
gonna be some some of these experience that you have that will come handy for us.
I'm glad to hear that. Cool.
Perfect. Well, thank you so much. Yeah. If there's nothing else,
you know, we'll end it there, and then Neha will reach out to you with the with the next steps.
Perfect. I appreciate that. Awesome. Thank you. Take care. Bye.
So all of this right now is the transcription from the interview itself.
Now what I want you to do is basically
you cannot access this directly right now, I want you to copy and paste
whatever is inside the like, you know, if you go into this
macOS file system, you would find that there's this
like, in the home folder in the there you would find a code
folder, like, folder called code. And then in there, you would find


