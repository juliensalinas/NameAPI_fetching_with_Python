## Example of JSON data sent through a POST request body in Python using the real case of NameAPI.org fetching

JSON data to send:

```json
{
  "inputPerson" : {
    "type" : "NaturalInputPerson",
    "personName" : {
      "nameFields" : [ {
        "string" : "Petra",
        "fieldType" : "GIVENNAME"
      }, {
        "string" : "Meyer",
        "fieldType" : "SURNAME"
      } ]
    },
    "gender" : "UNKNOWN"
  }
}
```

cURL command:

```shell
curl -H "Content-Type: application/json" \
-X POST \
-d '{"inputPerson":{"type":"NaturalInputPerson","personName":{"nameFields":[{"string":"Petra Meyer","fieldType":"FULLNAME"}]}}}' \
http://rc50-api.nameapi.org/rest/v5.0/parser/personnameparser?apiKey=<API-KEY>
```

NameAPI.org's expected response:

```json
{
"matches" : [ {
  "parsedPerson" : {
    "personType" : "NATURAL",
    "personRole" : "PRIMARY",
    "mailingPersonRoles" : [ "ADDRESSEE" ],
    "gender" : {
      "gender" : "MALE",
      "confidence" : 0.9111111111111111
    },
    "addressingGivenName" : "Petra",
    "addressingSurname" : "Meyer",
    "outputPersonName" : {
      "terms" : [ {
        "string" : "Petra",
        "termType" : "GIVENNAME"
      },{
        "string" : "Meyer",
        "termType" : "SURNAME"
      } ]
    }
  },
  "parserDisputes" : [ ],
  "likeliness" : 0.926699401733102,
  "confidence" : 0.7536487758945387
}
```

This repo does the above using Python.
Here is an [in-depth explanation of this script](https://juliensalinas.com/en/REST_API_fetching_go_golang_vs_python/) and comparison with Go.