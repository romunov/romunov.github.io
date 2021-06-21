title: Working with Notion API from R
date: 2021-06-21 19:30
tags: R, API, Notion, json, httr
keywords: Notion, API, httr
category: HowTo
slug: working-with-notion-api-from-r
author: Roman Luštrik
summary: There are a few tricks I needed to figure out to be able to talk to Notion via its API.
lang: en
status: published

When searching for a solution where I could store some flat files as a database, [Notion](https://www.notion.so/) came up. The nice thing about it is that it offers an API to most of its functionality. At the time of this writing this is still in beta, but hopefully it will become even more powerful in the future.

The functionality I'm concerned with right now is interacting with the databases. The boilerplate code to start communicating via the Notion API is

```r
library(httr)
library(jsonlite)

NOTION_KEY = "enter-your-key"

ask <- GET(
  url = "https://api.notion.com/v1/databases/",
  add_headers("Authorization" = paste("Bearer", NOTION_KEY),
              "Notion-Version" = "2021-05-13"))
stop_for_status(ask)
fromJSON(rawToChar(ask$content))
```

You should get an R list of elements returned by this `databases` endpoint.

To write to a database (add a row), you need to prepare an object that corresponds to the corresponding table schema. A JSON object would look like something like this:

```bash
properties: {
      Name: {
        title: [
          {
            text: {
              content: 'Tuscan Kale',
            },
          },
        ],
      },
      Description: {
        text: [
          {
            text: {
              content: 'A dark green leafy vegetable',
            },
          },
        ],
      },
      'Food group': {
        select: {
          name: '🥦 Vegetable',
        },
      },
      Price: {
        number: 2.5,
      },
    },
```

Using a similar logic, I wrote my call in R

```r
pb <- list(
  parent = list(database_id = NOTION_DATABASE_ID),
  properties = list(
    Name = list(
      title = list(text = list(content = "4"))
    ),
    Genus = list(
      rich_text = list(text = list(content = "Neki"))
    ),
    Species = list(
      rich_text = list(text = list(content = "noviga"))
    )
  )
)
```

but this produced the following error

```bash
body failed validation. Fix one: body.properties.Name.title.id should be defined, instead was `undefined`.
body.properties.Name.title.name should be defined, instead was `undefined`.
body.properties.Name.title.start should be defined, instead was `undefined`.
```

Long story short, it turns out that every curly braces and array need to be a `list()`. This worked (notice the extra `list()` calls compared to the original):

```r
pb <- list(
  parent = list(database_id = NOTION_DATABASE_ID),
  properties = list(
    Name = list(
      title = list(
        list(text = list(content = "4"))
      )
    ),
    Genus = list(
      rich_text = list(
        list(text = list(content = "Neki"))
      )
    ),
    Species = list(
      rich_text = list(
        list(text = list(content = "noviga"))
      )
    )
  )
)

send.row <- POST(
  url = "https://api.notion.com/v1/pages",
  add_headers("Authorization" = paste("Bearer", NOTION_KEY),
              "Notion-Version" = "2021-05-13"),
  body = pb,
  encode = "json"
)
```
