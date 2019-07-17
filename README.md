# metrics

### How to install 
- Clone
- Install requirements
- Set SECRET_KEY, DB values and DJANGO_SETTINGS_MODULE (normal settings and test settings) in the enviroment

### Assumptions under I have worked
- you only need to filter from/to date
- I realize that to follow proper REST protocol I should use a GET request instead of POST to get some data from the server.
  However, in my opinon this solution wasn't very clean and was leading to a long/clunky url which was very hard to parse. 
  A very long url can actually lead to 414-url-too-long. I decided to go with a POST instead. I considered other methods such 
  as sending the data in the session but that also didn't seem optimal.
  
### How to run 
- Go to http://localhost:8000/api/metrics/
- the API expects input like the format below so you can use PostMan to send it
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
- You can add or remove fileds to change your query
- If you add anything but the "show", "filter", "group", "sort" the API will not take the input into account
