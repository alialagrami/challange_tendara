## Notice matching
There are thousands of new tender notices published every day across the EU. These include all sorts of supplies and services that public institutions need to procure. From buying cleaning supplies for schools to building railways, you name it. Legally, the buyer is required to publish a notice on public procurement portals. One of the biggest European portals is [TED](https://ted.europa.eu/). You could try searching for notices there, e.g. you could try something like "AI projects", but as you will notice it's not the most user-friendly interface.

Imagine we are working with a cutting-edge AI consultancy called GovAI that builds novel AI applications for public institutions. For example, one of their projects could be building a chatbot to help people navigate the city's website. They do not sell any hardware or servers, it's mostly consulting / implementation projects. They are currently searching for new projects and want to find contracts that are relevant for them. They are subscribed to different portals and get notified about new notices, but there are too many irrelevant results for them to go through manually.

Most notices also have nothing to do with AI IT projects, and hence completely irrelevant. We want to build a matching algorithm that will find only the most relevant notices for the client. Unfortunately, categories like CPV codes / locations are not always present in the notices, and they are not always reliable.

Concretely, we want to be able to make a Search Profile for each customer where they can set the criteria for the notices they are looking for. This search profile can be as simple as a set of keywords or more complex rules including location / volume / CPV codes etc. You can also decide what you want to ask the user to set up the search profile.

We generated a synthetic dataset of 100 notices. It's in the `data/notices.json` file. In utils.py you will find a small helper function to load the data. You can see the structure of the notices defined in Notice pydantic model with comments for each field.

TL;DR: There is a bunch of notices and your job is to write a function that will only return the relevant ones for the search profile.


### Questions to consider:
You don't necessarily have to give a written answer to these questions but this is something that we will discuss with you during the interview:

- What are some tradeoffs in your solution between around quality of results? Are you optimising for recall or precision?
- How would you change your approach if you had 100k or 1M notices?
- How would you build the pipeline to get the data in the first place? What if it's spread out across 100+ different portals? What architecture would you use for this?
- How would you ensure the quality of data, since we know that sometimes there could be fields missing in the notice that are in the documents?
- How would you deploy this matching as a service, considering also how long it takes to actaully give the recommended notices?