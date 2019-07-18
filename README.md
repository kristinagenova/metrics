# metrics

### How to install 
- Clone
- Install requirements from requirements.txt
- Set SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD and DJANGO_SETTINGS_MODULE (normal settings and test settings) in the enviroment

### Assumptions under I have worked
- You only need to filter from/to date.
- I realize that to follow proper REST protocol I should use a GET request instead of POST to get some data from the server.
  However, in my opinon, this solution wasn't very clean and was leading to a long/clunky url which was very hard to parse. 
  A very long url can lead to 414-url-too-long. I decided to go with a POST instead. I considered other methods such 
  as sending the data in the session but that also didn't seem optimal.
  
### Documentation
##### The api will expect input in the following format.
```
{	
	"show": ["impressions", "clicks"],
	"filter": {
		"date": {
			"approx": "to",
			"date": "2017-06-01"
		},
		"country": "CA"
	},
	"group" : ["channel", "country"],
	"sort" : {
		"order" : "-",
		"field" : "clicks"
	}
}
```
- You can add or remove fields to change your query.
- You are obliged to have at least one value for all fields i.e show, filter, group, sort.
- if you want to add a date as a filter you add another json object within the filter field like so. 

```
"date": {
	"approx": "to",
	"date": "2017-06-01"
}
```
- if you want to filter for a time period before the date in the `"approx"` keyword you pass `to`.
- if you want to filter for a time period after the date in the `"approx"` keyword you pass `from`.
- if you want to filter for events on that specific date you can leave the `"approx"` field blank.
- the logic is similar for the `sort`

```
"sort" : {
	"order" : "-",
	"field" : "clicks"
}
```
- if you want a descending order the `order` field must have a value of `-`
- if you want an ascending order the `order` field can be blank 

### How to use

- Go to the endpoint http://localhost:8000/api/metrics/
- Go to Postman and input your post value as raw json 

#### Examples

1.Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

```
{	
	"show": ["impressions", "clicks"],
	"filter": {
		"date": {
			"approx": "to",
			"date": "2017-06-01"
		},
	},
	"group" : ["channel", "country"],
	"sort" : {
		"order" : "-",
		"field" : "clicks"
	}
}
```

2.Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order. (I realize that because of my implementation this is impossible - with more time I would have extended the `date` field to handle for those cases)


3.Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

```
{	
	"show": ["revenue"],
	"filter": {
		"date": {
			"approx": "",
			"date": "2017-06-01"
		},
		"country": "US"
	},
	"group" : ["os"],
	"sort" : {
		"order" : "-",
		"field" : "revenue"
	}
}
```

4.Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

```
{	
	"show": ["CPI", "spend"],
	"filter": {
		"country": "CA"
	},
	"group" : ["channel"],
	"sort" : {
		"order" : "-",
		"field" : "CPI"
	}
}
```

Feel free to contact me if any question arise!
