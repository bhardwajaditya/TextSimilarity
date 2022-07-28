# Text Similarity

##### Flask based API to check if the target text is similar to available texts
#


### API Provides :-

* Endpoint to check if the target question is similar to available questions

### Setup and Installation :-

1. Clone the git repository.
2. Make sure python3.5+ is installed.
3. Install the requirements listed in requirements.txt

### Running the REST Server
```emacs
$ cd TextSimilarity
$ python api.py
```

### Sample Request

```javascript
{
    "questions":[
        "Which of the following is a fruit",
        "Which of the following is a vegetable"
    ],
    "target": "Which of the following is not a ghost"
}
```